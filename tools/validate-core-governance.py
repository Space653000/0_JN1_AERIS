#!/usr/bin/env python3
"""Read-only governance contract validation. PASS is not product acceptance."""
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ACTIVE=['AGENTS.md','CLAUDE.md','README.md','constitution.md','aeris.policy.yaml','docs/AERIS_BLUEPRINT_ZH_TW.md','docs/governance/AI_READ_ORDER.md','docs/governance/AI_AUTOPILOT_SOP.md','docs/governance/ASTRA_EXECUTION_GATE_V3.md','docs/governance/CODEX_LOCAL_ONLY_WORKFLOW.md','docs/governance/GITHUB_ACCESS_BOUNDARY.md','docs/governance/AERIS_TRACEABILITY_MATRIX.md']
REQUIRED_IDS={'AERIS-AD-UI-001', 'AERIS-AD-D-001', 'AERIS-AD-SYNC-001', 'AERIS-AD-A-002', 'AERIS-AD-VERSIONS-001', 'AERIS-AD-SYNC-002', 'AERIS-AD-B-001', 'AERIS-AD-A-001', 'AERIS-AD-PROGRESS-001', 'AERIS-AD-ROOT-001', 'AERIS-AD-D-002', 'AERIS-AD-C-001', 'AERIS-AD-B-002', 'AERIS-AD-A-003', 'AERIS-AD-E-001', 'AERIS-AD-C-002'}
RETAINED={'schema_version': 1, 'source_commit': '6a4236c', 'appendix': 'docs/governance/RETAINED_STRICT_RULES.md', 'superseded': {'url_trigger': 'GATE-08', 'workspace': 'GATE-03', 'model_routing': 'GATE-07', 'core_publication': 'GATE-01', 'E_scope': 'ADR-AD-008', 'completion': 'GATE-04', 'public_root': 'GATE-03', 'version_tuple': 'GATE-06'}, 'required_core_guards': ['canonical_fetch_url', 'disabled_push_url', 'deny_pre_push_hook', 'detached_checkout', 'clean_worktree', 'head_equals_recorded_core_sha'], 'never_bypass': ['privacy', 'checksum_or_signature_failure', 'core_drift', 'unsupported_machine', 'failed_verification', 'proprietary_license', 'hardware_calibration', 'irreversible_release_approval'], 'publication_scope': 'normal_deployment_forbidden_explicit_bounded_governance_PR_exception', 'legacy_executables': ['aeris-data.js', 'aeris-theme.js', 'tools/local-only/New-AERISLocalWorkspace.ps1', 'tools/local-only/Protect-AERISReadOnly.ps1', 'tools/local-only/Sync-AERISTarget.ps1', 'tools/local-only/Verify-AERISReadOnly.ps1'], 'governance_executables': ['tools/validate-core-governance.py', 'tools/test_core_governance.py'], 'required_delivery_fields': ['target_sha', 'implementation_sha', 'local_workspace', 'tests', 'core_integrity', 'local_inference', 'offline_state', 'company_opening_state', 'dashboard_frontend_backend_state', 'persistence_watchdog_state', 'evidence_paths', 'unresolved_software_gaps', 'remaining_external_blockers', 'remote_write_performed_no'], 'forbidden_remote_operations': ['push', 'force_push', 'create_remote_branch', 'update_remote_branch', 'delete_remote_branch', 'create_remote_tag', 'update_remote_tag', 'delete_remote_tag', 'create_pull_request', 'update_pull_request', 'merge_pull_request', 'repository_file_write', 'update_ref', 'release_publish', 'repository_settings_change', 'pages_settings_change', 'branch_protection_change', 'ruleset_change', 'auto_accept_core_drift']}
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
 retained=obj('aeris.retained-rules.json')
 need(retained==RETAINED,'retained strict rules/supersession mapping drift')
 appendix=read(RETAINED['appendix'])
 for token in RETAINED['required_core_guards']+RETAINED['never_bypass']+RETAINED['required_delivery_fields']+RETAINED['forbidden_remote_operations']:
  need(token in appendix,'retained appendix missing '+token)
 for doc in ['AGENTS.md','constitution.md','docs/governance/AI_READ_ORDER.md']:
  need('RETAINED_STRICT_RULES.md' in read(doc),'mandatory retained-rule link absent '+doc)
 allowed=set(RETAINED['legacy_executables']+RETAINED['governance_executables'])
 for file in root.rglob('*'):
  if file.is_file() and file.suffix.lower() in {'.py','.ps1','.js','.sh','.bat','.cmd','.exe','.dll'}:
   rel=file.relative_to(ROOT).as_posix()
   need(rel in allowed,'Core executable outside narrow allowlist: '+rel)
 need(a.get('canonical_core',{}).get('branch')=='main','Core branch drift')
 need(a.get('canonical_core',{}).get('authority')=='read_only_design_ssot','Core authority drift')
 need(a.get('human_ai_roles',{}).get('human_chief_engineer')=='final_authority_and_irreversible_release_approval','Human role drift')
 need(v.get('human_authority',{}).get('final_authority') is True,'Human final authority missing')
 need(v.get('human_authority',{}).get('reviewer_pass_is_release_authority') is False,'review cannot release')
 for flag in ['launch_claude_code','launch_second_model_reviewer','use_codex_tasks_or_scheduler']:
  need(a.get('default_execution_policy',{}).get(flag) is False,'unsafe execution policy '+flag)
 for action in ['checkout','merge','push']:
  need(v.get('automatic_git_actions',{}).get(action) is False,'automatic Git '+action)
 need(v.get('review_routing',{}).get('same_context_repair_approval') is False,'self approval')
 need(v.get('review_routing',{}).get('independent_verification')=='isolated_reviewer_or_independent_rerun','independent verification missing')
 need('independent_verification' in v.get('admission',{}).get('required_before_human_decision',[]),'review admission bypass')

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
 need(bool(ids) and REQUIRED_IDS.issubset(set(ids)),'required requirement IDs missing')
 need(len(ids)==len(set(ids)) and None not in ids,'duplicate/empty requirements')
 matrix=read('docs/governance/AERIS_TRACEABILITY_MATRIX.md')
 rows=[line for line in matrix.splitlines() if line.startswith('| AERIS-')]
 expected_rows=[f"| {q['id']} | {q['workstream']} | {q['requirement']} | {q['status']} |" for q in req]
 need(sorted(rows)==sorted(expected_rows),'matrix and JSON rows differ')
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
