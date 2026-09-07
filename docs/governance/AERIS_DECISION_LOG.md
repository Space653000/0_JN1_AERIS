# 現行治理決策與歷史

## ADR-AD-008 — 使用者最新授權，0.7.0-governance.2

決策狀態 ACCEPTED（使用者裁定）；實作驗證 REVIEW_PENDING / NOT VERIFIED。
最新指示全面 Astra Low、自主解決可判斷矛盾、Blueprint寫好、Implementation連動唯一產品 `C:\0_JN1_AERIS`，其他本機目錄不動。取代 ADR-AD-005 的 Sol 路由及早期強制Medium；模型選擇只是操作路由。
ADR-AD-003 四方 tuple 修正為 Blueprint、Implementation、Local checkout、Running service；Evidence 綁定tuple。
ADR-AD-004 公開唯一產品根目錄是使用者契約，禁止私人帳戶路徑仍保留；Core唯讀治理validator/負例/CI是窄例外。
ADR-AD-007 的 E 誤定義被取代：E 是後續全面本機驗收，不是所有HOW；A/B/C/D恢復使用者原始意義。A–D仍待逐批驗證，不因文件存在而完成。
無條件Full Build、任意workspace及正常部署之外永久禁止Core發布，分別改成admission/單批、唯一根目錄、明確授權治理PR。此決策不弱化聲學、隱私、Evidence、獨立驗證及不可逆發布規則。

## 下列是歷史來源，不是现行执行授权

# AERIS 治理決策記錄

決策集：`AERIS-A-D-GOVERNANCE-20260907`

架構版本：`0.7.0-ad.1`

本檔只記錄 Core 的產品與治理決策。執行方式由 Implementation repo 決定。

## ADR-AD-001：100 席位是能力邊界

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-A-002`
- 決策：R001–R100 是可選用的 capability／authority／evidence／review seats，不是 100 個常駐代理。
- 理由：能力清單需要穩定識別；實際任務只需組成足夠的小隊，避免用進程數或模型數假裝成熟度。
- 後果：任何介面或報告不得用「100 個角色存在」推導「100 個角色已驗證」。

## ADR-AD-002：採用五步產品工作流

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-A-003`
- 決策：所有工程工作遵循「定義問題與權限 → 組隊 → 產出 → 證據審查 → Human 決定」。
- 理由：讓需求、執行、審查與最終權限形成一條可追溯鏈。
- 後果：Implementation 可選擇執行技術，但必須保留這五個語義階段及其 gate。

## ADR-AD-003：進度必須由 requirement 與 Evidence 證明

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-B-001`、`AERIS-AD-B-002`
- 決策：狀態升級要能從 requirement ID 追到驗收與 Evidence；版本一致必須記錄 Core、Implementation、Local checkout、Evidence Bundle 四方 tuple。
- 理由：單一 SHA、CI 綠燈、UI 百分比或模型共識都不足以證明端到端成果。
- 後果：缺少任一方資料時，報告必須縮小宣稱範圍。

## ADR-AD-004：Core 管 WHAT，Implementation 管 HOW

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-C-001`、`AERIS-AD-C-002`
- 決策：Core 只新增產品需求、治理、驗收及研究 provenance；runtime、scripts、prompts、deployment 由 Implementation 擁有。
- 理由：設計權威要跨機器與工具保持穩定，執行細節則需要獨立演進。
- 後果：Core 新文件不得包含私人絕對路徑或把實作細節寫成唯一解。既有越界材料列為歷史遷移債務。

## ADR-AD-005：A–D 改採 Sol／Sol 獨立審查

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-D-001`、`AERIS-AD-D-002`
- 決策：本批由 GPT-5.6 Sol High implementer 產出，另由隔離 context 的 GPT-5.6 Sol High reviewer 審查。不再要求返回 Astra。Human Chief Engineer 保留最終權限。
- 理由：使用者已更新模型路由；獨立性來自作者與 reviewer 的 context／責任隔離，而不是品牌或模型名稱差異。
- 後果：reviewer 不得沿用 implementer context 或自行修補後核准。任何修訂都使受影響的舊審查失效。舊 [Astra → Sol → Astra 閘門](ASTRA_SOL_REVIEW_GATE_V1.md) 保留為歷史，不再是現行 gate。

## ADR-AD-006：禁止未授權的自動 Git 發布

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-D-002`
- 決策：AERIS 的預設自動化不得自行 checkout 任意 ref、merge 或 push。只有目前 Human 明確授權的治理發布或其他明確範圍，才能執行指定 Git 動作。
- 理由：自動化便利不能擴張版本選擇與發布權限。
- 後果：現行 reviewer 可建議接受或拒絕候選版本，但 Human 仍有最終決定權。

## ADR-AD-007：E 保持未開始

- 狀態：ACCEPTED
- 關聯需求：`AERIS-AD-E-001`
- 決策：本批不施工 runtime、scripts、prompts 或 deployment；E 固定為 `NOT_STARTED`。
- 理由：先建立可審查的產品與治理契約，再由另行核准的 Implementation 批次實作 HOW。
- 後果：A–D 的完成不得被描述成 AERIS runtime 或真機驗收完成。
