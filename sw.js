const CACHE = "ytp-vocabuddy-v6";     // v6：安裝時繞過 HTTP 快取逐檔抓（修 v5 裝到舊 words.js 的問題）
const SHELL = ["./", "index.html", "words.js", "srs.js", "csv.js", "manifest.json", "icon.png"];

self.addEventListener("install", e => {
  // 新版不等所有分頁關閉就接手；頁面收到通知後彈「有新版本」，重載時機由人決定
  self.skipWaiting();
  // cache:"reload" 繞過瀏覽器 HTTP 快取逐檔抓，避免「新版 SW 裝了舊檔」的混合快取
  e.waitUntil(caches.open(CACHE).then(c =>
    Promise.all(SHELL.map(u => c.add(new Request(u, { cache: "reload" }))))
  ));
});

self.addEventListener("activate", e => {
  // 清掉舊快取（如 v2）→ 接手既有分頁 → 主動通知頁面「新版已上線」
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
    const wins = await self.clients.matchAll({ type: "window" });
    wins.forEach(c => c.postMessage({ type: "vb-activated" }));
  })());
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request)) // 先問快取，沒有才上網
  );
});
