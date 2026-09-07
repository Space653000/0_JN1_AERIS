# AERIS A–E 追溯矩陣

本表是 [`aeris.traceability.json`](../../aeris.traceability.json) 的人類可讀投影。若兩者不一致，以 JSON 與 CI validator 的結果為準。

| Requirement ID | 工作流 | Owner | Requirement | Acceptance / Evidence | 狀態 |
|---|---|---|---|---|---|
| `AERIS-AD-A-001` | A | CORE | 提供白話繁中總藍圖 | [總藍圖](../AERIS_BLUEPRINT_ZH_TW.md)存在且由 read order 可達 | IMPLEMENTED |
| `AERIS-AD-A-002` | A | CORE | 明確說明 100 席位不是 100 個常駐代理 | [總藍圖：100 席位](../AERIS_BLUEPRINT_ZH_TW.md#這不是-100-個常駐代理) | IMPLEMENTED |
| `AERIS-AD-A-003` | A | CORE | 定義五步工作流及 role／skill／Evidence／review 關係 | [總藍圖：五步工作流](../AERIS_BLUEPRINT_ZH_TW.md#五步工作流) | IMPLEMENTED |
| `AERIS-AD-B-001` | B | CORE | 進度由 requirement、acceptance 與 Evidence 證明，並記錄四方版本 tuple | [總藍圖：可證明進度](../AERIS_BLUEPRINT_ZH_TW.md#可證明的進度)、本 JSON 契約 | IMPLEMENTED |
| `AERIS-AD-B-002` | B | CORE | 保存研究 provenance，包含 Agent Zero 官方參考入口與採用界線 | [總藍圖：研究來源](../AERIS_BLUEPRINT_ZH_TW.md#研究來源與採用界線) | IMPLEMENTED |
| `AERIS-AD-C-001` | C | CORE | Core 只新增產品需求、治理、驗收、研究 provenance | [總藍圖：ownership](../AERIS_BLUEPRINT_ZH_TW.md#core-與-implementation-的所有權)、[ADR-AD-004](AERIS_DECISION_LOG.md#adr-ad-004core-管-whatimplementation-管-how) | IMPLEMENTED |
| `AERIS-AD-C-002` | C | IMPLEMENTATION | runtime、scripts、prompts、deployment 由 Implementation repo 擁有 | 同上；本批不建立 HOW | IMPLEMENTED |
| `AERIS-AD-D-001` | D | CORE | A–D 採 Sol implementer 與隔離 Sol reviewer，不要求返回 Astra | [現行審查 gate](SOL_INDEPENDENT_REVIEW_GATE_V2.md)、[`aeris.review.json`](../../aeris.review.json) | IMPLEMENTED |
| `AERIS-AD-D-002` | D | CORE | 保留 Human 最終權限與歷史記錄，禁止未授權自動 checkout／merge／push | [現行審查 gate](SOL_INDEPENDENT_REVIEW_GATE_V2.md)、[舊 gate（歷史）](ASTRA_SOL_REVIEW_GATE_V1.md) | IMPLEMENTED |
| `AERIS-AD-E-001` | E | IMPLEMENTATION | 實作 runtime、scripts、prompts、deployment | 無；本批明確不施工 | NOT_STARTED |

## 四方版本記錄

只有下列四項都出現在同一 Evidence Bundle，才可宣稱該範圍版本一致：

| 記錄 | 最低必要欄位 |
|---|---|
| Core Blueprint | repository、branch、commit SHA、architecture version |
| Implementation | repository、branch、commit SHA、declared Core SHA |
| Local checkout | HEAD、dirty/overlay digest、configuration/asset versions |
| Evidence Bundle | scope、artifact digests、test results、review decision、time |

本文件不填入特定機器的私人絕對路徑。實際 tuple 應由 Implementation 的 Evidence 產物保存。

本批固定的 Core 起點為 `fa65e86a8612b227ef4c9e6976ef0060ca2221ac`；2026-09-07 只讀觀察到的 Implementation remote main 為 `5f591f2dbde75e30fe7f61d7f8fbfb56a2c0e433`。Local checkout 與 runtime Evidence Bundle 不在 A–D 範圍，因此目前端到端一致性結論是 `NOT_CLAIMED`，不是把未知欄位補成一致。
