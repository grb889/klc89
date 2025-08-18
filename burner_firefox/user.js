// --- Privacy and Fingerprinting Protection ---
user_pref("media.peerconnection.enabled", false); // WebRTC
user_pref("geo.enabled", false);
user_pref("dom.battery.enabled", false);
user_pref("dom.gamepad.enabled", false);
user_pref("device.sensors.enabled", false);
user_pref("webgl.disabled", true);
user_pref("dom.webnotifications.enabled", false);
user_pref("dom.push.enabled", false);
user_pref("beacon.enabled", false);

user_pref("privacy.resistFingerprinting", true);
user_pref("privacy.resistFingerprinting.letterboxing", true);
user_pref("privacy.resistFingerprinting.block_mozAddonManager", true);

user_pref("canvas.poisondata", true);
user_pref("canvas.poisondata.enable", true);
user_pref("canvas.capturestream.enabled", false);
user_pref("dom.webaudio.enabled", false);

user_pref("network.http.referer.XOriginTrimmingPolicy", 2);
user_pref("network.http.referer.XOriginPolicy", 2);
user_pref("network.dns.disablePrefetch", true);
user_pref("network.prefetch-next", false);
user_pref("network.predictor.enabled", false);

user_pref("browser.formfill.enable", false);
user_pref("network.cookie.cookieBehavior", 5);
user_pref("privacy.partition.network_state.ocsp_cache", true);

// --- DNS over HTTPS ---
user_pref("network.trr.mode", 2);
user_pref("network.trr.uri", "https://mozilla.cloudflare-dns.com/dns-query");

// --- UI & Session Behavior ---
user_pref("browser.startup.page", 0);
user_pref("signon.rememberSignons", false);
user_pref("browser.sessionstore.privacy_level", 2);
user_pref("browser.download.manager.addToRecentDocs", false);
