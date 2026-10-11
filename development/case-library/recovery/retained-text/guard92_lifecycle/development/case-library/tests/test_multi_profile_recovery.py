"""Profile isolation under concurrent builds and failed OT1992 publication.

Every mutation is confined to disposable fixture repositories. These checks
exercise the shared lifecycle with the retained pilot and both complete terms.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import threading
import unittest
from unittest.mock import patch

import test_ot1992 as fixtures


pilot = fixtures.pilot
PROFILES = (None, "OT1991", "OT1992")


class MultiProfileRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.OT1992Tests(methodName="runTest")
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.fixture.copy_catalogue("OT1991")
        self.root = self.fixture.root
        self.pointer_path = self.fixture.pointer_path

    def scope(self, profile):
        return self.root / pilot.catalogue_path(profile)

    def bytes_under(self, profile):
        return self.fixture.bytes_under(self.scope(profile))

    def build_profiles(self):
        return {profile: pilot.build(self.root, catalogue=profile)[0]
                for profile in PROFILES}

    def assert_older_preserved(self, before):
        for profile, expected in before.items():
            with self.subTest(preserved_profile=profile or "retained pilot"):
                self.assertEqual(self.bytes_under(profile), expected)
                pilot.load_snapshot(self.root, catalogue=profile)

    def test_other_profile_pointer_requires_scoped_recovery_and_preserves_snapshots(self):
        folders = self.build_profiles()
        older = {profile: self.bytes_under(profile) for profile in PROFILES[:-1]}
        previous_files = self.fixture.bytes_under(folders["OT1992"])
        # A valid pointer copied from another catalogue must not redirect reads
        # to that catalogue or cause recovery to alter its snapshot history.
        misplaced = (self.scope("OT1991") / "CURRENT.json").read_bytes()
        self.assertNotEqual(json.loads(misplaced)["build_id"], folders["OT1992"].name)
        self.pointer_path.write_bytes(misplaced)

        with self.assertRaisesRegex(pilot.PilotError, "Current snapshot is damaged"):
            pilot.build(self.root, catalogue="OT1992")
        self.assertEqual(self.pointer_path.read_bytes(), misplaced)
        self.assertFalse((self.scope("OT1992") / "recovery").exists())
        self.assert_older_preserved(older)

        restored, report, changed = pilot.build(self.root, catalogue="OT1992", recover=True)
        self.assertTrue(changed)
        self.assertEqual(restored, folders["OT1992"])
        self.assertEqual((report["term"], report["case_count"]), ("OT1992", 123))
        self.assertEqual(self.fixture.bytes_under(restored), previous_files)
        backups = list((self.scope("OT1992") / "recovery").glob("*/CURRENT.before.json"))
        self.assertEqual([path.read_bytes() for path in backups], [misplaced])
        self.assert_older_preserved(older)
        pilot.load_snapshot(self.root, catalogue="OT1992")

    def test_publication_failure_rolls_back_only_ot1992_and_reuses_retained_orphan(self):
        folders = self.build_profiles()
        older = {profile: self.bytes_under(profile) for profile in PROFILES[:-1]}
        previous = self.pointer_path.read_bytes()
        previous_files = self.fixture.bytes_under(folders["OT1992"])
        selection = self.fixture.selection()
        selection["cases"][0]["aliases"].append("Reviewed OT1992 recovery fixture")
        self.fixture.fixture.write_json(self.fixture.selection_path, selection)
        reviewed = self.fixture.selection_path.read_bytes()
        original_atomic = pilot.atomic_file
        interrupted = False

        def fail_after_pointer_replacement(path, data):
            nonlocal interrupted
            result = original_atomic(path, data)
            if Path(path) == self.pointer_path and not interrupted:
                interrupted = True
                raise OSError("Injected interruption after OT1992 pointer replacement")
            return result

        with patch.object(pilot, "atomic_file", side_effect=fail_after_pointer_replacement):
            with self.assertRaisesRegex(OSError, "Injected interruption"):
                pilot.build(self.root, catalogue="OT1992")
        self.assertTrue(interrupted)
        self.assertEqual(self.pointer_path.read_bytes(), previous)
        self.assertEqual(self.fixture.bytes_under(folders["OT1992"]), previous_files)
        self.assertEqual(self.fixture.selection_path.read_bytes(), reviewed)
        self.assert_older_preserved(older)

        orphan, = [path for path in (self.scope("OT1992") / "builds").iterdir()
                   if path != folders["OT1992"]]
        orphan_files = self.fixture.bytes_under(orphan)
        restored, _, changed = pilot.build(self.root, catalogue="OT1992")
        self.assertTrue(changed)
        self.assertEqual(restored, orphan)
        self.assertEqual(self.fixture.bytes_under(orphan), orphan_files)
        _, entries, _ = pilot.load_snapshot(self.root, catalogue="OT1992")
        self.assertEqual(len(pilot.lookup(entries, "Reviewed OT1992 recovery fixture")), 1)
        self.assert_older_preserved(older)

    def test_distinct_profiles_build_concurrently_but_same_profile_is_locked(self):
        # All three builders must acquire their respective locks before any
        # preparation proceeds. A mistakenly shared lock fails this barrier.
        prepared = threading.Barrier(len(PROFILES), timeout=30)
        original_prepare = pilot.prepare

        def concurrent_prepare(root, *, catalogue=None):
            prepared.wait()
            return original_prepare(root, catalogue=catalogue)

        with patch.object(pilot, "prepare", side_effect=concurrent_prepare):
            with ThreadPoolExecutor(max_workers=len(PROFILES)) as executor:
                jobs = {profile: executor.submit(pilot.build, self.root, catalogue=profile)
                        for profile in PROFILES}
                results = {profile: job.result(timeout=90) for profile, job in jobs.items()}

        for profile, (folder, report, changed) in results.items():
            with self.subTest(profile=profile or "retained pilot"):
                self.assertTrue(changed)
                self.assertEqual(folder.parent, self.scope(profile) / "builds")
                self.assertEqual(report["term"], profile or "OT1991")
                pilot.load_snapshot(self.root, catalogue=profile)
        before = {profile: self.bytes_under(profile) for profile in PROFILES}
        with pilot.build_lock(self.root, catalogue="OT1992"):
            with self.assertRaisesRegex(pilot.PilotError, "Another pilot build/recovery"):
                pilot.build(self.root, catalogue="OT1992")
        for profile in PROFILES:
            self.assertEqual(self.bytes_under(profile), before[profile])


if __name__ == "__main__":
    unittest.main()
