# AERIS Sol 獨立審查閘門 v2

日期：2026-09-07

適用批次：A–D Core／WHAT

E：`NOT_STARTED`

## 現行路由

1. GPT-5.6 Sol High implementer 依凍結的 A–D requirement IDs 產出候選版本。
2. 另一個隔離 context 的 GPT-5.6 Sol High reviewer 從固定 commit 與需求重新檢查，不繼承 implementer 的推理或自我評價。
3. implementer 處理 findings 後，受影響範圍交由隔離 reviewer 重驗。
4. validator 與 CI 通過後，候選版本才可進入 Human 決策。
5. Human Chief Engineer 保留最終接受、拒絕、範圍核准與正式發布權。

本流程不要求返回 Astra。模型相同不會自動破壞審查獨立性；獨立性由 context 隔離、固定輸入、作者／reviewer 分責、不能自修自批及可重現 finding 記錄建立。

## Reviewer 必查

- A–D requirement IDs 是否都有 owner、acceptance、Evidence 與可驗證狀態。
- E 是否仍為 `NOT_STARTED`，且 Core 是否誤納 runtime、scripts、prompts、deployment HOW。
- 總藍圖是否清楚說明 100 席位、五步工作流、角色／技能／Evidence／review、Human 權限、成果限制及可證明進度。
- 四方版本 tuple 是否完整區分 Core、Implementation、Local checkout 與 Evidence Bundle。
- Agent Zero 來源是否只作 provenance/reference，沒有虛構採用或能力聲稱。
- 舊 Astra → Sol → Astra 契約是否仍可查閱，但不再控制現行批次。
- 預設自動化是否明確禁止未授權 checkout、merge、push。

## Git 與發布權限

審查本身不授權 Git checkout、merge 或 push。AERIS 的預設自動化對這三項皆為禁止；若 Human 對某次治理發布給出明確、當前且有界的授權，執行者只能處理該指定 repository、branch 與 gate。

Reviewer 的 PASS 是技術建議，不是 Human 核准，也不是 runtime／真機驗收。PR CI 成功只證明該 CI 覆蓋範圍；合併後 main 仍需自己的 CI 結果。

## 歷史契約

[AERIS Astra → Sol → Astra 審查閘門 v1](ASTRA_SOL_REVIEW_GATE_V1.md) 及其 `AERIS-ASTRA-SOL-REVIEW-20260907` 記錄保留為歷史來源。2026-09-07 的 Human 決策以本 v2 取代其「必須返回 Astra」與 `HOLD_FOR_SOL_RED_TEAM` 路由；歷史內容不得被改寫成現行政策。
