#!/usr/bin/env python3
"""Read-only governance contract validation. PASS is not product acceptance."""
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ACTIVE=['AGENTS.md','CLAUDE.md','README.md','constitution.md','aeris.policy.yaml','docs/AERIS_BLUEPRINT_ZH_TW.md','docs/governance/AI_READ_ORDER.md','docs/governance/AI_AUTOPILOT_SOP.md','docs/governance/ASTRA_EXECUTION_GATE_V3.md','docs/governance/CODEX_LOCAL_ONLY_WORKFLOW.md','docs/governance/GITHUB_ACCESS_BOUNDARY.md','docs/governance/AERIS_TRACEABILITY_MATRIX.md']
def validate(root=ROOT):
 errors=[]
 def need(ok,msg):
  if not ok:errors.append(msg)
 def read(p):
  try:return (root/p).read_text(encoding='utf-8-sig')
  except Exception as e:errors.append(f'{p}: {e}');return ''
 def obj(p):
  try:return json.loads(read(p))
  except Exception as e:errors.append(f'{p}: {e}');return {}
 a=obj('aeris.autopilot.json');t=obj('aeris.traceability.json');v=obj('aeris.review.json')
 need(a.get('schema_version')==3,'autopilot schema drift')
 need(a.get('canonical_core',{}).get('repository')=='Space653000/0_JN1_AERIS','wrong Core')
 need(a.get('implementation',{}).get('repository')=='Space653000/0_JN1_AERIS_Local-computer-implementation','wrong Implementation')
 trigger=a.get('trigger',{})
 need(trigger.get('interpretation')=='PROJECT_IDENTIFICATION_ONLY','unsafe URL trigger')
 need(trigger.get('active_workspace_counts_as_target_path') is False,'arbitrary workspace')
 need(trigger.get('target_root')==r'C:\0_JN1_AERIS','wrong root')
 need(trigger.get('requires_scoped_authorization') is True,'missing authorization')
 admission=a.get('admission_precondition',{})
 for key in ['evaluate_before_trigger','requires_scoped_authorization','drift_stops_construction']:need(admission.get(key) is True,'admission missing '+key)
 need(admission.get('runtime_enforcement_implemented') is False,'false runtime claim')
 need(a.get('full_build_phases')==['ADMISSION_DRIFT','PLAN','IMPLEMENT','EXECUTE','EVIDENCE','VERIFY','PASS','NEXT'],'batch ordering drift')
 need(a.get('default_execution_policy',{}).get('continue_until_no_safe_software_gap_remains') is False,'unbounded build')
 need(v.get('state')=='REVIEW_PENDING','unreviewed governance claim')
 need(v.get('review_result',{}).get('status')=='PENDING','review not independently recorded yet')
 need(v.get('review_routing',{}).get('default_model')=='gpt-6-astra','routing drift')
 need(v.get('review_routing',{}).get('reasoning_effort')=='low','effort drift')
 need(v.get('review_routing',{}).get('domain_contract_model_binding') is False,'model domain binding')
 fields=set(v.get('evidence_contract',{}).get('required_fields',[]))
 need({'requirement_id','reproduce_command','expected_result','actual_result','result','artifact','artifact_sha256','versions','timestamp'}<=fields,'incomplete Evidence contract')
 need(set(t.get('four_way_version_tuple',{}).get('required_records',[]))=={'core_blueprint','implementation','local_checkout','running_service'},'four-way tuple missing service')
 need(t.get('four_way_version_tuple',{}).get('current_end_to_end_alignment_claim')=='NOT_CLAIMED','false alignment')
 need(t.get('workstreams',{}).get('E',{}).get('name')=='full_local_acceptance','E meaning drift')
 need(t.get('workstreams',{}).get('E',{}).get('status')=='NOT_STARTED','E started')
 for key in 'ABCD':need(t.get('workstreams',{}).get(key,{}).get('status') in ['REVIEW_PENDING','NOT VERIFIED'],'unsupported workstream completion '+key)
 req=t.get('requirements',[]);ids=[q.get('id') for q in req]
 need(len(ids)==len(set(ids)) and None not in ids,'duplicate/empty requirements')
 for q in req:
  need(q.get('status') in ['REVIEW_PENDING','NOT_STARTED','NOT VERIFIED'],'unsupported requirement completion')
  need(bool(q.get('requirement')) and bool(q.get('acceptance')),'missing requirement/acceptance')
  for e in q.get('evidence',[]):need((root/e.split('#')[0]).is_file(),'missing reference '+e)
 c=read('constitution.md')
 for i in range(1,9):need(f'GATE-{i:02}' in c,'missing gate')
 for token in ['calibration state','noise、distance、azimuth、speaker、language','margin','offline','NO EVIDENCE = NOT DONE']:need(token in c,'weakened engineering rule '+token)
 for p in ACTIVE:
  text=read(p)
  need('C:\\Users\\' not in text,'private user path '+p)
  for forbidden in ['that alone is a complete','active_workspace_counts_as_target_path: true','The two canonical GitHub URLs are the command','Codex may not publish that package','AWAITING_INDEPENDENT_SOL_REVIEW']:
   need(forbidden not in text,'legacy authority '+p+': '+forbidden)
  for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
   if '://' in link or link.startswith('#'):continue
   need((root/p).parent.joinpath(link.split('#')[0]).exists(),'broken link '+p+': '+link)
 return errors
if __name__=='__main__':
 errors=validate()
 print('AERIS_CORE_GOVERNANCE='+('FAIL' if errors else 'PASS'))
 for error in errors:print('- '+error)
 raise SystemExit(bool(errors))
