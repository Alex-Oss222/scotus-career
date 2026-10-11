"""Schema and operator-curation contract on disposable source repositories."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

AREA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AREA/'tools'))
import library


class ContractTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='library-contract-')
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.base = self.root/library.BASE
        self.base.mkdir(parents=True)
        for name in ('tools', 'schemas', 'inputs'):
            shutil.copytree(AREA/name, self.base/name, ignore=shutil.ignore_patterns('__pycache__'))
        self.path = 'terms/OT1995/records/example_1995-11-07.md'
        source = self.root/self.path
        source.parent.mkdir(parents=True)
        source.write_text('Example source.\n')
        record = {'record_id':'record-example','term':'OT1995','path':self.path,
                  'sha256':library.digest(source.read_bytes()), 'kind':'court_event',
                  'metadata':{'Case and dockets':'Example; 94-7427'},'title':'Example',
                  'event_date':'1995-11-07','effective_date':None,'chunks':[1],
                  'inventory_refs':[],'references':[],
                  'citations':[{'text':'505 U.S. 833','source_path':self.path,'line':1,'section':'Example'}],
                  'sections':[],'warnings':[]}
        summary = {'term':'OT1995','record_count':1,'court_event_count':1,'admitted_source_count':0,
                   'inventory_count':0,'mapped_inventory_count':0,'chunks':[1]}
        self.data={'terms':[summary],'records':[record],'inventory':[],'carryovers':[],
                   'warnings':[],'sources':{self.path:{'sha256':record['sha256'],'size':source.stat().st_size}}}
        self.patch=patch.object(library,'build_catalogue',side_effect=lambda *_:deepcopy(self.data))
        self.patch.start();self.addCleanup(self.patch.stop)

    def collect(self):
        return library.collect(self.root, ('OT1995',))

    def annotate(self, entries):
        path=self.base/'inputs/annotations.json'
        path.write_bytes(library.json_bytes({'schema_version':2,'entries':entries}))
        return path

    def test_operator_annotations_survive_rebuild_and_are_searchable(self):
        annotation={'aliases':['Alternate name'],'notes':['Source checked locally'],
                    'extensions':{'research':{'owner':'operator','detail':None}}}
        path=self.annotate({'record-example':annotation});original=path.read_bytes()
        first,catalogue,_=library.build(self.root, ('OT1995',))
        self.assertEqual(catalogue['records'][0]['curation'],annotation)
        self.assertEqual(len(library.search(catalogue,'alternate NAME')),1)
        again,_,changed=library.build(self.root, ('OT1995',))
        self.assertFalse(changed);self.assertEqual(first,again)
        self.assertEqual(path.read_bytes(),original)

    def test_unknown_annotation_identity_refuses_build(self):
        self.annotate({'record-missing':{'aliases':[],'notes':[],'extensions':{}}})
        with self.assertRaises(library.LibraryError):self.collect()

    def test_extensions_cannot_replace_core_or_integration_fields(self):
        for value in [{'aliases':[],'notes':[],'extensions':{},'production_integration':True},
                      {'aliases':[],'notes':[],'extensions':{'experiment':True}}]:
            with self.subTest(value=value):
                self.annotate({'record-example':value})
                with self.assertRaises(library.LibraryError):self.collect()

    def test_invalid_calendar_date_and_boolean_chunk_fail(self):
        for key,value in [('event_date','1995-02-30'),('chunks',[True])]:
            original=deepcopy(self.data)
            self.data['records'][0][key]=value
            with self.subTest(key=key),self.assertRaises(library.LibraryError):self.collect()
            self.data=original

    def test_wrong_counts_and_duplicate_record_identity_fail(self):
        for mutate in [lambda d:d['terms'][0].update(record_count=2),
                       lambda d:d['records'].append(deepcopy(d['records'][0]))]:
            original=deepcopy(self.data);mutate(self.data)
            with self.assertRaises(library.LibraryError):self.collect()
            self.data=original

    def test_record_hash_must_match_source_observation(self):
        self.data['records'][0]['sha256']='0'*64
        with self.assertRaises(library.LibraryError):self.collect()

    def test_reference_provenance_requires_fingerprinted_source(self):
        self.data['records'][0]['references']=[{'kind':'external','target':'https://example.org/',
            'source_path':'terms/OT1995/records/not-read.md','line':1,'section':'Sources',
            'review_status':'unverified','material_kind':'unknown'}]
        with self.assertRaises(library.LibraryError):self.collect()

    def test_citation_index_points_to_observed_record_line(self):
        catalogue=self.collect()
        locations=catalogue['citation_index']['505 U.S. 833']
        self.assertEqual(locations,[{'record_id':'record-example',**self.data['records'][0]['citations'][0]}])
        self.assertIsNone(catalogue['records'][0]['effective_date'])

    def test_search_scope_and_parameter_types(self):
        catalogue=self.collect()
        self.assertEqual(len(library.search(catalogue,'94-7427',term='OT1995',chunk=1,kind='court_event')),1)
        self.assertEqual(library.search(catalogue,'94-7427',chunk=10),[])
        for kwargs in [{'term':'OT1996'},{'chunk':True},{'chunk':0},{'kind':'historical'}]:
            with self.subTest(kwargs=kwargs),self.assertRaises(library.LibraryError):library.search(catalogue,'',**kwargs)
        with self.assertRaises(library.LibraryError):library.search(catalogue,'x'*4097)

    def test_core_schema_rejects_unknown_fields_and_activation(self):
        catalogue=self.collect()
        for key,value in [('production_integration',True),('unexpected','typo')]:
            altered=deepcopy(catalogue);altered[key]=value
            with self.subTest(key=key),self.assertRaises(library.LibraryError):library.validate_catalogue(self.root,altered)


if __name__=='__main__':unittest.main()
