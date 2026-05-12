const CACHE_NAME = 'masthi-updates-v1';
const ASSETS = [
    '/',
    '/static/manifest.json',
    '/static/images/logo.png'
];

self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(ASSETS).catch(() => {});
        })
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(self.clients.claim());
    // Cleanup old caches
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            );
        })
    );
});

// Fetch strategy: Network first, falling back to cache
self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    
    // Don't cache API or dynamic routes aggressively if not needed
    if (event.request.url.includes('/latest-post/') || event.request.url.includes('/save-subscription/')) {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then(response => {
                const responseClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, responseClone).catch(() => {});
                });
                return response;
            })
            .catch(() => caches.match(event.request))
    );
});

// Periodic notification check mechanism triggered by client communication
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'CHECK_LATEST_POST') {
        checkLatestPost();
    }
});

let lastNotifiedPostId = null;

async function checkLatestPost() {
    try {
        const res = await fetch('/latest-post/');
        const data = await res.json();
        if (data && data.success && data.id) {
            // Check if we already notified for this post
            if (lastNotifiedPostId !== data.id) {
                lastNotifiedPostId = data.id;
                
                // Show notification if permissions granted
                if (self.registration && self.registration.showNotification) {
                    await self.registration.showNotification(data.title, {
                        body: data.short_description || 'Tap to read the latest update on Masthi Updates!',
                        icon: '/static/images/logo.png',
                        image: data.feature_image || null,
                        badge: '/static/images/logo.png',
                        data: { url: `/blogs/${data.slug}/` },
                        vibrate: [200, 100, 200]
                    });
                }
            }
        }
    } catch (e) {
        console.error('Service Worker: Error checking latest post', e);
    }
}

// Support actual Web Push events
self.addEventListener('push', event => {
    let title = 'New on Masthi Updates!';
    let options = {
        body: 'Fresh movie news and updates have just been published.',
        icon: '/static/images/logo.png',
        badge: '/static/images/logo.png',
        vibrate: [200, 100, 200],
        data: { url: '/' }
    };

    if (event.data) {
        try {
            const payload = event.data.json();
            title = payload.title || title;
            options.body = payload.body || options.body;
            if (payload.image) options.image = payload.image;
            if (payload.url) options.data.url = payload.url;
        } catch (e) {
            options.body = event.data.text();
        }
    }

    event.waitUntil(self.registration.showNotification(title, options));
});

// Handle click on notification
self.addEventListener('notificationclick', event => {
    event.notification.close();
    const targetUrl = (event.notification.data && event.notification.data.url) ? event.notification.data.url : '/';
    
    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then(windowClients => {
            // Check if there is already a window/tab open with the target URL
            for (let client of windowClients) {
                if (client.url.includes(targetUrl) && 'focus' in client) {
                    return client.focus();
                }
            }
            // If not, open a new window/client
            if (clients.openWindow) {
                return clients.openWindow(targetUrl);
            }
        })
    );
});
