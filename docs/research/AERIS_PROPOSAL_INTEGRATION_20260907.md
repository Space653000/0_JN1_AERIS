# AERIS 兩份提案整併評估

架構版本：**0.6.0-review.1**；狀態：**設計採納／禁止施工／等待 Sol**。
來源：Core `82f4554623b2d87185dac39a3b93194af7dd5275`、Implementation `32ca69baa778959d01c10a72bba1a8f0c0ac7eb5`、[兩份原文與雜湊](inputs/2026-09-07/README.md)。

| 提案內容 | 決策 | 納入方式與理由 |
|---|---|---|
| 100 capability pool、按需組隊、Evidence／獨立審查／Human | KEEP | 既有 Core 已有；保留，不建立第二套同義架構。 |
| 10 divisions × A001–A100 | MODIFY | 作為候選搜尋／能力標籤視圖；Canonical 保留六群 R001–R100。角色數與職能覆蓋不同，禁止等號換號。 |
| A100 = Reviewer | REJECT AS REPLACEMENT | 既有 R100 是 Autonomous Experiment & Optimization，R098 才是 Acoustic Red-Team / DFMEA Reviewer；覆蓋會改變歷史責任。 |
| Mission-first、問題導向首頁 | MODIFY | Mission 是 Project/Requirement/Task/Workflow 的協調視圖；先補同一 task_id 的可追溯關聯，不再創第二套狀態真相。 |
| 16 個導覽入口、100 卡片、示意 KPI | DEFER | 維持 Dashboard／Workspace／Services 三入口與 v0.5 視覺；專家池在次層，示意數字不能流入正式狀態。 |
| Specialist contracts／Goldens／maturity／版本化 standards | ADD DETAIL | 採用 role × capability × scope 評估，補 reject cases、輸入假設、誤差與授權。 |
| OneManCompany 等可直接套用 80–95% | NOT VERIFIED | 原文保留為來源意見；沒有固定版本、授權、重現測試，不能作採購或建置依據。 |
| Voice Publishing shared capability | ADD | 採 [Voice Contract](../architecture/VOICE_PUBLISHING_CAPABILITY_V1.md)，不是第 101 個角色。 |
| abogen／Kokoro／其他 TTS | DEFER SELECTION | 可作 optional adapter/reference；本次不 clone、install 或綁定 backend，逐語言評估與授權查證後選擇。 |
| PDF／EPUB 在首階段 | MODIFY | 最小切片先 Markdown/TXT；PDF/OCR/EPUB 到下一階段，避免解析誤差與不必要依賴。 |
| Job／Cache 留到 Phase 2 | MODIFY | 最小持久 job、cancel、timeout、segment resume 在長任務第一版就要具備；較複雜排程後移。 |
| 可重現完全相同音訊 | MODIFY | Bit-identical 與 tolerance-equivalent 分開；GPU/TTS 不確定性、codec、seed、環境必須記錄。 |
| 摘要／表格轉語音 | MODIFY | 朗讀與摘要分模式，來源段落逐段映射；數值、單位、否定、限制與來源授權為硬性 gate。 |

## 1000 字內評估結果（第 1 項）

兩份提案值得納入，但不適合原封不動變成施工命令。100-Specialist 的核心思想與 AERIS 原藍圖一致，真正新增價值是能力契約、問題導向操作與領域評估；主要衝突是新舊角色編號與組織分工，尤其 A100 與 R100 完全不同。因此保留原有識別，將新分類視為可映射的候選視圖。Voice Publishing 適合作為共用平台能力，先做可追溯的 Markdown/TXT 朗讀，再擴充 PDF、EPUB 與有聲書。它必須維持本機隱私、專業詞彙、內容授權與數值正確，並區分生成成功與出版核准。Astra 更新改善審查工具選擇，不能證明本機模型、百人專業能力或語音品質已達標。結論是有條件採納設計，後端選型與施工保持暫停。
