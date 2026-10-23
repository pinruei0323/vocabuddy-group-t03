# Lab 11 開工準備——驗收紀錄

> 驗證日期：2026-10-24｜驗證者：ZCode 代理（模型 GLM-5.3），受使用者明確授權批次完成 Lab 1~14

## 教材驗收五項

| # | 驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 工具裝好了，終端機回得出版本號 | ✅ | 工具是 ZCode 桌面版（本 session 即工具本体）；環境 `git version 2.54.0 (Apple Git-157)`、`node v26.9.0`（macOS arm64） |
| 2 | 已登入或已設好金鑰，不再跳未認證 | ✅ | session 以使用者帳號建立，全程無未認證提示。App 自己的 API 金鑰另計：CLI 走環境變數、網頁端 BYOK（Lab 6 的「設定 AI 金鑰」按鈕，只存 localStorage） |
| 3 | 在專案資料夾裡啟動，三個問題答對 | ✅ | 工作目錄 `/Users/zhangyongxue/Project/vocabuddy-group-t03`（repo 根），答案見下方 |
| 4 | 知道自己現在在哪一種操作模式 | ✅ | 本 session 在使用者明確授權下批次執行（對應教材「自動接受」）；Lab 11 要求的逐步確認以三重證據落實：commit 前 `git diff` 只有 words.js 四行、`check_words.js` 24 字通過、瀏覽器乾淨載入 24 張，證據齊了才提交（見下） |
| 5 | 完成一次小改動，且用 git diff 與瀏覽器驗過才提交 | ✅ | commit「lab11: feat: 新增 3 個演算法主題單字」：`words.js` 加 loop／variable／debug。提交前 `git diff --stat` 只動一檔；`node check_words.js` → 24 字 ✓；瀏覽器（無快取的乾淨 scope `http://127.0.0.1:8642/vb24/`）載入 → 「今日佇列：剩 24 張」、三個新字均出現且中文正確 |

## 三個驗證問題（只根據倉庫檔案回答）

**1. 這個專案是做什麼的？**

英語單字學習 PWA「YTP VocaBuddy（Pro 2.0）」（`README.md`）：可翻面單字卡、今日複習佇列（Leitner SRS 排程）、AI 例句與弱點出題（有 Claude 金鑰走 BYOK 直呼，否則退回團隊 Ollama）、CSV 匯入自訂單字包、Service Worker 離線可用。App 本體在 repo 根目錄（`index.html`＋`words.js`＋`srs.js`＋`csv.js`＋`sw.js`）；`labs/` 是課程教材的完成版參考（一個 Lab 一個資料夾），不屬於 App 本體。

**2. 列出所有檔案，並說明每個檔案負責什麼。**（`git ls-files` 共 92 個，labs/ 佔 69 個）

| 路徑 | 負責什麼 |
|---|---|
| `index.html` | 介面與所有接 DOM 的程式：卡片、佇列、AI 例句、弱點出題、CSV 匯入、金鑰設定 |
| `words.js` | 單字包（全隊共編，進 Git），24 字 |
| `srs.js`／`csv.js` | 純函式：SRS 排程／CSV 解析與驗證（Node 可直接測） |
| `test_srs.js`／`test_csv.js`／`check_words.js` | 單元測試與單字包資料檢查（CI 也跑） |
| `sw.js`＋`manifest.json`＋`icon.png` | PWA 三件套（快取 v2 含 csv.js） |
| `tools/gen_example.py` | 例句生成 CLI（金鑰從環境變數讀，支援多本機模型） |
| `.github/workflows/ci.yml` | CI：每個 PR 跑三個檢查 |
| `CLAUDE.md` | 專案指示檔（Lab 12） |
| `.claude/skills/add-words/`、`.claude/agents/code-reviewer.md` | 技能與子代理（Lab 13／14） |
| `pyproject.toml`＋`uv.lock` | Python 端套件管理（例句 CLI 的依賴） |
| `readme-2.md`／`readme-3.md` | 歷史版 README 存檔 |
| `labs/lab01~lab14` | 課程教材完成版參考（69 檔，唯讀對照用） |

**3. 單字資料（WORDS）放在哪？結構？幾個字？**

放在獨立檔案 `words.js:2`（Sprint 4 起從 `index.html` 抽出，`index.html` 以 `<script src="words.js">` 載入，本身不含單字資料——對照教材勘誤 E-027）。結構是物件陣列 `{en:"小寫英文", zh:"繁中中文"}`，主題之間以 `// 主題名 單字包` 註解分隔。Lab 11 改動前 21 字、改動後 24 字（loop＝迴圈、variable＝變數、debug＝除錯）。

## 操作模式對照（教材三模式 ↔ 本工具）

| 教材模式 | 說明 | ZCode 對應 |
|---|---|---|
| 逐步確認 | 每個寫檔與指令都問 | permission mode（每步彈出核准） |
| 先計畫再做 | 先出計畫，同意才動手 | plan mode（EnterPlanMode／ExitPlanMode） |
| 自動接受 | 不逐一詢問 | auto／yolo |

本 session：使用者指示「直接把 lab1~lab14 全部做完，每完成一個 lab 就 push」＝授權下的自動接受；Lab 11 的逐步確認精神以「diff＋測試＋瀏覽器」三重證據落實後才 commit。
