# Astra 有界執行與獨立驗證 Gate v3

版本 0.7.0-governance.4；REVIEW_PENDING / NOT VERIFIED。
現行權威為 ../../constitution.md；完整 GATE-01～08 必讀。
使用者已取代 Sol High、強制 Astra Medium/回 Astra、任意工作目錄及無條件 Full Build 的旧路由。Astra Low 操作路由不綁 domain contract。

本批僅治理：先基線 → 修正 → validator/負例 → 保存 Diff/命令/Expected/Actual/結果 → 隔離 review → 依授權發布。作者測試 PASS 不等於獨立 review PASS；修復後重新審查，未滿足不得合併。
治理過關後 A–D 可按已授權目的拆小批功能施工，每批另做 admission/drift，並非一次放行所有 backlog。
E 是 A–D 之後的全面本機驗收，NOT_STARTED；不是所有 Implementation HOW 的代稱。

公開候選治理 PR 已获使用者授權；正式工程/客戶發布另受 Human Gate。自動 fetch 只更新狀態，checkout/merge/push 必須有當批授權、dirty 保護及通過適用 gate。
Runtime enforcement 尚未實作；本批 validator 只驗文件治理，不聲稱運行時已阻擋任何操作。
