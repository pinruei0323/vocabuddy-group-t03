# CLAUDE.md —— VocaBuddy 專案指示

## 專案是什麼
英語單字學習 PWA：`index.html` 單頁 App（可翻面單字卡、今日複習佇列、AI 例句、弱點出題、CSV 匯入），搭配 Service Worker 離線可用。`labs/` 是課程教材資料夾，不屬於 App 本體，除非另有說明不要改動。

## 檔案結構
- `index.html`：介面與所有接 DOM 的程式；`words.js` 單字包（全隊共編）；`srs.js`／`csv.js` 純函式（不碰 DOM、不碰 localStorage，Node 可直接測）
- `test_srs.js`／`test_csv.js` 單元測試、`check_words.js` 單字包資料檢查；`sw.js`＋`manifest.json`＋`icon.png` 是 PWA 三件套
- `tools/gen_example.py` 例句生成 CLI（API key 從環境變數讀）

## 程式碼慣例
- 2 空格縮排、雙引號、能用 `const` 就不用 `let`；取 DOM 用 `$("id")`
- 新函式加一行繁中註解，格式固定 `// 用途：…`，說「為什麼」不只說「做什麼」
- localStorage 讀寫一律包 `try/catch`；模型輸出一律當文字（`textContent`／`createElement`），不用 `innerHTML`
- 邏輯可測就抽成純函式放獨立檔，配 `test_*.js`（Node 內建 assert，不裝依賴）

## Git 工作流程
- 每項改動開 issue → `feature/`（或 `labNN/feature/`）分支 → PR 請隊友 review → merge；`main` 只收 PR，不直接 commit
- commit 訊息：`類型: 說明`（feat／fix／docs／test），屬於某個 Lab 時加 `labNN:` 前綴，例如 `lab10: feat: …`
- 不自動 push；push 與 merge 由人決定

## 測試與安全
- 提交前三個檢查都要綠：`node check_words.js`、`node test_srs.js`、`node test_csv.js`（CI 也跑這三個）
- 改到 `index.html` 一定要用瀏覽器完整複習一輪再提交；改 `sw.js` 記得把 `CACHE` 版號 +1
- 金鑰不進 Git：CLI 用環境變數，網頁端 BYOK（金鑰只存使用者自己的 localStorage，如 `vb-claude-key`）；學習紀錄只留本地，不回傳任何伺服器
