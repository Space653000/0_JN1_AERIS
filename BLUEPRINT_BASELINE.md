# AERIS 定稿藍圖與變更管制

定稿版本名稱：`v0.7.0-blueprint.1`；設計治理版本：`0.7.0-governance.4`。

本文件定義發布條件；只有 GitHub 上實際存在的定稿 tag、對應 commit、三輪檢查證據及生效的保護規則，才證明定稿發布完成。文件存在或名稱帶「定稿」不構成完成證據。發布證據以該 tag 的註解及相應 PR 紀錄為準；tag 未建立時仍為待發布。

## 定稿範圍

一位人類主管，搭配 100 個聲學專業能力席位。README 的「一人抵百人」是產品願景，不是已測得的人力替代率、效能或工程資格。

設計真相依 [constitution](constitution.md)、[讀取順序](docs/governance/AI_READ_ORDER.md)、[繁中總藍圖](docs/AERIS_BLUEPRINT_ZH_TW.md)、[UX 與技能範例規格](docs/architecture/AERIS_UX_SKILL_EXAMPLES_V1.md) 及 [需求契約](aeris.traceability.json)。Kairos 的 UX/UI、Agent Zero 的透明流程、哈利說的繁中互動教學方向均屬設計要求。

定稿只固定這一版設計與驗收要求。歷史研究、原始提案與靜態展示保留各自來源及限制，不升格為當前指令或真實能力證據。Implementation 相容性、四方版本對齊、100 席位的逐項專業驗證仍待完成；A–D 整體 NOT VERIFIED，E NOT_STARTED。

## 三輪發布檢查

1. 固定候選 commit，盤點所有 tracked 檔案及 hash；檢查指定標題、三個參考方向、100 個唯一 Role ID、需求與現行版本，並確認較嚴格規則仍保留。
2. 隔離審查者對同一 commit 檢查適用文件的語意、現行／歷史權威邊界及 Evidence；有阻擋問題就修正並重新固定版本審查。
3. 同一候選的治理檢查、負例測試與 PR CI 通過後才合併；再確認 merged-main CI、遠端內容與保護規則。任何缺項均不得宣告發布完成。

檢查用於發現遺漏，不構成永遠沒有缺點的保證。未來發現新問題時，保留本版證據並按下列程序修訂。

## 鎖定與後續變更

- `main` 必須經 PR、必要 CI 與既有較嚴格保護規則；禁止直接 push、force push 及刪除。
- 定稿 tag 建立後須由 GitHub 規則禁止移動與刪除；不得用同名 tag 覆蓋新版。
- 後續設計變更必須先說明理由、受影響 Requirement 與驗收，升版、獨立審查、CI，再發布新的定稿 tag。不能靜默修改本版。
- 讀取定稿使用 tag 解析後的完整 commit SHA；查最新進度仍依 [HANDOFF](HANDOFF.md) 即時核對。歷史觀測快照不能取代查詢。
- GitHub 管理員仍能修改保護設定；設定被修改時必須留下治理紀錄，不能聲稱管理員也無法改動。

本規則不授權 runtime 部署、付費／硬體操作或正式客戶發布；原有 Human Gate 與 Evidence 要求仍有效。
