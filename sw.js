const CACHE = "ytp-vocabuddy-v2";     // v2：加入 csv.js（Lab 10 匯入功能離線可用）
const SHELL = ["./", "index.html", "words.js", "srs.js", "csv.js", "manifest.json", "icon.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)));   // 安裝時先存一份
});

self.addEventListener("activate", e => {
  // 啟用新版本時清掉舊快取（如 v1），避免離線時繼續拿到沒有 csv.js 的舊頁面
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request)) // 先問快取，沒有才上網
  );
});
