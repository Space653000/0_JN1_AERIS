# AERIS Architecture — v0.6 設計基線與現行治理

日期：2026-09-07；**REVIEW BASELINE / NO IMPLEMENTATION AUTHORIZATION**。
現行治理版本：0.7.0-governance.4。模型路由、授權、目錄、續建順序與驗收依 [constitution](../../constitution.md) 及 [Astra Gate v3](../governance/ASTRA_EXECUTION_GATE_V3.md)；本文件保留 v0.6 的聲學設計基線，檔名不代表現行治理版本。與舊研究衝突的 ID、成熟度、風險採本設計基線，其餘 Speaker/Microphone 全領域願景及更嚴格工程要求保留。

## 可落地的產品定義

1 Human Chief Engineer + 100 stable capability seats + local modular monolith + deterministic engineering tools + on-demand model assistance + Evidence + independent review + Human authority。

100 是能力分類與責任邊界，不是 100 個同時推論的程序，也不是 100 名真人工程師能力已實證。模型推論無法代替原始量測、校正、授權工具、domain expert 與責任簽核。前端參考 Kairos 的簡潔；不由畫面推斷其內部架構或 AERIS 成熟度。

## 身分與成熟度

Canonical 為 [100 個穩定 R-ID](CANONICAL_ROLE_REGISTRY_V1.json)：8/18/18/24/20/12 六群；排序或顯示名改變不能改 ID。Axxx 提案屬獨立命名空間，另作 many-to-many crosswalk 後才可用於路由。此 registry 固定設計身分；目前 runtime 仍以位置產生 ID，落地遷移與回歸未施工。

角色能力以 `role_id × capability_id × product/domain scope × method_version × evidence` 衡量：L0 registry、L1 contracted、L2 executable local、L3 evaluated domain baseline、L4 real-evidence verified。原研究 Ask→Discover 六層是能力願景，不可直接轉換為 L0–L4。平台 NOT_IMPLEMENTED/IMPLEMENTED/TESTED/VERIFIED、公司 opening state、角色成熟度是三種不同維度；整間公司完成還需要適用的 Company Done gates。

## 模型與資源

現行 authoring/review 預設 GPT-6 Astra Low，依 constitution GATE-07；不強制 Sol High、升 Medium 或回 Astra。獨立驗證仍依 GATE-05。此操作路由與 AERIS 本地 runtime 模型分離，不因此加入 paid API 或移動私密資料；模型與 effort 必須以執行 metadata 證明，不能用文件設定推定。

普通 Pod 2–8／複雜 5–15 指參與職能數，不是同時載入模型數。初始單機配置先限制一個重型 inference job；TTS 與 LLM 共用 accelerator 時排隊，不以 16GB 標稱 RAM 直接推論 VRAM 足夠。可提高 concurrency 前先取得模型 digest、KV cache、context、量化、峰值 RAM/VRAM、p95 latency、溫度、功耗及故障復原量測。允許拒絕、deadline、cancel、有限 retries；不以雲端靜默 fallback 解決私密模型 OOM。

## 任務與信任邊界

Mission 是使用者意圖及 scope，連結 Project/Requirement/Task/Workflow/Artifact/Review。同一工程任務只有一個 canonical task_id 和單一狀態寫入權；SQLite UI task 與 JSON engineering task 必須由明確 adapter 關聯並對帳，不能各自算完成。

VERIFIED 要解析 G0–G4 與實際封存證據，APPROVED/RELEASED 要對應 Human approval artifact。所有參照須驗證存在、hash、task/scope/role、方法/輸入/校正/標準版本與時效。呼叫端字串 authority、reviewer 名称、approved=true 或 evidence://id 不構成授權。資料變更須使相關簽核 STALE；重放與並行更新採一致的 version check/idempotency。CI通過不代表上述整合已完成。

R0 只讀；R1 可逆本機；R2 有受控執行及獨立審查，physical/hardware risk 加 Human；R3 高衝擊/破壞性；R4 客戶、正式報告、production 或 Core publication。R3/R4 需要人類且不能由模型自授。risk ceiling 與 role_id 都不是授權憑證。

## 聲學正確性

所有 metric 必須帶 units、reference、measurement/synthetic class、calibration、frequency coverage、sampling/grid、method applicability、numerical tolerance、uncertainty budget 與 decision rule。平均 dB 需明示 sample-arithmetic 或 energy/spatial/band weighting，不得混作總 SPL。資料不覆蓋需求頻段時回 BLOCKED_INCOMPLETE_DATA，不能以兩點通過全頻段。每條公開 skill/workflow path 都執行相同輸入驗證，拒絕 NaN/Inf、重複/不單調頻率、未知 schema、缺校正與越權資料。

Boundary decision：PASS/FAIL/INDETERMINATE 與 uncertainty/guard-band 共同記錄；假設不成立先停止。Synthetic fixtures 與真實量測分開統計，任何 Golden 必須有獨立 oracle 與負例；模型同意不作 oracle。

## 分期與範圍

先凍結安全/任務/證據 contract → 修復已證實阻擋項 → 一個真實 FR 任務端到端 → 一個 mic/array 任務 → 按已驗證方法擴展角色 → Voice MVP → 後续輸入/工具/出版。100 roles L2 是長期全局目標，不能要求一次無界代理循环做完；每批限定能力、資料、資源、accept/reject oracle、rollback 和 stop。缺專業儀器不阻擋適用的 free baseline，但不得用 baseline 冒充該儀器驗證。

## UI、Knowledge 與交付

保持 v0.5 三入口及 light/dark identity。Mission-first 透過既有 workspace 進入，能力搜尋／十分類可為第二層。所有模擬數字標 SAMPLE，未驗證即 UNKNOWN/BLOCKED；只顯示預先界定 scope 的 metric。

Knowledge 分來源權利、版本、有效性、適用產品、引用與失效傳播。不可用模型記憶宣稱標準 current；無 live verification 時顯示截至日期及 UNVERIFIED_CURRENT_STATUS。私人資料與音訊留 Local；public query 仍可能人工貼入機密，不能聲稱有完整 OS DLP。Voice 定義見 [Voice Contract](VOICE_PUBLISHING_CAPABILITY_V1.md)。

## 1000 字內評估結果（第 2 項）

AERIS 的組織方向可行：保留單一人類責任者、穩定職能池、模型中立、本機工具與證據鏈，比複製 AI 公司外觀更可靠。但現有藍圖跨文件存在六群與十群、新舊角色 ID、三套成熟度與模型分工的混用，必須先統一解釋。新版固定 R001–R100、拆開參與角色與實際推論併發、補足任務單一真相與可驗證的授權／證據契約，並把全公司目標改為有界批次。真正可行性需由指定機器、合法資料、專業方法、負例、量測不確定度與獨立 review 證明。不能保證所有聲學領域等同百位資深真人，也不能僅靠免費軟體取得儀器校正與正式認證能力。結論：架構可逐步落地，但目前仍是待驗證設計，不核准全面動工。
