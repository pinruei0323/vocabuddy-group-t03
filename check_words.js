const words = require("./words.js");
if (words.length < 2) throw new Error("單字至少要 2 個——抽卡與出題都需要");
const seen = new Set();
for (const w of words){
  if (!w.en || !w.zh) throw new Error("欄位缺漏：" + JSON.stringify(w));
  if (w.en !== w.en.toLowerCase()) throw new Error("en 請統一小寫：" + w.en);
  if (seen.has(w.en.toLowerCase())) throw new Error("重複單字（不分大小寫）：" + w.en);   // 大小寫變體也算重複，攔得住手誤
  seen.add(w.en.toLowerCase());
}
console.log("words.js 檢查通過，共 " + words.length + " 字 ✓");
