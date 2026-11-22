// Offline support: network-first for the app files so updates show up, cache fallback when offline.
const CACHE = "apq-v8";
const FILES = ["./", "index.html", "questions.json", "manifest.webmanifest", "icon.svg", "icon-180.png", "icon-512.png", "img/skull.jpg", "img/spine.jpg", "img/girdle.jpg", "img/scapula.jpg", "img/humerus.jpg", "img/forearm.jpg", "img/hand.jpg", "img/pelvis.jpg", "img/femur.jpg", "img/leg.jpg", "img/foot.jpg", "story.html", "stories/index.json"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res.status === 200) {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy));
      }
      return res;
    }).catch(() => caches.match(e.request).then(r => r || caches.match("index.html")))
  );
});
