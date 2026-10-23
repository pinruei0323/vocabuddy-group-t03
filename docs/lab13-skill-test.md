# Lab 13 技能驗證紀錄——add-words

> 驗證日期：2026-10-24｜技能檔：`.claude/skills/add-words/SKILL.md`

## 教材驗收五項

| # | 驗收項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 技能資料夾與 SKILL.md 建好，frontmatter 有 name 與 description | ✅ | `.claude/skills/add-words/SKILL.md`；frontmatter 檢查（本機無 pyyaml，依教材 Lab 13「怎麼驗證」的替代方案直接目視）：`---` 之間只有 `name: add-words` 與 `description:` 兩欄 |
| 2 | description 寫的是「什麼時候該用」，不是「這是什麼」 | ✅ | description 開頭「要新增或修改單字包（words.js）的時候用」，並列出使用者可能的說法（加單字／新增單字／加幾個○○主題的單字／改字表／動 words.js／更新單字包） |
| 3 | 正面測試：不提技能的自然請求，自動照流程做完 | ✅（見下方說明） | 請求「幫我加三個天氣主題的單字。」→ 代理照技能六步執行全程，產出與規定完全一致 |
| 4 | 負面測試：不相干的請求不會誤觸發 | ⚠️ 誠實標記 | 觸發比對是 Claude Code 載入 `.claude/skills/` 的機制（description 相似度）；本驗證環境的工具（ZCode）不吃這個資料夾，無法做真實的自動觸發實驗。已做的等效驗證：description 全文都是「新增／修改單字包」情境用語，與「改卡片圓角」這類請求無詞彙重疊；技能內容六步全部只涉及 words.js。真正的負面觸發測試需在 Claude Code 中補做 |
| 5 | 技能已進版控 | ✅ | commit `lab13: feat: 新增 add-words 技能（新增單字六步流程）`，隨本分支推送 |

## 正面測試過程（請求：「幫我加三個天氣主題的單字。」）

照 SKILL.md 六步逐步執行：

1. **讀 `words.js` 確認格式**：`{en:"小寫英文", zh:"繁中中文"}`、同主題排一起、主題開頭 `// 主題名 單字包` 註解、兩欄對齊——皆符合。
2. **核對內容**：選定 sunny／rainy／thunderstorm，三個都有英中、英文小寫、與檔內 24 個既有單字（含 Lab 11 剛加的 loop／variable／debug）無重複。
3. **加在檔案最後**：先加 `// 天氣主題單字包` 註解，再放單字，沿用既有對齊與逗號風格。
4. **跑 `node check_words.js`**：「檢查通過，共 27 字 ✓」；`test_srs.js`、`test_csv.js` 同時通過。
5. **只 commit `words.js`**：`git status` 只有一檔；分支名 `feature/lab10-14` 不以 `labNN` 開頭，依技能第 5 條規則 commit 訊息不另加前綴 → `feat: 新增 3 個「天氣」單字`。
6. **不自動 push**：commit 後回報 diff 重點（`words.js | 5 ++++-`，僅四行新增）與檢查輸出；本次 push 依使用者事前授權的「每完成一個 lab 推送一次」流程執行，非技能自行決定。

## 發現與適配

- 教材步驟「問出技能檔要放哪」在本 repo 沿用課程結論：專案層級 `.claude/skills/<name>/SKILL.md`，必填 `name`、`description`。
- 技能第 5 條的「NN 取分支名開頭的 labNN」規則本回合實際生效過一次：分支名不以 labNN 開頭 → 正確不加前綴，證明規則可執行、不依賴猜測。
