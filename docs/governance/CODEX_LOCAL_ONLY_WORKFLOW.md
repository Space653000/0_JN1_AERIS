# Core 讀取與治理發布邊界

現行依 [constitution](../../constitution.md) 與 [Astra Gate v3](ASTRA_EXECUTION_GATE_V3.md)。
正常部署使用唯讀 Core cache：canonical fetch、disabled push URL、deny pre-push、detached clean checkout、HEAD 等於記錄 SHA；air-gap snapshot 須驗證 checksum 與真實來源。
使用者明確授權治理時，以獨立有界 worktree 產生 Diff、測試、隔離 review 與候選 PR；可使用既有授權連線發布，但不得輸出 credentials、改 Ruleset/settings 或 force push。此例外不授權 runtime 直接更改 Core。
本機唯一寫入根目錄 `C:\0_JN1_AERIS`；其他路徑不動。同步僅 fetch 與狀態比較；保護 dirty worktree，經授權驗證才整併。既有 tools/local-only 是歷史遷移債務，不能以舊參數選任意正式路徑。
