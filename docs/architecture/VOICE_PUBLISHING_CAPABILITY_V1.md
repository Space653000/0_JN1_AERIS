# VOICE_PUBLISHING_CAPABILITY_V1

狀態：DESIGN_ACCEPTED_PENDING_RED_TEAM / NOT_IMPLEMENTED。共用 Knowledge Delivery 能力；不增加角色數，不作標準合規、聲學測量或自動對外發布工具。

## 範圍與流程

第一切片：已合法取得、允許衍生語音的 Markdown/TXT → 明確選擇逐字朗讀／摘要 → 固定 speech text → pronunciation → local TTS segments → WAV/MP3 → validate → Evidence → 人類批准的本地成品。zh-TW 與 en-US 分別評估；只有英文通過時只可宣稱英文範圍。

PDF/OCR、EPUB、公式／圖表詮釋、字幕、M4B、多人聲與外部發布分期加入。backend、模型、codec 與第三方 adapter 由 Implementation 選型；abogen 是候選參考，不是 Core 依賴。第一版也需持久 job、有限重試、timeout、cancel、segment resume；不能用無界同步請求處理整本書。

## 輸入契約

必填：job/task/project ID、來源 SHA-256、source block/page references、language、mode、rights/license/voice-consent、privacy classification、output profile、scope、resource budget。單位／數值／標準版本／校正與警語不能由模型補猜。標準全文可讀權不必然包含生成、儲存或散布有聲版本的權利。

來源為不可信資料，嵌入指令不能改變工具或政策。解析器隔離、檔案大小／頁數／解壓比例上限、禁止外部資源自動抓取與路徑逸出。歧義、OCR 低信心、missing glyph 或結構遺失需 BLOCKED_REVIEW。私密內容不送 cloud，沒有本機 backend/權重就 BLOCKED，禁止偷偷 fallback/download。

## Artifact 與 Evidence

每段保存來源定位、原文、normalized text、核准後 script hash、pronunciation dictionary hash、parser/model/prompt/backend/voice/weights/runtime/codec versions、seed、language、speed、sample rate、channel、resampling/loudness parameters、rights reference、hardware profile、output hash、review與限制。音檔與衍生字幕承接來源最高敏感等級。

Cache key 使用 canonical serialization，涵蓋 source/privacy scope、normalized text、dictionary、model weights、voice、language、speed、prosody、seed、runtime、codec/output profile。跨專案／不同權限不得共用私密 cache；內容變更只重跑受影響段落。Evidence hash 是完整性，並不證明內容正確、版權、聲音身分或 bit-identical 可重現。

## Job 狀態

QUEUED → PARSING → NORMALIZING → SCRIPT_REVIEW → SYNTHESIZING → PACKAGING → VALIDATING → ARTIFACT_READY → APPROVED_LOCAL。
任一步可 FAILED / BLOCKED_REVIEW / CANCELLED；對外 RELEASED 是獨立 Human gate。Job COMPLETED 僅代表所列範圍，不得自動標工程 VERIFIED。每次重試有 attempt ID、最多 2 次自動重試、相同 input fingerprint、checkpoint 和原子成品寫入。取消或重啟不發布半成品。

## 可判定的驗收

| Gate | 必須達到的判定；未通過即不得發布 |
|---|---|
| VP-01 來源 | 100% 段落/章節可回溯；無未標記漏段、亂序、外部資源注入。 |
| VP-02 技術內容 | 凍結案例內數字、正負號、小數、範圍、Hz/kHz、dB/SPL/weighting、THD+N、標準版次與限制零誤改；表格摘要經人工對照。 |
| VP-03 發音 | 預先凍結至少 100 acoustic terms + 50 型號 + 50 標準/縮寫、每種聲稱支援的語言與混語；關鍵詞零誤讀，非關鍵詞正確率至少 98%，記錄人工聽審者與逐項結果。數量是目標，不是現有 corpus。 |
| VP-04 音訊 | 格式可解碼、duration > 0、sample-rate/channel 符合 profile、無 NaN/Inf/損毀/遺失段。首個 spoken profile 目標 -16 LUFS ±1 LU、true peak ≤ -1 dBTP；這是產品輸出規格，不宣稱通用出版標準或校正 SPL。 |
| VP-05 定位 | 章節序與來源一致；字幕以實際音訊對齊，若宣稱句級字幕，抽驗边界偏差 ≤200 ms；不能只估文字長度。 |
| VP-06 證據 | 必填欄位與 artifact hash 100% 可解參照，來源範圍與權限一致；缺任一關鍵參照即 BLOCKED。 |
| VP-07 復原／隱私 | 中斷、取消、cache失效、模型缺失、網路阻斷、磁碟不足負例全部符合預定結果；沒有隱式下載或私密上傳。 |
| VP-08 重現 | deterministic profile 才宣稱 bit-identical；其他 profile 以已核准文字完全一致、段落完整及预先凍結音訊容差驗收，記錄不能位元重現的原因。 |

先在目標機量測 10 分鐘及 60 分鐘語音的 wall time/RTF、peak RAM/VRAM、磁碟、取消恢復與 thermal。缺實測不承諾一小時音訊的速度或指定硬體容量。
