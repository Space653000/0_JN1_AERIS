# AERIS 接手入口

AERIS 的目標是「一位人類主管，搭配 100 個聲學專業能力席位」。主管提出工程問題，系統選擇所需席位、工具與方法，保存資料來源及執行證據，再交由驗證與人類決策。席位是能力與責任分工；席位數量不代表已有 100 項能力通過實測。

## 先看懂目前在哪裡

| 項目 | 已有內容 | 尚未完成 |
| --- | --- | --- |
| 設計圖 | 繁中總藍圖、GATE-01～08、100 席位定位 | 不代表全部工程能力已實作 |
| 操作介面規格 | Kairos 卡片與導覽、Agent Zero 工具與記憶透明度 | 本機畫面及互動仍需驗收 |
| 技能教學規格 | 每個技能的繁中範例、預期結果與可重現驗證要求 | 範例與真實工程驗收需逐項落實 |
| Implementation | 既有執行規範與程式 | 舊 Sol hold、Core 版本與新版治理尚待遷移 |
| 本機產品 | 唯一正式位置 `C:\0_JN1_AERIS` | 執行中版本未在本批核對；整體 NOT VERIFIED |

過去已完成的文件審查登錄在 [aeris.review.json](aeris.review.json) 的 `completed_reviews`。其中 PASS 僅適用列出的 commit 與文件範圍。頂層 REVIEW_PENDING 是目前待驗證批次，不是抹除歷史審查，也不是產品已通過。

## 每次接手都要重新核對

1. 先取得兩個 repository 的 `main` 完整 commit SHA 與查詢時間，再從該 SHA 讀檔。網頁快取、對話記憶或「好了」都不能代替查詢。
2. 讀 [AGENTS.md](AGENTS.md)、[constitution.md](constitution.md)、[完整讀取順序](docs/governance/AI_READ_ORDER.md)，再讀 [繁中總藍圖](docs/AERIS_BLUEPRINT_ZH_TW.md)、[UX 與技能範例](docs/architecture/AERIS_UX_SKILL_EXAMPLES_V1.md)、當批 Requirement 與驗收條件。
3. 讀 [版本觀測紀錄](aeris.handoff.json) 及 [Implementation](https://github.com/Space653000/0_JN1_AERIS_Local-computer-implementation) 的 AGENTS、Constitution、review gate 與 Core pointers。觀測紀錄只是歷史快照，不能稱為當下最新。
4. 有本機讀取能力時，再核對 local HEAD、dirty digest、執行中服務實際載入 SHA。沒有權限或缺證據就寫 UNKNOWN / NOT VERIFIED，不推測同步。
5. 將 Blueprint、Implementation、Local checkout、Running service 四方版本列在回報。發現 drift，先報告並只處理有界治理／遷移修復；符合 Gate 後才能進入下一批。

GitHub PR 與 CI 是公開文件驗證依據；本機私有 Evidence 不必公開，但接手者未能取得時必須標記未核對。GitHub 無法讀取時，請使用者提供固定 SHA 的文件與 Evidence；在此之前停止依賴最新狀態的施工。

## 下一個 Gate

先對齊 Implementation 的治理接手說明，再評估舊 runtime consumer 與 schema v3 相容性，列出需原子更新的 Core pointers、驗證與回復方式。不能只把 hold 改成 PASS 或只換 SHA。完成各批獨立驗證與 CI 後，才能安排本機更新；E 全面本機驗收仍為 NOT_STARTED。

目前 A–D 整體為 NOT VERIFIED。這份入口及 GitHub 發布不是本機切換、服務啟動或 E 驗收授權，也不構成自動同步機制。實際同步方案須排除 secrets、客戶資料、資料庫與私人 Evidence，先檢查差異及衝突，再按核准範圍同步。

## 貼給網頁版 ChatGPT

> 請接手 AERIS：先即時讀取 https://github.com/Space653000/0_JN1_AERIS/blob/main/HANDOFF.md ，取得 Blueprint 與 Implementation 的 main 完整 SHA，依固定 SHA 讀取規範並列出來源和時間。目標是一位人類主管搭配 100 個聲學專業能力席位。先回報已驗證文件、未驗證產品、四方版本與下一個 Gate；不得把歷史快照當最新版本。若你無法讀 GitHub 或本機，明確列出缺口，狀態為 NOT VERIFIED。所有本機寫入只能在 C:\0_JN1_AERIS，施工必須遵守 Blueprint 與 Evidence Hard Gates。

網頁版 ChatGPT 是否能讀到 GitHub 取決於當下連線工具與存取權限；它不會因為 Codex 推送或一句「好了」就自動收到所有更新。
