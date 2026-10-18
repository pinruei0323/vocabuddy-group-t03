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

## Google Colab 開啟連結
[點此透過 Google Colab 開啟 VocaBuddy.ipynb](https://colab.research.google.com/drive/1siUD3jBBmxax0lo0m6Y_vkS6j4Xnv1kj?usp=sharing)

## 程式執行方式
### 網頁版單字卡
在專案資料夾啟動本機伺服器，再用瀏覽器打開 http://localhost:8000：

```bash
python -m http.server 8000
```

不要直接點兩下 `index.html`（`file://`）：AI 例句與「考我弱點」要呼叫本機 Ollama，而 Ollama 會擋下 `file://` 來的請求；PWA 的 service worker 也只在 http(s) 下運作。AI 功能需要先安裝 [Ollama](https://ollama.com) 並執行 `ollama pull qwen3.5:4b`；沒有的話背單字照常可用。

### Python 工具（例句生成 CLI）
套件用 [uv](https://docs.astral.sh/uv/) 管理，記錄在 `pyproject.toml` 與 `uv.lock`。拉下專案後裝好一模一樣的套件：

```bash
uv sync
```

執行（`--provider` 可選 `claude`、`local`、`auto`）：

```bash
uv run python tools/gen_example.py interval --provider local
```

新增套件請用 `uv add 套件名稱`，不要用 `pip install`，這樣其他人 `uv sync` 才會裝到。

### Colab 筆記本
1. 點擊上方提供的 **Google Colab 開啟連結** 進入筆記本。
2. 點選 Google Colab 上方選單的 **「執行階段」**。
3. 點選 **「全部執行」**，即可依序載入單字庫並執行各項單字查詢與測驗功能。

## 使用技術
* 網頁版：HTML / CSS / JavaScript、PWA、本機 Ollama（qwen3.5:4b）
* Python 工具：anthropic、requests（uv 管理）
* 筆記本：Python、Google Colab
* CI：GitHub Actions（`node test_srs.js`、`node check_words.js`）
