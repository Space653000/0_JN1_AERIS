# 有界批次 SOP

先讀 [Constitution](../../constitution.md)、[現行 gate](ASTRA_EXECUTION_GATE_V3.md)、aeris.review.json 與 aeris.traceability.json。
1. 核對使用者當批授權與唯一根目錄 `C:\0_JN1_AERIS`。
2. 讀取 Blueprint、Implementation 規範；記錄四方版本與 dirty state。drift 立即停工，只准有界治理修復。
3. 定義一批 requirement、Expected Result、測試及回復方式；不得由 URL 自動進入 full build。
4. Plan → Implement → Execute → Evidence → Verify → PASS → Next。
5. 交付 Diff、衝突檢查、Expected/Actual/PASS-FAIL/命令/產物 hash。缺證據 NOT VERIFIED。
6. 關鍵變更隔離 review 或獨立重跑，失敗重新修復及驗證；不得同 context 自我核准。
正常部署 Core 唯讀；已授權治理 PR 為窄例外。runtime、腳本、提示詞、部署都由 Implementation 落實。
