# AERIS CORE EXECUTION DISCIPLINE

版本：0.7.0-governance.4；狀態：REVIEW_PENDING / NOT VERIFIED。
這是 AERIS 專案治理，不覆蓋平台安全規則。使用者最新明確裁定高於舊專案契約；其餘更嚴格的聲學、隱私、Evidence 與人類權限保留。任何無法依已授權目標解決的矛盾，STOP → REPORT；可解矛盾先記錄來源及決策，再重驗。此批僅治理整合，沒有功能施工或 E 驗收授權。

## GATE-01 — Blueprint 是唯一設計真相
`Space653000/0_JN1_AERIS` 是唯一 Blueprint / Architecture Source of Truth。
Implementation 與本機不得自行發明、改寫、擴充架構。需要變更時，先改 Blueprint、升版、審查，再改 Implementation。設計與實作衝突，依 Blueprint 停工，不能直接接受 drift。

## GATE-02 — Implementation 只能落實 Blueprint
`Space653000/0_JN1_AERIS_Local-computer-implementation` 只落實已核准 Blueprint。禁止偷改目標、新增未核准架構、刪減必要功能、為通過測試降低驗收。
Core 的唯一程式窄例外：唯讀治理 validator、其負例測試及 CI；不能包含 runtime、部署脚本或功能提示詞。既有 HOW 材料是歷史遷移債務，不構成新增先例。

## GATE-03 — 本機才是真實產品
`C:\0_JN1_AERIS` 是使用者明確授權公開的唯一正式 Runtime / Product Environment 契約，不是私人路徑洩漏。
所有正式程式碼、設定、模型配置、Skill、RAG、Database、Log、Evidence 均須存在於此根目錄。隔離 worktree、測試及輸出須在此根目錄內；它們不能冒充 running service。其他本機目錄不得寫入、搬移或視為成果。歷史來源紀錄保留，不授權重用歷史路徑。公開資料仍須排除私人帳戶路徑、secret、客戶資料、私人 Evidence。

## GATE-04 — Evidence Before DONE
每個 DONE 必須同時有：實際執行、可重現測試、Expected Result、Actual Result、PASS / FAIL、Log / Screenshot / Output / Report、對應 Blueprint Requirement ID。
缺任一項：STATUS = NOT VERIFIED；不得標記 DONE / COMPLETE / PASS。文件存在僅證明文件存在；CI 不證明本機模型、量測或公司完成。Evidence 必須記錄命令、版本、時間、產物雜湊與限制。

## GATE-05 — 禁止自我證明
AI 宣稱完成不算驗收。關鍵架構、重大功能、Release Gate 須隔離審查者或獨立重新執行驗證；作者不得修復後同一 context 自行核准。修訂使受影響的舊審查失效。Human Chief Engineer 保留最終及不可逆發布權。

## GATE-06 — Drift 立即停止
重大修改前後核對 Blueprint → Implementation → Local Runtime。
發現 drift：STOP → REPORT → FIX SOURCE OF TRUTH → RE-VERIFY。
允許有界治理修復以解決已報告 drift，但禁止帶 drift 繼續功能施工。四方 tuple 是 Blueprint SHA、Implementation SHA、Local checkout HEAD/dirty digest、Running service loaded SHA；Evidence 綁定整個 tuple，不取代 Running service。缺項只能 NOT VERIFIED。

## GATE-07 — 模型使用紀律
依使用者最新裁定，預設 GPT-6 Astra / Low 負責分析、治理、架構、修改、提示詞、施工與判斷；不強制切 Sol、回 Astra 或升 Medium。
這是可替換的操作路由，不是聲學 domain contract。實際模型須由可查執行 metadata 記錄，僅設定文字不能證明使用模型。不能為節省 Token 降低驗收標準；独立性仍依 GATE-05。

## GATE-08 — 一次只通過一個 Gate
Plan → Implement → Execute → Evidence → Verify → PASS → Next。
先 admission / drift 檢查，再一個有界批次。禁止僅貼兩個 URL 就無條件 full build、禁止大量施工最後一次驗收。舊自動補齊全部軟體缺口契約由本條取代；功能 backlog 保留，每批通過才進下一批。

## 保留既有聲學與安全要求
以下承接 Implementation `company/CONSTITUTION.md` 既有規則，沒有降低標準：
1. LLM 推論不得寫成量測事實。
2. 工程數值附 unit、condition、source。
3. Simulation 保存 boundary conditions、method、tool version。
4. Measurement 保存 calibration state、fixture、environment。
5. Standards 保存 edition、status、effective scope。
6. Correlation 不佳不得用 tuning 掩蓋未確認 root cause。
7. Algorithm 改善檢查 latency、compute、memory、power。
8. Speaker tuning 檢查 excursion、temperature、distortion。
9. Mic algorithm 跨 noise、distance、azimuth、speaker、language 驗證，不用模糊 scenario 取代。
10. PASS/FAIL 同時提供 margin（適用工程數值判定）。
11. 重大 design decision 保存 Evidence Bundle。
12. 正式工程完成須符合 Verification / Approval policy。
13. offline mode 禁止 configured cloud provider。
14. 正常 build/deployment 的 Core 唯讀；使用者明確授權的有界治理變更可由代理提交及發布候選 PR，通過獨立審查與 CI 後才可依授權合併；不自動改 Ruleset、settings 或 force push。
15. Model 可替換；Constitution、Skills、Methods、Evidence 不綁模型品牌。

NO EVIDENCE = NOT DONE.

必讀 [保留較嚴格規則](docs/governance/RETAINED_STRICT_RULES.md)：除精確列出的使用者取代條款，其餘原規範仍有效。schema v3 是治理候選，舊 runtime consumer 尚未遷移；不得宣稱相容或enforcement已完成。
