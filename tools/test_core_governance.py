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
 def rglob(self,p):return self.path.rglob(p)
 def exists(self):return self.path.exists()
 def is_file(self):return self.path.is_file()
 def read_text(self,encoding):return self.changes.get(self.path.relative_to(v.ROOT).as_posix(),self.path.read_text(encoding=encoding))
class NegativeTests(unittest.TestCase):
 def mutate(self,file,change):
  data=json.loads((v.ROOT/file).read_text(encoding='utf-8-sig'));change(data)
  self.assertTrue(v.validate(Overlay({file:json.dumps(data)})))
 def test_baseline(self):self.assertEqual(v.validate(),[])
 def test_handoff_cannot_be_cached_latest(self):self.mutate('aeris.handoff.json',lambda h:h.update(live_refresh_required=False))
 def test_handoff_cannot_claim_alignment(self):self.mutate('aeris.handoff.json',lambda h:h.update(alignment='PASS'))
 def test_handoff_cannot_authorize_runtime(self):self.mutate('aeris.handoff.json',lambda h:h.update(runtime_authorized_by_this_manifest=True))
 def test_historical_review_needs_evidence(self):self.mutate('aeris.review.json',lambda r:r['completed_reviews'][0].update(evidence={}))
 def test_historical_review_cannot_verify_runtime(self):self.mutate('aeris.review.json',lambda r:r['completed_reviews'][0].update(claim_boundary='RUNTIME'))
 def test_historical_review_needs_pin(self):self.mutate('aeris.review.json',lambda r:r['completed_reviews'][0].update(reviewed_commit=None))
 def test_old_url_trigger(self):self.mutate('aeris.autopilot.json',lambda a:a['trigger'].update(interpretation='AERIS_FULL_BUILD_AUTOPILOT_REQUEST'))
 def test_arbitrary_workspace(self):self.mutate('aeris.autopilot.json',lambda a:a['trigger'].update(active_workspace_counts_as_target_path=True))
 def test_admission_bypass(self):self.mutate('aeris.autopilot.json',lambda a:a['admission_precondition'].update(evaluate_before_trigger=False))
 def test_false_complete(self):self.mutate('aeris.traceability.json',lambda t:t['workstreams']['A'].update(status='COMPLETE'))
 def test_false_requirement_done(self):self.mutate('aeris.traceability.json',lambda t:t['requirements'][0].update(status='DONE'))
 def test_missing_service(self):self.mutate('aeris.traceability.json',lambda t:t['four_way_version_tuple'].update(required_records=['core_blueprint','implementation','local_checkout','evidence_bundle']))
 def test_incomplete_evidence(self):self.mutate('aeris.review.json',lambda r:r['evidence_contract'].update(required_fields=['artifact']))
 def test_runtime_claim(self):self.mutate('aeris.autopilot.json',lambda a:a['admission_precondition'].update(runtime_enforcement_implemented=True))
 def test_skill_example_requirement_cannot_disappear(self):self.mutate('aeris.traceability.json',lambda t:t.update(requirements=[q for q in t['requirements'] if q['id']!='AERIS-EX-01']))
 def test_empty_requirements(self):self.mutate('aeris.traceability.json',lambda t:t.update(requirements=[]))
 def test_human_authority(self):self.mutate('aeris.review.json',lambda r:r['human_authority'].update(final_authority=False))
 def test_core_branch(self):self.mutate('aeris.autopilot.json',lambda a:a['canonical_core'].update(branch='other'))
 def test_core_authority(self):self.mutate('aeris.autopilot.json',lambda a:a['canonical_core'].update(authority='writable'))
 def test_scheduler(self):self.mutate('aeris.autopilot.json',lambda a:a['default_execution_policy'].update(use_codex_tasks_or_scheduler=True))
 def test_claude(self):self.mutate('aeris.autopilot.json',lambda a:a['default_execution_policy'].update(launch_claude_code=True))
 def test_auto_push(self):self.mutate('aeris.review.json',lambda r:r['automatic_git_actions'].update(push=True))
 def test_self_approve(self):self.mutate('aeris.review.json',lambda r:r['review_routing'].update(same_context_repair_approval=True))
 def test_no_independent(self):self.mutate('aeris.review.json',lambda r:r['review_routing'].update(independent_verification='none'))
 def test_retained_weakened(self):self.mutate('aeris.retained-rules.json',lambda r:r.update(never_bypass=[]))
 def test_supersession_drift(self):self.mutate('aeris.retained-rules.json',lambda r:r['superseded'].update(url_trigger='none'))
 def test_missing_appendix(self):self.assertTrue(v.validate(Overlay({'docs/governance/RETAINED_STRICT_RULES.md':''})))
 def test_matrix_drift(self):self.assertTrue(v.validate(Overlay({'docs/governance/AERIS_TRACEABILITY_MATRIX.md':''})))
 def test_executable_allowlist(self):
  class FakeFile:
   suffix='.py'
   def is_file(self):return True
   def relative_to(self,root):return Path('runtime.py')
  class Extra(Overlay):
   def rglob(self,p):return list(super().rglob(p))+[FakeFile()]
  self.assertTrue(v.validate(Extra({})))
if __name__=='__main__':unittest.main()
