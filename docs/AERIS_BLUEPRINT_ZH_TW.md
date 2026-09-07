# AERIS 繁體中文總藍圖

版本：`0.7.0-ad.1`

範圍：A–D Core／WHAT；E 尚未開始

狀態依據：[機器可讀追溯契約](../aeris.traceability.json)

## 一句話說清楚 AERIS

AERIS 是由一位 Human Chief Engineer 掌握最終權限、以聲學工程需求為中心、用可替換的 AI 模型協助完成工作，並以證據、獨立審查及可重現性判定成果是否可信的工程組織系統。

它的核心資產不是某一個模型，而是產品需求、角色責任、技能契約、工程知識、決策、Evidence、驗收規則與研究來源。模型可以換，這些可追溯資產仍必須成立。

## 這不是 100 個常駐代理

「100 個角色」代表 100 個能力與責任席位，不代表同時啟動 100 個 LLM process。每個席位界定可處理的問題、可用技能、風險上限、必交證據，以及不能自行核准的事項。

收到工作時，AERIS 才從能力席位中選出足夠的小隊。一般任務可由 2–8 個角色完成，複雜任務可擴大到 5–15 個角色；實際規模由需求與風險決定。角色名稱不等於專業能力，只有通過適用測試、留下 Evidence 並完成審查，才可聲稱該範圍已達標。

## 五步工作流

1. **定義問題與權限**：把人的目標轉成有 ID 的需求，標出限制、完成條件、資料界線與需要 Human 決定的事項。
2. **組成任務小隊**：依需求挑選角色與技能，指定執行者和獨立 reviewer，避免同一責任主體自行核准成果。
3. **產出工程成果**：執行被授權的工作，保留輸入、假設、版本、單位、條件、產物與失敗資訊。
4. **用證據審查**：把成果對照需求與驗收條件；Evidence 不足、測試失敗或來源不明時，狀態不能升級。獨立 reviewer 應找反例，而不是附和執行者。
5. **由 Human 決定採用**：Human Chief Engineer 保留最終裁決、範圍核准與不可逆發布權。通過的結果可成為受控知識；未通過的結果保留限制與下一個最小行動。

這五步是產品行為契約。執行引擎、script、prompt、部署方式與本機路徑屬於 Implementation repo 的 HOW，不在 Core 指定。

## 角色、技能、證據與審查

| 概念 | 它回答的問題 | 必守規則 |
|---|---|---|
| Role | 誰對這類判斷負責？ | 有明確 scope、authority、risk ceiling 與 review conflict。 |
| Skill | 可重複使用哪一種能力？ | 有輸入、輸出、限制、失敗條件與評估方式；不能只是一段 persona。 |
| Evidence | 為什麼能相信成果？ | 指回需求、來源、條件、版本、工具結果與產物；推論不能冒充量測。 |
| Review | 誰用什麼標準找錯？ | reviewer 與 implementer 必須隔離；修訂後受影響範圍重新審查。 |
| Human Gate | 哪些決定不能由系統代替？ | 範圍、風險例外、不可逆行為、正式發布與最終裁決由 Human 掌握。 |

## Human 與 AI 的權限

Human Chief Engineer 是最終權限。Core 是產品需求、治理與驗收的設計權威；Implementation 是執行方式的權威；Evidence 是工程判斷依據。AI 可以分析、產出與審查，但不能因模型自信、角色投票或畫面顯示綠色，就自行宣布工程完成。

任何自動化都不得自行 checkout 未核准版本、merge 或 push。這些 Git 動作只有在目前 Human 指示明確授權、目標可驗證且必要 gate 已滿足時，才可由受控發布流程執行。Human 仍可拒絕已通過技術審查的候選版本。

## 真實成果與限制

AERIS 的成果可以是需求、設計決策、計算、分析報告、測試計畫、工具輸出、Evidence Bundle、審查結論或可執行的 Implementation。每一項成果都要說明適用範圍與限制。

下列敘述不能互相替代：

- 文件存在不代表 runtime 已實作。
- 程式可啟動不代表工程功能已驗證。
- CI 通過不代表真機、離線、硬體、聲學量測或正式發布已通過。
- 多個模型同意不代表有工程證據。
- 介面顯示完成不代表 Evidence 完整。
- 模擬結果不等於量測事實；推論必須標成推論。
- 需要 license、校正、硬體、客戶資料或實體操作的範圍，在條件不存在時必須保留為限制或外部阻擋。

## 可證明的進度

進度以 requirement ID 為最小單位。每個 ID 必須同時指向：需求文字、owner、狀態、驗收條件與 Evidence。狀態只能由對應證據支持，不能靠百分比、聊天摘要或人工改字升級。

本批 A–D 的人類可讀對照在 [追溯矩陣](governance/AERIS_TRACEABILITY_MATRIX.md)，機器可讀真相在 [`aeris.traceability.json`](../aeris.traceability.json)。A–D 表示 Core 文件與治理契約已建立；它不代表 Implementation runtime 已完成。E 明確為 `NOT_STARTED`。

## 四方版本一致

任何宣稱「版本一致」都必須記錄同一個四方 tuple：

1. **Core Blueprint**：Core repository、branch、commit SHA 與架構版本。
2. **Implementation**：Implementation repository、branch、commit SHA 與所宣稱支援的 Core SHA。
3. **Local checkout**：實際執行環境的 HEAD、dirty state／overlay digest 與設定或資產版本。
4. **Evidence Bundle**：驗收範圍、產物 digest、測試結果、時間與 reviewer decision。

四方資料缺一，就只能說明已知的文件或程式狀態，不能宣稱端到端一致。Core SHA 相同也不代表 Local 沒有未提交差異；CI 成功也不能代替 Evidence Bundle 內的真機結果。

## Core 與 Implementation 的所有權

Core 只擁有 WHAT：

- 產品需求與不可變原則；
- 治理、角色、權限與風險界線；
- 驗收條件、狀態語義與 Evidence 要求；
- 研究 provenance、來源判斷與設計決策。

Implementation 擁有 HOW：

- runtime 與狀態機的程式實作；
- scripts、adapters、安裝與維運工具；
- prompts、模型/provider 組態與執行策略；
- 部署、服務、OS persistence 與機器特定設定。

Core 可以要求某個結果可驗證，但不指定私人本機路徑、shell 命令、服務啟動方法或某一個 provider 的執行細節。既有 Core 中超出此邊界的歷史材料視為待遷移債務，不構成新增 HOW 的先例。

## A–E 範圍

| 工作流 | 名稱 | 本批成果 | 狀態 |
|---|---|---|
| A | 白話繁中總藍圖、100 席位正確語義、五步工作流 | IMPLEMENTED |
| B | decision log、requirement traceability、可證明進度、四方版本一致 | IMPLEMENTED |
| C | Core／Implementation 的 WHAT／HOW ownership | IMPLEMENTED |
| D | Sol implementer＋隔離 Sol reviewer、Human 最終權限、舊 Astra 記錄歷史化 | IMPLEMENTED；需依現行 gate 記錄審查結果 |
| E | runtime、scripts、prompts、deployment 的實際施工 | NOT_STARTED |

## 研究來源與採用界線

本藍圖延續 AERIS 既有研究索引與來源清單。Agent Zero 官方網站 [https://www.agent-zero.ai/](https://www.agent-zero.ai/) 作為 agent framework 的參考入口；本次只記錄參考來源，不宣稱採用其 runtime、程式碼、授權條款或安全模型，也不把外部產品的存在當成 AERIS 能力已完成的證據。

相關來源：

- [AERIS Master Research & Architecture Baseline](research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)
- [AERIS Research Data Index](research/AERIS_RESEARCH_DATA_INDEX_20260831.md)
- [本批治理決策記錄](governance/AERIS_DECISION_LOG.md)
- [本批追溯矩陣](governance/AERIS_TRACEABILITY_MATRIX.md)
