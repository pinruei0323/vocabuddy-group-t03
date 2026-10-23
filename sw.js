const CACHE = "ytp-vocabuddy-v3";     // v3：加入更新提示（skipWaiting＋activate 通知頁面）
const SHELL = ["./", "index.html", "words.js", "srs.js", "csv.js", "manifest.json", "icon.png"];

self.addEventListener("install", e => {
  // 新版不等所有分頁關閉就接手；頁面收到通知後彈「有新版本」，重載時機由人決定
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)));   // 安裝時先存一份
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
