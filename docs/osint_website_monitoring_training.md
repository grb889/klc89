
# OSINT Training Guide: Website Monitoring

This guide is designed to train analysts and researchers in monitoring websites for uptime, changes, backlinks, and security using open-source tools. These skills are essential in identifying potential indicators of compromise, new partnerships, or suspicious behavior across monitored domains.
Credit to CavemenTech Youtube [video](https://www.youtube.com/watch?v=UHaCwQkcit8) Never Miss a Clue: The Ultimate Guide to Website Monitoring (OSINT & Security)

---

## 🟢 Uptime Monitoring & Blacklist Checks

Monitoring whether a website is live or has been blacklisted can provide critical early warnings in OSINT investigations.

### 🔧 Tools:
- [HetrixTools](https://hetrixtools.com/)
- [UptimeRobot](https://uptimerobot.com/)

### 📘 Instructions:

#### **HetrixTools**
1. Sign up for a free account.
2. Go to `Monitors > Add Monitor`.
3. Enter the domain or IP, set the monitoring interval, and choose protocols (HTTP, HTTPS, PING).
4. Use the **Blacklist Monitor** to check if the domain or IP appears in any major blacklists.

#### **UptimeRobot**
1. Create an account at [uptimerobot.com](https://uptimerobot.com).
2. Click `Add New Monitor`.
3. Select "HTTP(s)" as the type, input the website URL, and configure monitoring intervals.
4. Enable email or SMS alerts to be notified when the website is down.

### ✅ OSINT Tip:
Tracking availability over time helps determine patterns of takedowns or malicious behavior.

---

## 📰 Website Change Detection

Stay informed about content updates, product releases, legal disclaimers, or removals on targeted websites.

### 🔧 Tools:
- [Visualping](https://visualping.io/)
- [Distill.io](https://distill.io/)

### 📘 Instructions:

#### **Visualping**
1. Navigate to [visualping.io](https://visualping.io).
2. Paste the target website URL.
3. Select the area of the page to monitor (optional).
4. Choose check frequency and alert method (email, Slack, etc.).
5. Visualping will notify you of any visual or content change.

#### **Distill.io**
1. Install the [Distill.io browser extension](https://distill.io/resources).
2. Visit the target webpage.
3. Click the extension > Select parts of the page you want to monitor.
4. Configure the check interval and notification settings.

### ✅ OSINT Tip:
Monitor "Terms of Service," "Contact," or "Press Release" pages to detect organizational changes.

---

## 🔗 Backlink Monitoring & Analysis

Backlinks can reveal business relationships, third-party support, affiliate programs, or unexpected external references.

### 🔧 Tool:
- [Ahrefs Free Backlink Checker](https://ahrefs.com/backlink-checker)

### 📘 Instructions:

1. Go to [ahrefs.com/backlink-checker](https://ahrefs.com/backlink-checker).
2. Enter the domain or specific URL.
3. Review:
   - Referring domains
   - Top backlinks
   - Anchor texts
4. Export data if needed.

### ✅ OSINT Tip:
New backlinks can indicate media coverage, partnerships, or disinformation campaigns.

---

## 🛡️ Malware & Security Scanning

Detect malware, phishing activity, or suspicious behavior linked to a website.

### 🔧 Tools:
- [VirusTotal](https://www.virustotal.com/)
- [URLScan.io](https://urlscan.io/)

### 📘 Instructions:

#### **VirusTotal**
1. Visit [virustotal.com](https://www.virustotal.com/).
2. Paste the domain or URL.
3. Analyze results from multiple antivirus engines and reputation checkers.
4. Review detailed results under the "Details" and "Community" tabs.

#### **URLScan.io**
1. Go to [urlscan.io](https://urlscan.io/).
2. Enter the URL and click `Public Scan`.
3. Analyze:
   - Page content
   - Linked domains
   - Hosting and tracking details
   - Embedded scripts and behaviors

### ✅ OSINT Tip:
Use both tools to compare outputs and validate threat intelligence reports or suspicions.

---

## 🧠 Final Notes

- Use alerts to automate monitoring without needing to manually revisit each site.
- Combine all findings into your investigation or reporting workflow.
- Always ensure ethical and legal compliance when monitoring websites, especially private or login-gated pages.

---

**Next Step:** Integrate these tools into a case study or red team/blue team simulation.
