"""Adversarial storage tests use disposable repositories, never Court records.

The tiny collector is deliberately independent of legal parsing: each call reads
the fixture anew. These tests exercise publication, source freshness, integrity,
and recovery, while ingestion has its own tests with actual record formats.
"""
from __future__ import annotations

from hashlib import sha256
from html import escape
import json
import multiprocessing
import os
from pathlib import Path
import shutil
import signal
import sys
import tempfile
import unittest
from unittest.mock import patch


AREA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AREA / "tools"))
import library


def encoded(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="case-library-lifecycle-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repo"
        self.base = self.root / "development/case-library"
        self.base.mkdir(parents=True)
        for name in ("schemas", "tools", "inputs"):
            shutil.copytree(AREA / name, self.base / name,
                            ignore=shutil.ignore_patterns("__pycache__"))
        self.records = self.root / "terms/OT1991/records"
        self.records.mkdir(parents=True)
        self.source = self.records / "one.md"
        self.source.write_text("Reviewed source one.\n", encoding="utf-8")
        self.pointer = self.base / "CURRENT.json"
        self.collect_calls = 0
        self.addCleanup(patch.stopall)
        patch.object(library, "collect", side_effect=self.collect).start()
        patch.object(library, "render", side_effect=self.render).start()

    def collect(self, root, terms, *args, **kwargs):
        self.collect_calls += 1
        root = Path(root)
        paths = sorted((root / "terms/OT1991/records").glob("*.md"))
        source_data = {path.relative_to(root).as_posix(): path.read_bytes() for path in paths}
        visible_sources = list(source_data.values())
        record_paths = list(source_data)
        for directory, suffix in (("tools", ".py"), ("schemas", ".json"), ("inputs", ".json")):
            for path in sorted((root / "development/case-library" / directory).glob("*" + suffix)):
                source_data[path.relative_to(root).as_posix()] = path.read_bytes()
        return {
            "schema_version": 2,
            "development_only": True,
            "production_integration": False,
            "scope": {"terms": list(terms), "source_revision": "a" * 40},
            "terms": [],
            "records": [],
            "citation_index": {},
            "inventory": [],
            "carryovers": [],
            "warnings": [raw.decode("utf-8").strip() for raw in visible_sources],
            "sources": {path: {"sha256": digest(raw), "size": len(raw)}
                        for path, raw in source_data.items()},
            "directory_memberships": {"terms/OT1991/records": record_paths},
        }

    @staticmethod
    def render(catalogue, *args, **kwargs):
        return "<!doctype html><html><body><pre>" + escape(encoded(catalogue).decode()) + "</pre></body></html>\n"

    def build(self, **kwargs):
        return library.build(self.root, terms=("OT1991",), **kwargs)

    def load(self, **kwargs):
        return library.load_current(self.root, **kwargs)

    def bytes_under(self, folder):
        return {path.relative_to(folder).as_posix(): path.read_bytes()
                for path in sorted(folder.rglob("*")) if path.is_file()}

    def rehash(self, folder):
        manifest_path = folder / "manifest.json"
        manifest = json.loads(manifest_path.read_bytes())
        for name in manifest["files"]:
            manifest["files"][name] = digest((folder / name).read_bytes())
        manifest["content_id"] = digest((folder / "catalogue.json").read_bytes() + b"\0"
                                        + (folder / "index.html").read_bytes())
        manifest_path.write_bytes(encoded(manifest))
        pointer = json.loads(self.pointer.read_bytes())
        pointer["manifest_sha256"] = digest(manifest_path.read_bytes())
        self.pointer.write_bytes(encoded(pointer))

    def assert_refused(self, *, fresh=True):
        pointer = self.pointer.read_bytes()
        snapshots = self.bytes_under(self.base / "builds")
        with self.assertRaises(library.LibraryError):
            self.load(require_fresh=fresh)
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(self.bytes_under(self.base / "builds"), snapshots)

    def test_unchanged_build_reuses_identical_snapshot_and_preserves_sources(self):
        source_bytes = self.source.read_bytes()
        folder, data, changed = self.build()
        self.assertTrue(changed)
        original = self.bytes_under(folder)
        pointer = self.pointer.read_bytes()
        second, data_again, changed_again = self.build()
        self.assertEqual(second, folder)
        self.assertEqual(data_again, data)
        self.assertFalse(changed_again)
        self.assertEqual(self.bytes_under(folder), original)
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(self.source.read_bytes(), source_bytes)
        self.assertEqual(self.load(), (folder, data))

    def test_source_update_creates_snapshot_and_retains_previous_build(self):
        old, original, _ = self.build()
        previous = self.bytes_under(old)
        self.source.write_text("Reviewed source two.\n", encoding="utf-8")
        new, current, changed = self.build()
        self.assertTrue(changed)
        self.assertNotEqual(new, old)
        self.assertNotEqual(current, original)
        self.assertEqual(self.bytes_under(old), previous)
        self.assertEqual(self.load(), (new, current))

    def test_same_size_source_change_with_restored_timestamp_is_stale(self):
        self.build()
        stat = self.source.stat()
        self.source.write_text("Reviewed source two.\n", encoding="utf-8")
        os.utime(self.source, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        self.assert_refused()
        self.load(require_fresh=False)

    def test_new_record_membership_invalidates_live_snapshot(self):
        self.build()
        (self.records / "two.md").write_text("New member.\n", encoding="utf-8")
        self.assert_refused()

    def test_removed_record_membership_invalidates_live_snapshot(self):
        self.build()
        self.source.unlink()
        self.assert_refused()

    def test_tool_bytes_invalidate_live_snapshot(self):
        self.build()
        tool = self.base / "tools/library.py"
        tool.write_bytes(tool.read_bytes() + b"\n# Fixture change.\n")
        self.assert_refused()

    def test_schema_bytes_invalidate_live_snapshot(self):
        self.build()
        schema = next((self.base / "schemas").glob("*.json"))
        schema.write_bytes(schema.read_bytes() + b"\n")
        self.assert_refused()

    def test_corrupt_pointer_blocks_build_until_explicit_recovery(self):
        folder, _, _ = self.build()
        snapshot = self.bytes_under(folder)
        corrupt = b'{"schema_version":2,"build_id":"truncated"'
        self.pointer.write_bytes(corrupt)
        with self.assertRaises(library.LibraryError):
            self.build()
        self.assertEqual(self.pointer.read_bytes(), corrupt)
        self.assertEqual(self.bytes_under(folder), snapshot)
        self.build(recover=True)
        self.load()
        self.assertEqual(self.bytes_under(folder), snapshot)
        self.assertTrue(any(path.read_bytes() == corrupt
                            for path in (self.base / "recovery").rglob("*") if path.is_file()))

    def test_corrupt_snapshot_recovery_preserves_exact_damaged_bytes(self):
        folder, _, _ = self.build()
        html = folder / "index.html"
        html.write_bytes(html.read_bytes() + b"damaged")
        damaged = self.bytes_under(folder)
        pointer = self.pointer.read_bytes()
        with self.assertRaises(library.LibraryError):
            self.build()
        self.assertEqual(self.pointer.read_bytes(), pointer)
        replacement, _, changed = self.build(recover=True)
        self.assertTrue(changed)
        self.assertNotEqual(replacement, folder)
        self.assertEqual(self.bytes_under(folder), damaged)
        self.load()

    def test_duplicate_pointer_keys_are_rejected(self):
        self.build()
        original = self.pointer.read_bytes()
        self.pointer.write_bytes(original.rstrip()[:-1] + b',"schema_version":2}\n')
        self.assert_refused()

    def test_nonfinite_pointer_number_is_rejected(self):
        self.build()
        pointer = json.loads(self.pointer.read_bytes())
        pointer["schema_version"] = float("nan")
        self.pointer.write_bytes(encoded(pointer))
        self.assert_refused()

    def test_boolean_and_float_schema_versions_are_rejected(self):
        self.build()
        original = json.loads(self.pointer.read_bytes())
        for version in (True, 2.0):
            with self.subTest(version=version):
                pointer = dict(original, schema_version=version)
                self.pointer.write_bytes(encoded(pointer))
                self.assert_refused()

    def test_pointer_build_id_cannot_escape_builds_directory(self):
        self.build()
        original = json.loads(self.pointer.read_bytes())
        for identifier in ("../outside", "/tmp/outside", "a" * 63, "G" * 64, "a" * 64 + "/child"):
            with self.subTest(identifier=identifier):
                self.pointer.write_bytes(encoded(dict(original, build_id=identifier)))
                self.assert_refused()

    def test_manifest_may_not_add_path_traversal_member(self):
        folder, _, _ = self.build()
        manifest_path = folder / "manifest.json"
        manifest = json.loads(manifest_path.read_bytes())
        manifest["files"]["../../outside"] = "a" * 64
        manifest_path.write_bytes(encoded(manifest))
        pointer = json.loads(self.pointer.read_bytes())
        pointer["manifest_sha256"] = digest(manifest_path.read_bytes())
        self.pointer.write_bytes(encoded(pointer))
        self.assert_refused(fresh=False)

    def test_missing_manifest_member_is_rejected(self):
        folder, _, _ = self.build()
        (folder / "index.html").unlink()
        self.assert_refused(fresh=False)

    def test_rehashed_unreviewed_catalogue_is_not_live_authority(self):
        folder, _, _ = self.build()
        path = folder / "catalogue.json"
        data = json.loads(path.read_bytes())
        data["warnings"].append("Unreviewed generated claim.")
        path.write_bytes(encoded(data))
        (folder / "index.html").write_text(self.render(data), encoding="utf-8")
        self.rehash(folder)
        self.assert_refused()

    def test_rehashed_generated_html_must_match_current_renderer(self):
        folder, _, _ = self.build()
        html = folder / "index.html"
        html.write_bytes(html.read_bytes() + b"\nUnreviewed display edit.\n")
        self.rehash(folder)
        self.assert_refused()

    def test_rehashed_source_fresh_impostor_current_requires_explicit_recovery(self):
        original, reviewed, _ = self.build()
        original_bytes = self.bytes_under(original)
        impostor = original.parent / ("f" * 64)
        shutil.copytree(original, impostor)
        path = impostor / "catalogue.json"
        data = json.loads(path.read_bytes())
        data["warnings"].append("Unreviewed generated claim.")
        path.write_bytes(encoded(data))
        (impostor / "index.html").write_text(self.render(data), encoding="utf-8")
        manifest_path = impostor / "manifest.json"
        manifest = json.loads(manifest_path.read_bytes())
        manifest["build_id"] = impostor.name
        manifest_path.write_bytes(encoded(manifest))
        pointer = json.loads(self.pointer.read_bytes())
        pointer["build_id"] = impostor.name
        self.pointer.write_bytes(encoded(pointer))
        self.rehash(impostor)
        damaged = self.bytes_under(impostor)
        pointer_bytes = self.pointer.read_bytes()
        self.assert_refused()
        with self.assertRaises(library.LibraryError):
            self.build()
        self.assertEqual(self.pointer.read_bytes(), pointer_bytes)
        self.assertEqual(self.bytes_under(impostor), damaged)
        recovered, data, changed = self.build(recover=True)
        self.assertTrue(changed)
        self.assertEqual(recovered, original)
        self.assertEqual(data, reviewed)
        self.assertEqual(self.bytes_under(original), original_bytes)
        self.assertEqual(self.bytes_under(impostor), damaged)
        self.assertTrue(any(path.read_bytes() == pointer_bytes
                            for path in (self.base / "recovery").rglob("*") if path.is_file()))
        self.load()

    def test_symlink_snapshot_member_is_rejected_even_when_bytes_match(self):
        folder, _, _ = self.build()
        member = folder / "index.html"
        outside = self.root.parent / "outside.html"
        outside.write_bytes(member.read_bytes())
        member.unlink()
        member.symlink_to(outside)
        self.assert_refused(fresh=False)

    def test_symlink_source_is_rejected_even_when_bytes_match(self):
        self.build()
        outside = self.root.parent / "outside.md"
        outside.write_bytes(self.source.read_bytes())
        self.source.unlink()
        self.source.symlink_to(outside)
        self.assert_refused()
        with self.assertRaises(library.LibraryError):
            self.build()

    def test_symlink_current_pointer_is_rejected(self):
        self.build()
        outside = self.root.parent / "outside-pointer.json"
        outside.write_bytes(self.pointer.read_bytes())
        self.pointer.unlink()
        self.pointer.symlink_to(outside)
        with self.assertRaises(library.LibraryError):
            self.load()
        with self.assertRaises(library.LibraryError):
            self.build()
        self.assertTrue(self.pointer.is_symlink())

    def test_publication_failure_preserves_prior_pointer_and_source(self):
        old, data, _ = self.build()
        pointer = self.pointer.read_bytes()
        snapshot = self.bytes_under(old)
        self.source.write_text("Reviewed source two.\n", encoding="utf-8")
        replace = os.replace

        def fail_pointer(source, destination, *args, **kwargs):
            if Path(destination) == self.pointer:
                raise OSError("Injected publication failure")
            return replace(source, destination, *args, **kwargs)

        with patch.object(library.os, "replace", side_effect=fail_pointer):
            with self.assertRaises((library.LibraryError, OSError)):
                self.build()
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(self.bytes_under(old), snapshot)
        self.assertEqual(self.source.read_text(), "Reviewed source two.\n")
        self.assertEqual(self.load(require_fresh=False), (old, data))

    def test_interrupted_first_publication_has_no_current_and_retry_checks_orphan(self):
        replace = os.replace

        def fail_pointer(source, destination, *args, **kwargs):
            if Path(destination) == self.pointer:
                raise OSError("Injected first-publication failure")
            return replace(source, destination, *args, **kwargs)

        with patch.object(library.os, "replace", side_effect=fail_pointer):
            with self.assertRaises((library.LibraryError, OSError)):
                self.build()
        self.assertFalse(self.pointer.exists())
        orphans = list((self.base / "builds").iterdir())
        self.assertEqual(len(orphans), 1)
        original = self.bytes_under(orphans[0])
        folder, data, changed = self.build()
        self.assertTrue(changed)
        self.assertEqual(folder, orphans[0])
        self.assertEqual(self.bytes_under(folder), original)
        self.assertEqual(self.load(), (folder, data))

    def test_interrupted_first_publication_does_not_adopt_corrupt_orphan(self):
        replace = os.replace

        def fail_pointer(source, destination, *args, **kwargs):
            if Path(destination) == self.pointer:
                raise OSError("Injected first-publication failure")
            return replace(source, destination, *args, **kwargs)

        with patch.object(library.os, "replace", side_effect=fail_pointer):
            with self.assertRaises((library.LibraryError, OSError)):
                self.build()
        orphan, = (self.base / "builds").iterdir()
        (orphan / "index.html").write_bytes(b"damaged retained orphan")
        damaged = self.bytes_under(orphan)
        with self.assertRaises(library.LibraryError):
            self.build()
        self.assertFalse(self.pointer.exists())
        self.assertEqual(self.bytes_under(orphan), damaged)
        replacement, _, changed = self.build(recover=True)
        self.assertTrue(changed)
        self.assertNotEqual(replacement, orphan)
        self.assertEqual(self.bytes_under(orphan), damaged)
        self.load()

    def test_source_edit_at_publication_rolls_back_pointer_without_losing_edit(self):
        old, data, _ = self.build()
        pointer = self.pointer.read_bytes()
        self.source.write_text("Reviewed source two.\n", encoding="utf-8")
        replace = os.replace
        injected = False

        def change_source(source, destination, *args, **kwargs):
            nonlocal injected
            if Path(destination) == self.pointer and not injected:
                injected = True
                self.source.write_text("Concurrent reviewed edit.\n", encoding="utf-8")
            return replace(source, destination, *args, **kwargs)

        with patch.object(library.os, "replace", side_effect=change_source):
            with self.assertRaises(library.LibraryError):
                self.build()
        self.assertTrue(injected)
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(self.source.read_text(), "Concurrent reviewed edit.\n")
        self.assertEqual(self.load(require_fresh=False), (old, data))

    def test_membership_change_at_publication_rolls_back_pointer(self):
        old, data, _ = self.build()
        pointer = self.pointer.read_bytes()
        self.source.write_text("Reviewed source two.\n", encoding="utf-8")
        added = self.records / "two.md"
        replace = os.replace
        injected = False

        def add_source(source, destination, *args, **kwargs):
            nonlocal injected
            if Path(destination) == self.pointer and not injected:
                injected = True
                added.write_text("Concurrent added record.\n", encoding="utf-8")
            return replace(source, destination, *args, **kwargs)

        with patch.object(library.os, "replace", side_effect=add_source):
            with self.assertRaises(library.LibraryError):
                self.build()
        self.assertTrue(injected)
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(added.read_text(), "Concurrent added record.\n")
        self.assertEqual(self.load(require_fresh=False), (old, data))

    def test_source_change_during_live_recompute_is_detected(self):
        self.build()
        pointer = self.pointer.read_bytes()

        def change_after_collection(root, terms, *args, **kwargs):
            data = self.collect(root, terms, *args, **kwargs)
            self.source.write_text("Concurrent live-read edit.\n", encoding="utf-8")
            return data

        with patch.object(library, "collect", side_effect=change_after_collection):
            with self.assertRaises(library.LibraryError):
                self.load()
        self.assertEqual(self.pointer.read_bytes(), pointer)
        self.assertEqual(self.source.read_text(), "Concurrent live-read edit.\n")

    def test_simultaneous_first_builds_publish_one_snapshot_and_retry_cleanly(self):
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        results = context.Queue()

        def worker():
            try:
                if not ready.wait(timeout=10):
                    raise RuntimeError("Writer start signal timed out")
                folder, _, changed = self.build()
                results.put(("ok", folder.name, changed))
            except Exception as error:
                results.put(("error", type(error).__name__, str(error)))

        processes = [context.Process(target=worker) for _ in range(3)]
        try:
            for process in processes:
                process.start()
            ready.set()
            output = [results.get(timeout=30) for _ in processes]
            for process in processes:
                process.join(timeout=10)
                self.assertFalse(process.is_alive(), "Writer must not deadlock")
                self.assertEqual(process.exitcode, 0)
            successful = [row for row in output if row[0] == "ok"]
            self.assertTrue(successful, output)
            for row in output:
                if row[0] == "error":
                    self.assertEqual(row[1], "LibraryError", output)
                    self.assertIn("writer is active", row[2], output)
            self.assertEqual(len({row[1] for row in successful}), 1)
            self.assertEqual(sum(row[2] for row in successful), 1)
            folder, _ = self.load()
            self.assertEqual(folder.name, successful[0][1])
            self.assertEqual(len(list((self.base / "builds").iterdir())), 1)
            retry, _, changed = self.build()
            self.assertEqual(retry, folder)
            self.assertFalse(changed)
        finally:
            for process in processes:
                if process.is_alive():
                    process.terminate()
                process.join(timeout=5)
            results.close()
            results.join_thread()

    def test_killed_writer_releases_process_lock_without_stale_lock_cleanup(self):
        context = multiprocessing.get_context("fork")
        ready = context.Event()

        def hold_writer():
            with library._writer(self.root):
                ready.set()
                signal.pause()

        process = context.Process(target=hold_writer)
        try:
            process.start()
            self.assertTrue(ready.wait(timeout=10))
            with self.assertRaisesRegex(library.LibraryError, "writer is active"):
                self.build()
            self.assertFalse(self.pointer.exists())
            process.terminate()
            process.join(timeout=10)
            self.assertFalse(process.is_alive())
            folder, data, changed = self.build()
            self.assertTrue(changed)
            self.assertEqual(self.load(), (folder, data))
        finally:
            if process.is_alive():
                process.terminate()
            process.join(timeout=5)


class StrictJsonTests(unittest.TestCase):
    def test_nested_duplicate_keys_and_nonfinite_numbers_are_rejected(self):
        inputs = (
            '{"nested":{"same":1,"same":2}}',
            '{"nested":[{"same":1,"same":2}]}',
            '{"number":NaN}',
            '{"number":Infinity}',
            '{"number":-Infinity}',
            '{"number":1e999}',
            '{"number":-1e999}',
        )
        with tempfile.TemporaryDirectory(prefix="library-json-") as directory:
            path = Path(directory) / "input.json"
            for raw in inputs:
                with self.subTest(raw=raw):
                    path.write_text(raw, encoding="utf-8")
                    with self.assertRaises(library.LibraryError):
                        library.read_json(path)

    def test_finite_numbers_unicode_and_null_remain_supported(self):
        with tempfile.TemporaryDirectory(prefix="library-json-") as directory:
            path = Path(directory) / "input.json"
            expected = {"number": 1.5, "zero": 0, "label": "München", "unknown": None}
            path.write_bytes(encoded(expected))
            self.assertEqual(library.read_json(path), expected)


if __name__ == "__main__":
    unittest.main()
