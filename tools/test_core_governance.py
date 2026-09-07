"""In-memory filesystem overlay negative tests; no runtime or real repo writes."""
import importlib.util,json,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('validator',Path(__file__).with_name('validate-core-governance.py'));v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
class Overlay:
 def __init__(self,changes,path=v.ROOT):self.changes=changes;self.path=path
 def __truediv__(self,p):return Overlay(self.changes,self.path/p)
 @property
 def parent(self):return Overlay(self.changes,self.path.parent)
 def joinpath(self,p):return self/p
 def exists(self):return self.path.exists()
 def is_file(self):return self.path.is_file()
 def read_text(self,encoding):return self.changes.get(str(self.path.relative_to(v.ROOT)),self.path.read_text(encoding=encoding))
class NegativeTests(unittest.TestCase):
 def mutate(self,file,change):
  data=json.loads((v.ROOT/file).read_text(encoding='utf-8-sig'));change(data)
  self.assertTrue(v.validate(Overlay({file:json.dumps(data)})))
 def test_baseline(self):self.assertEqual(v.validate(),[])
 def test_old_url_trigger(self):self.mutate('aeris.autopilot.json',lambda a:a['trigger'].update(interpretation='AERIS_FULL_BUILD_AUTOPILOT_REQUEST'))
 def test_arbitrary_workspace(self):self.mutate('aeris.autopilot.json',lambda a:a['trigger'].update(active_workspace_counts_as_target_path=True))
 def test_admission_bypass(self):self.mutate('aeris.autopilot.json',lambda a:a['admission_precondition'].update(evaluate_before_trigger=False))
 def test_false_complete(self):self.mutate('aeris.traceability.json',lambda t:t['workstreams']['A'].update(status='COMPLETE'))
 def test_false_requirement_done(self):self.mutate('aeris.traceability.json',lambda t:t['requirements'][0].update(status='DONE'))
 def test_missing_service(self):self.mutate('aeris.traceability.json',lambda t:t['four_way_version_tuple'].update(required_records=['core_blueprint','implementation','local_checkout','evidence_bundle']))
 def test_incomplete_evidence(self):self.mutate('aeris.review.json',lambda r:r['evidence_contract'].update(required_fields=['artifact']))
 def test_runtime_claim(self):self.mutate('aeris.autopilot.json',lambda a:a['admission_precondition'].update(runtime_enforcement_implemented=True))
if __name__=='__main__':unittest.main()
