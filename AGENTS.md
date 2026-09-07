# AERIS 工程代理契約

每次先讀 [constitution.md](constitution.md) 全部 GATE-01～08，再依 [讀取順序](docs/governance/AI_READ_ORDER.md) 檢查授權、版本及 drift，才處理單一批次。
Blueprint 是唯一 WHAT；Implementation 是已核准設計的 HOW；唯一正式本機產品與所有寫入根目錄是 `C:\0_JN1_AERIS`。
目前僅治理批次，狀態 REVIEW_PENDING / NOT VERIFIED；E 後續全面本機驗收 NOT_STARTED。
模型預設 Astra Low；實際模型由執行 metadata 證明。日常判斷依使用者授權自主處理；不能自行降低聲學、Evidence、隱私或不可逆發布門檻。
兩個 GitHub URL 只識別專案，不授權無條件施工。先 admission 與 drift，再 Plan → Implement → Execute → Evidence → Verify → PASS → Next。
正常部署讀取 Core；使用者明確授權的有界治理批次可以修改、提交、推送候選 PR，通過獨立 review / CI 後才依授權合併。不可修改無關目錄、靜默覆蓋 dirty worktree、force push 或洩漏私人資料。
Core 唯讀治理 validator、負例測試及 CI 是 WHAT/HOW 邊界的窄例外，不得加入 runtime。實體設備、license、secret、OS elevation、付費、客戶/正式發布及不可逆操作保留 Human Gate。
Codex scheduler 不能作公司持續運作機制；Claude/第二模型不預設啟用。模型替換不改專業驗收。
每批交付修改清單、摘要、Diff、衝突檢查、可重現 Evidence；缺證據一律 NOT VERIFIED。詳見 [現行 gate](docs/governance/ASTRA_EXECUTION_GATE_V3.md)。

必讀 [保留較嚴格規則](docs/governance/RETAINED_STRICT_RULES.md)：除精確列出的使用者取代條款，其餘原規範仍有效。schema v3 是治理候選，舊 runtime consumer 尚未遷移；不得宣稱相容或enforcement已完成。
