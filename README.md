# vocabuddy-group-t03

[![CI](https://github.com/pinruei0323/vocabuddy-group-t03/actions/workflows/ci.yml/badge.svg)](https://github.com/pinruei0323/vocabuddy-group-t03/actions/workflows/ci.yml)

## 小組名稱
為什麼初賽在分科前

## 組員姓名
陳品叡, 張御㨒, 利勁鋼, 張永學

## 組員的 GitHub 帳號


| 隊員 | Github帳號 |
|-|-|
|陳品叡|pinruei0323|
|張御㨒|Alec1024-210|
|利勁鋼|okeik|
|張永學|Jordan0811|

## 專案簡介
本專案為「VocaBuddy」英語單字學習小組協作專案。透過 GitHub 與 Google Colab 的結合，實現多人版本控制與共同開發，旨在打造一個輕量、互動且具備隨機測驗功能的英文單字學習輔助工具。

## 組員分工
1. **陳品叡**：建立 GitHub Repository、邀請協作者、建立初始 `VocaBuddy.ipynb` 並新增第一版單字與第一次 Commit。
2. **張御㨒**：寫好gitignore 還有準備好uv 環境、新增考單字的功能
3. **利勁鋼**：新增網頁版單字卡 `index.html`、補上 `.gitattributes`（Lab 1）


## 本次新增的單字與功能
* **新增的單字**：
  * `apple`（蘋果）
  * `orange`（橘子）
  * `banana`（香蕉）
  * *(若有其他組員新增的單字可在此補充)*
* **新增的功能**：
  * 考單字
  * 單字包 CSV 匯入（Lab 10 畢業挑戰）：貼上 `en,zh` 格式的 CSV，即可擴充自訂單字；含格式驗證（欄位缺漏、重複字、BOM、CRLF、引號內逗號），錯誤行逐行回報，合法行照常匯入。

## 📊 Lab 進度總覽表

| Lab | 主題 | 狀態 | 對應檔案 | 備註 |
|-----|------|------|----------|------|
| Lab 1 | 第一次提交：可翻面單字卡 | ✅ 已完成 | `index.html` | 可翻面卡片、8 個單字，首次 commit 已推上 GitHub |
| Lab 2 | 分支、PR 與衝突解決 | ✅ 已完成 | `index.html` | 「考我」隨機抽卡功能，GitHub Flow 已走完 |
| Lab 3 | 例句生成 CLI（Python） | ✅ 已完成 | `tools/gen_example.py` | 呼叫 Claude API 產生例句，API key 從環境變數讀取 |
| Lab 5 | Sprint 1 MVP：今日複習併列 | ✅ 已完成 | `index.html` | 看卡→回想→翻面→自評→下一張，localStorage 儲存 seen/wrong |
| Lab 6 | Sprint 2：AI 例句上卡片 | ⚠️ 部分完成 | `index.html` | 有 AI 例句按鈕，但目前呼叫本地 Ollama 而非教材要求的 Claude BYOK |
| Lab 7 | Sprint 3：SRS 排程（Leitner） | ✅ 已完成 | `srs.js`、`test_srs.js` | 純函式排程，5 組測試通過 |
| Lab 8 | Sprint 4：弱點出題 + 單字包共編 | ✅ 已完成 | `words.js`、`check_words.js` | 「考我弱點」按鈕，單字包獨立成檔，CI 檢查通過 |
| Lab 9 | Ship It：PWA + CI + 上線 | ⚠️ 部分完成 | `sw.js`、`manifest.json`、`ci.yml` | 有 Service Worker 與 CI，但快取仍為 v1，未加入 csv.js |
| Lab 10 | 畢業挑戰：CSV 匯入 | ✅ 已完成 | `csv.js`、`test_csv.js` | 畢業挑戰已完成，測試皆綠 |
| Lab 11~14 | 代理式編碼工具層 | ❌ 未開始 | － | 缺 `CLAUDE.md`、`.claude/skills/`、`.claude/agents/` |

> 目前分支：`feature/lab10-csv-import`（CSV 匯入已 commit）  
> 主分支：`main`

## 📁 各檔案與 Lab 對應表

| 檔案 | 所屬 Lab | 負責功能 |
|------|----------|----------|
| `index.html` | Lab 1~5（核心） | 單字卡介面、複習迴路、localStorage 學習紀錄 |
| `words.js` | Lab 8 | 單字包（21 字），獨立成檔供全隊共編 |
| `check_words.js` | Lab 8 | 單字包驗證：欄位缺漏、重複字檢查 |
| `srs.js` | Lab 7 | Leitner SRS 純函式排程（間隔 1/2/4/8/16 天） |
| `test_srs.js` | Lab 7 | SRS 單元測試，5 組斷言皆通過 |
| `csv.js` | Lab 10 | CSV 匯入純函式：BOM、CRLF、引號逗號、去重驗證 |
| `test_csv.js` | Lab 10 | CSV 匯入單元測試，9 組斷言皆通過 |
| `sw.js` | Lab 9 | Service Worker 離線快取（目前為 v1，建議升級 v2） |
| `manifest.json` | Lab 9 | PWA 應用程式清單 |
| `ci.yml` | Lab 9 | GitHub Actions CI，每次 push/PR 自動跑測試 |
| `tools/gen_example.py` | Lab 3 | Python 例句生成 CLI |

## ✅ Lab 5（Sprint 1 MVP：今日複習併列）驗收對照

Lab 5 教材要求的五項驗收條件，與本專案目前實作狀態如下：

| # | 教材驗收項目 | 目前狀態 | 說明 |
|---|-------------|---------|------|
| 1 | 打開頁面立即看到第一張卡與「剩 N 張」；答完全部出現「今日完成」 | ✅ 符合 | `index.html` 載入後顯示第一張單字與「今日併列：剩 N 張」；全部答完後顯示「今天沒有到期的卡——明天見！」（已演進為 SRS 版本） |
| 2 | 「忘了」的卡稍後會再出現，直到你答「記得」 | ✅ 符合 | `mark(false)` 時會將該卡 `queue.push(queue.shift())` 排到今天隊尾，直到答「記得」才移除 |
| 3 | 重新整理後，seen/wrong 統計仍在 | ✅ 符合 | 學習紀錄 `log` 儲存在瀏覽器 `localStorage`（鍵名 `vb-log`），重新整理不會消失 |
| 4 | 手機上按鈕大小、字級可正常操作 | ✅ 符合 | CSS 中按鈕有固定 padding 與 font-size，卡片字級 32px，可在手機瀏覽器操作 |
| 5 | PR 已合併、tag `sprint1-done` 已推上 GitHub | ⚠️ 程式碼已完成，tag 尚未建立 | 核心功能已實作，但尚未在 git 上建立 `sprint1-done` tag |

> 💡 注意：目前的 `index.html` 已經是包含 Lab 6~10 功能的完整版（AI 例句、SRS 排程、弱點出題、CSV 匯入、PWA），Lab 5 的核心複習迴路皆已包含在內並可正常運作。

## 🧪 如何驗證（在專案根目錄執行）

```bash
# 1. 檢查單字包是否正確（Lab 8）
node check_words.js

# 2. 檢查 SRS 排程測試（Lab 7）
node test_srs.js

# 3. 檢查 CSV 匯入測試（Lab 10）
node test_csv.js

# 4. 網頁版單字卡（Lab 1~5）
# 直接用瀏覽器打開 index.html 即可，不需安裝任何套件
```

## ⚠️ 目前已知缺口與下一步

1. **Lab 9 `sw.js` 快取版本過舊**：目前為 `v1`，`SHELL` 中未包含 `csv.js`，建議升級為 `v2` 並加入 `csv.js`、`icon.png`。
2. **Lab 6 AI 來源**：目前呼叫本地 Olloma，教材要求為瀏覽器直呼 Claude API（使用者自帶金鑰 BYOK），視課程要求決定是否切換。
3. **Lab 11~14 未開始**：缺 `CLAUDE.md`（專案指示檔）、`.claude/skills/add-words/`、` .claude/agents/code-reviewer/`。

---


## Google Colab 開啟連結
[點此透過 Google Colab 開啟 VocaBuddy.ipynb](https://colab.research.google.com/drive/1siUD3jBBmxax0lo0m6Y_vkS6j4Xnv1kj?usp=sharing)

## 程式執行方式
### 網頁版單字卡
直接用瀏覽器打開 `index.html`：點卡片翻面看中文，點「下一張」換單字。

> AI 例句功能：目前呼叫本地 Olloma（模型 `qwen3.5:9b`）。若要使用 AI 例句，請先啟動 Olloma 並拉取模型：`ollama pull qwen3.5:9b`，再開啟 `http://localhost:8000/` 使用。若未啟動 Olloma，AI 例句會顯示「AI 暫時不可用」，但不影響單字卡複習流程。

### CSV 單字包匯入
在 `index.html` 的匯入區塊貼上 `en,zh` 格式的 CSV 文字（例如 `apple,蘋果`），即可將單字加入複習併列。支援 BOM、CRLF、引號內逗號（例如 `"give up","放棄；投降, 認輸"`）；錯誤行會以紅字逐行說明原因，不影響其他合法行匯入。匯入後重新整理仍在，並會進入複習與弱點出題。

### Colab 筆記本
1. 點擊上方提供的 **Google Colab 開啟連結** 進入筆記本。
2. 點選 Google Colab 上方選單的 **「執行階段」**。
3. 點選 **「全部執行」**，即可依序載入單字庫並執行各項單字查詢與測驗功能。

## 使用技術
* 網頁版：HTML / CSS / JavaScript（單一 `index.html`，不需安裝任何套件）
* 筆記本：Python、Google Colab、uv
