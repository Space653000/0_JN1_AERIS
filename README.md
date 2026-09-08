# AERIS 一位人類主管＋100 個聲學專業能力席位的聲學工程師 = 一人抵百人 AI 聲學公司。

每次接手先讀 [接手入口與進度說明](HANDOFF.md)；[版本觀測紀錄](aeris.handoff.json) 是快照，最新版本需即時核對。

[定稿藍圖、發布條件與後續變更管制](BLUEPRINT_BASELINE.md)。定稿以實際 tag 與驗證紀錄為準，產品能力仍須驗收。

## 三個參考方向，如何用在 AERIS

AERIS 的目標是「一位人類主管，搭配 100 個聲學專業能力席位」。以下是已納入藍圖的設計要求；介面、技能與真實工程能力仍須逐項實作及驗證。

### 雷小蒙／Kairos：整體 UX/UI、導覽與卡片布局

參考 [雷小蒙／Kairos](https://os.lifehacker.tw/) 的介面呈現方向：

- **窄側邊導覽、留白與青綠色重點**：畫面乾淨，資訊有層次。
- **卡片與分類**：快速了解目前能力與工作狀態。
- **工作紀錄與能力圖譜**：看得出系統做過什麼、有哪些專業能力，並區分各自的驗證狀態。
- **繁中說明**：用日常語言解釋功能。

### Agent Zero：代理、工具、記憶與工作流程呈現

[Agent Zero](https://www.agent-zero.ai/) 為 AERIS 的互動方式與操作透明度參考。AERIS 參考其本機代理、工具、記憶與工作流程的呈現方向，設計繁體中文操作介面。

所有功能仍須符合 AERIS 的聲學需求、權限與 Evidence Hard Gates。是否採用其程式碼或執行框架，須另行評估授權、安全性、相容性及維護成本。

### 哈利說的：AI軟體必修課——技能範例、互動練習與白話解說

參考 [氛圍學院](https://academy.vibetech.tw/home)／哈利說的教學呈現方向，讓使用者透過範例、互動練習與白話解說理解技能；教材自行製作或採合法授權來源。

**所有技能必須有繁中教學範例與預期結果；可執行範例須提供可重現驗證。** 教學展示、合成資料與真實工程驗收必須清楚區分。缺少範例或證據時，不得標示為已驗證。

詳細設計與驗收條件見 [UX／操作透明度／技能範例規格](docs/architecture/AERIS_UX_SKILL_EXAMPLES_V1.md)。

## 藍圖版本與治理入口

Architecture revision: v0.7.0-governance.4；REVIEW_PENDING / NOT VERIFIED。
[繁體中文總藍圖](docs/AERIS_BLUEPRINT_ZH_TW.md) 是產品入口；[constitution](constitution.md) 是 GATE-01～08 強制治理。
Blueprint 是 WHAT；Implementation 是 HOW；`C:\0_JN1_AERIS` 是唯一正式產品與本機寫入根目錄。
本批僅治理整合，A–D 尚未完成，E 後續全面本機驗收 NOT_STARTED。CI 文件檢查不能證明產品完成。

- [執行規則](AGENTS.md)
- [讀取順序](docs/governance/AI_READ_ORDER.md)
- [現行 Gate](docs/governance/ASTRA_EXECUTION_GATE_V3.md)
- [追溯矩陣](docs/governance/AERIS_TRACEABILITY_MATRIX.md)
- [機器可讀契約](aeris.traceability.json)
- [審查狀態](aeris.review.json)
- [研究整合](docs/research/AERIS_PROPOSAL_INTEGRATION_20260907.md)

參考 [Agent Zero](https://www.agent-zero.ai/) 的代理、工具、記憶與工作流程呈現；不是已採用或已驗證聲學能力的證據。100席位是責任/能力邊界，不是100個常駐代理或100名已驗證真人工程師。
兩個 GitHub URL 只識別專案；先 admission/drift，再單批驗證。

- [Kairos UX/UI、Agent Zero 透明流程、所有技能繁中範例規格](docs/architecture/AERIS_UX_SKILL_EXAMPLES_V1.md)
