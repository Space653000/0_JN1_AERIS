# AERIS FULL BUILD Autopilot SOP

## Human normal input

When Codex already has exactly one safe selected/active writable workspace, the Human only needs to paste:

```text
https://github.com/Space653000/0_JN1_AERIS
https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation
```

Those two URLs are the command. They mean: **start AERIS FULL BUILD AUTOPILOT immediately.**

Do not ask the Human to paste another prompt. Do not ask `確認執行`. If the Human also gives a path, use it. Ask for a path only when no safe target exists or multiple targets are genuinely ambiguous.

## Required automatic flow

```text
read canonical Core authority
→ sync latest CI-passed Implementation main
→ inventory all gaps against Core + maturity + Definition of Company Done
→ automatically implement every safe software-only gap
→ add/update deterministic tests
→ repeat until no safe software-only gap remains
→ inventory real machine
→ install/configure supported dependencies
→ local model + Knowledge
→ Local/Offline acceptance
→ Company Opening
→ Dashboard/frontend/backend at 127.0.0.1:8765
→ OS-native persistence
→ watchdog/self-recovery
→ Evidence/Audit handoff
```

## Software Gap Closure Loop

`NOT_IMPLEMENTED` is not an acceptable stopping point when the missing item is ordinary software work that Codex can safely implement.

Codex must inspect at least:

- Implementation `config/maturity.json`;
- `docs/DEFINITION_OF_COMPANY_DONE.md`;
- Core architecture requirements;
- API/UI/workflow coverage;
- Skills/Methods/Standards registries;
- task/evidence/verification/reproduction/health coverage;
- automated tests.

For each gap:

```text
classify
├─ software-only + safe → implement automatically → test → continue
└─ true Human/external dependency → preserve evidence → Human Gate
```

The Human's two-URL trigger is standing authorization for reversible R0/R1 software work and controlled R2 work whose safety preconditions are satisfied. Large-task plan confirmation is not required.

## Token-efficiency rule

Do not use the Human's local Codex Token to rediscover defects that GitHub CI can catch first. Prefer the latest Windows+Ubuntu CI-passed Implementation main and cloud/GitHub validation. Use the local machine for machine-specific installation, runtime/inference, persistence/reboot evidence and genuinely local-only defects.

Do not launch Claude Code or another model reviewer by default.

Do not use Codex Tasks/scheduling for company continuity.

## Continuous operation

AERIS must continue after Codex exits:

- Windows: AERIS OS-native Scheduled Task/restart policy, with Startup fallback when necessary;
- Linux/Jetson: systemd user service with `Restart=always`, with documented fallback;
- watchdog/self-recovery restores the local Supervisor without bypassing Core/privacy/Human gates.

## Genuine Human Gates only

Stop only for the minimum exact action when blocked by:

- no safe/unambiguous target path;
- OS/admin/persistence policy denial;
- License/EULA acceptance;
- secret/credential/hardware token;
- physical cable/fixture/chamber/instrument/calibration;
- destructive unrelated disk/network/firewall impact;
- canonical Core policy change;
- one-time reboot/logoff needed to prove persistence;
- R3/R4 customer/production/formal/external release.

After the Human performs that one action, resume automatically from preserved state.

## Truth boundary

FULL BUILD means Codex must close every safely implementable software-only gap it can reach. It does not authorize fabricated success for capabilities that truly require unavailable licenses, hardware, calibration, credentials or Human authority.

These claims remain forbidden without matching evidence:

```text
all licensed tools available
all hardware verified
hard offline proven when not tested
production/customer release approved
```

## Completion condition

The normal run ends only when one of these is true:

1. all safely implementable software-only gaps for the requested AERIS full-build scope are closed and the supported local company is running with Dashboard/frontend/backend, persistence, watchdog and Evidence; or
2. the next unresolved gap is a genuine Human/external gate, in which case Codex asks for only that one action.

**The Human should not have to remember the orchestration prompt. The two canonical GitHub URLs are the orchestration prompt.**
