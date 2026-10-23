// words.js —— 單字包：全隊共編，進 Git
const WORDS = [
  {en:"apple", zh:"蘋果"},         {en:"orange", zh:"橘子"},
  {en:"banana", zh:"香蕉"},
  {en:"algorithm", zh:"演算法"},   {en:"recursion", zh:"遞迴"},
  {en:"vocabulary", zh:"字彙"},    {en:"memorize", zh:"背誦"},
  {en:"efficient", zh:"有效率的"}, {en:"persist", zh:"堅持；持續"},
  {en:"retrieve", zh:"取回；檢索"},{en:"interval", zh:"間隔"},
  // 動物主題單字包
  {en:"elephant", zh:"大象"},      {en:"giraffe", zh:"長頸鹿"},
  {en:"dolphin", zh:"海豚"},       {en:"penguin", zh:"企鵝"},
  {en:"squirrel", zh:"松鼠"},      {en:"turtle", zh:"烏龜"},
  {en:"kangaroo", zh:"袋鼠"},      {en:"octopus", zh:"章魚"},
  {en:"butterfly", zh:"蝴蝶"},     {en:"leopard", zh:"花豹"},
  // 演算法主題單字包（Lab 11 小改動）
  {en:"loop", zh:"迴圈"},          {en:"variable", zh:"變數"},
  {en:"debug", zh:"除錯"},
  // 天氣主題單字包
  {en:"sunny", zh:"晴朗的"},        {en:"rainy", zh:"下雨的"},
  {en:"thunderstorm", zh:"雷暴"}
];
if (typeof module !== "undefined") module.exports = WORDS;
