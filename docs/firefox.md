
# Firefox Configuration for OSINT Investigations (Kali Linux – VirtualBox)

## 🎯 Goal
To establish a hardened, compartmentalized, and anonymous browser setup for OSINT operations using:

- **Firefox ESR profiles** (full separation of investigations)
- **Multi-Account Containers** (per-tab compartmentalization)
- **Arkenfox-based hardening** (`user.js`)
- **Scripted automation** for burner-profile creation

## 🧱 1. Understanding Firefox Profiles

### 🔍 What is a Profile?
A **Firefox profile** is a self-contained environment that stores:

- Browsing history, cache, cookies
- Bookmarks and session info
- Installed extensions
- `about:config` settings

### 📦 OSINT Usage
Each **investigation target** should get its own Firefox profile. This avoids:

- Cross-contamination of cookies, storage, fingerprinting trails
- Session or login leakage between targets
- Correlating traffic from Target A and Target B

**Best Practice:** 1 Profile = 1 Target

### 🔧 Linux Commands

```bash
# Create a profile
firefox-esr -CreateProfile "target-a"

# List profiles
cat ~/.mozilla/firefox/profiles.ini

# Delete a profile manually
rm -rf ~/.mozilla/firefox/*.target-a/

# Launch a specific profile
firefox-esr -P "target-a"
```

## 🧩 2. Multi-Account Containers (MAC)

### 🔐 What are Containers?
Containers allow tab-level isolation *within a single profile*:

- Separate cookies, local storage, sessions
- Maintain multiple identities on the same site
- Reduce risk of cross-site tracking

### 🕵️ OSINT Application
Use containers **within an investigation profile** to separate workflows:

| Profile       | Container                 | Use Case            |
|---------------|---------------------------|----------------------|
| `target-a`    | `target-a-social`         | Log into Twitter     |
| `target-a`    | `target-a-research`       | Scrape open forums   |
| `target-a`    | `target-a-search`         | General browsing     |

**Best Practice:** 1 Profile → Multiple Containers (per investigation type)

### 🔧 Setup Notes

- The **Multi-Account Containers extension** can be pre-installed via `policies.json`.
- But **domain-to-container bindings must be set manually**.
- Containers do **not sync** between profiles.

## 🔐 3. Arkenfox User.js Hardening

### 🧬 Purpose
Arkenfox is a privacy-hardening configuration applied via a `user.js` file in each Firefox profile. It overrides `about:config` to:

- Disable tracking APIs
- Prevent fingerprinting
- Stop telemetry and WebRTC leaks

### ⚙️ OSINT-Optimized `user.js` (Place in each profile dir)

```js
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
```

## ⚙️ 4. Burner Profile Creation Script

### 🔄 `burner_firefox.sh`

```bash
#!/bin/bash

# === CONFIGURATION ===
PROFILE_NAME="burner-$(date +%s)"
FIREFOX_CMD=$(which firefox)

# Check if Firefox is installed
if [ -z "$FIREFOX_CMD" ]; then
  echo "❌ Firefox is not installed or not in PATH."
  exit 1
fi

echo "🌀 Creating Firefox burner profile: $PROFILE_NAME"
firefox -CreateProfile "$PROFILE_NAME"

# Find profile folder
PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name "*.$PROFILE_NAME" | head -n 1)

if [ -z "$PROFILE_DIR" ]; then
  echo "❌ Failed to find profile directory."
  exit 1
fi

echo "📁 Profile created at: $PROFILE_DIR"

# Download latest arkenfox user.js
echo "🌐 Downloading hardened user.js from arkenfox..."
curl -sSL https://raw.githubusercontent.com/arkenfox/user.js/master/user.js -o "$PROFILE_DIR/user.js"

# Launch Firefox with that profile
echo "🚀 Launching Firefox with burner profile..."
firefox -no-remote -P "$PROFILE_NAME" &
```

## 🔁 5. Extension Handling (Containers + uBlock etc.)

- Extensions **forced via `policies.json`** are installed into **every profile**, regardless of how it was created.
- Containers extension must be enabled in each profile even if pre-installed.
- Manual extension installs are profile-specific and **do not cross over**.

## 🔚 Final Recommendations

| Task                     | Tool                          |
|--------------------------|-------------------------------|
| Full investigation isolation | **Firefox Profile**             |
| Subtask separation        | **Multi-Account Containers**     |
| Fingerprint & leak defense | **Arkenfox `user.js`**         |
| Fast deployment           | **`burner_firefox.sh` script**  |

Use profiles as **walls between investigations** and containers as **drawers inside each investigation**. Harden each profile with Arkenfox or the lightweight `user.js`.

## 📁 Using `burner_firefox.sh`

This script automates creation of a hardened Firefox profile for OSINT:

### ✅ Requirements
- Firefox must be installed
- Run from any folder on a Linux system

### 🧾 How to Use

1. Unzip the `burner_firefox.zip`:
   ```bash
   unzip burner_firefox.zip
   cd burner_firefox
   ```

2. Make the script executable:
   ```bash
   chmod +x burner_firefox.sh
   ```

3. Run the script:
   ```bash
   ./burner_firefox.sh
   ```

4. Firefox will launch with a hardened profile, using the latest Arkenfox `user.js`.

5. Optional: You can place the included `user.js` manually in any profile folder under `~/.mozilla/firefox/xxxxxxxx.profileName/`.

---
