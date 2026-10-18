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

## Google Colab 開啟連結
[點此透過 Google Colab 開啟 VocaBuddy.ipynb](https://colab.research.google.com/drive/1siUD3jBBmxax0lo0m6Y_vkS6j4Xnv1kj?usp=sharing)

## 程式執行方式
### 網頁版單字卡
直接用瀏覽器打開 `index.html`：點卡片翻面看中文，點「下一張」換單字。

### CSV 單字包匯入
在 `index.html` 的匯入區塊貼上 `en,zh` 格式的 CSV 文字（例如 `apple,蘋果`），即可將單字加入複習併列。支援 BOM、CRLF、引號內逗號（例如 `"give up","放棄；投降, 認輸"`）；錯誤行會以紅字逐行說明原因，不影響其他合法行匯入。匯入後重新整理仍在，並會進入複習與弱點出題。

### Colab 筆記本
1. 點擊上方提供的 **Google Colab 開啟連結** 進入筆記本。
2. 點選 Google Colab 上方選單的 **「執行階段」**。
3. 點選 **「全部執行」**，即可依序載入單字庫並執行各項單字查詢與測驗功能。

## 使用技術
* 網頁版：HTML / CSS / JavaScript（單一 `index.html`，不需安裝任何套件）
* 筆記本：Python、Google Colab、uv
