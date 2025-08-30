# 📚 Practical OSINT Handbook – Table of Contents

This repository contains improved and fully detailed Markdown documentation for OSINT operations, tools, and environments. Each document is designed for professionals with a technical background, such as computer science graduates or infosec practitioners entering the OSINT field.

---

## ⚙️ 1. Environment Setup  

### 1.1 [Kali VirtualBox Setup](kali-osint-virtualbox-setup.md)  
**Description:**  
Step-by-step instructions to install Kali Linux inside VirtualBox, configure the system for OSINT work, optimize browser hygiene, set up VPN, and take snapshots for reproducible environments.  

**Key Sections:**  
- Install VirtualBox and Kali Linux  
- Post-install setup and tool automation  
- Installing Guest Additions  
- Browser configuration for OSINT  
- Installing and configuring NordVPN  
- Snapshot and clean profile best practices  

---

### 1.2 [Resize Your VM](resize-kali-vm.md)  
**Description:**  
Complete guide to expanding the virtual hard disk size of a Kali Linux VM and resizing partitions within the guest system using GParted.  

**Key Sections:**  
- Resize `.vdi` file using VBoxManage on Windows  
- Install and use GParted inside Kali  
- Confirming expanded disk space  

---

### 1.3 [Tails vs. Kali](OSINT_Environment_Kali_vs_Tails.md)  
**Description:**  
Comparative guide analyzing the use cases, pros, and cons of Tails vs. Kali Linux for OSINT tasks, along with operational security recommendations.  

**Key Sections:**  
- Tails: anonymity-first investigations  
- Kali: tool-rich investigations  
- Threat modeling and OpSec best practices  
- General legal/ethical guidance  

---

## 🔧 2. Core Tools & Techniques  

### 2.1 [Google Dorking for OSINT](google_dork_osint.md)  
**Description:**  
Comprehensive tutorial and cheat sheet on Google Dorking, including operator syntax, filters, and OSINT-specific search tricks for identifying public information across the web.  

**Key Sections:**  
- Face-only image search tricks  
- Google Dork operator examples (site:, filetype:, intitle:, etc.)  
- Search templates for documents, backups, exposed directories  
- Wildcarding and combining filters for precise queries  

---

### 2.2 [theHarvester OSINT Guide](theHarvester_OSINT_Guide.md)  
**Description:**  
In-depth reference manual for using theHarvester for passive reconnaissance. Includes advanced command syntax, use cases, and integration with custom wordlists and external APIs.  

**Key Sections:**  
- Basic usage and help commands  
- 30+ annotated command templates  
- Screenshot capture, output formats, DNS options  
- Wordlist management and batch scanning tips  

---

### 2.3 [Free OSINT Tools List](Free_OSINT_Tools_List.md)  
**Description:**  
A curated directory of completely free and open-source OSINT tools across multiple domains—general reconnaissance, subdomain discovery, phone/email tracking, image metadata, dark web crawling, and username verification.  

**Key Sections:**  
- Categorized tool list: General, Specific, Social Media, Metadata  
- GitHub and official site links for each tool  
- Tools with no paid tiers or usage restrictions  
- Includes Amass, IntelOwl, ExifTool, OnionScan, and more  

---
### 2.4 [Unique Search Operators in Bing & Yandex](Unique_SOperators_Bing_Yandex.md)  
**Description:**  
Reference guide to search operators exclusive to Bing and Yandex that can uncover content Google misses.  

**Key Sections:**  
- Bing-exclusive operators (ip:, hasfeed:, linkfromdomain:, etc.)  
- Yandex-exclusive operators (rhost:, mime:, proximity search, etc.)  
- Practical examples for OSINT workflows  
- When to pivot from Google to alternative engines  

---

## 🧪 3. Real-World OSINT Use Cases  

### 3.1 [OSINT Website Monitoring & Security Checks](website_monitoring.md)  
**Description:**  
Guide to monitoring domains for uptime, blacklisting, changes, backlinks, and malware. Includes tools like UptimeRobot, Visualping, Ahrefs, and VirusTotal.  

**Key Sections:**  
- Uptime & blacklist monitoring  
- Website content change detection  
- Backlink discovery & analysis  
- Malware and suspicious activity checks  

---

### 3.2 [OSINT Email Forensics & Spoofing Analysis](Email_Forensic_Investigation.md)  
**Description:**  
Step-by-step forensic methodology for investigating emails: uncovering spoofed senders, analyzing headers, and verifying SPF/DKIM/DMARC.  

**Key Sections:**  
- Spoofing and phishing kit analysis  
- Header and routing analysis  
- Sender authentication checks  
- Content and attachment forensics  

---

### 3.3 [Advanced Wireless OSINT: Wi-Fi & Bluetooth Investigations](advanced_wireless_osint.md)  
**Description:**  
Comprehensive workflow for leveraging wireless signals (Wi-Fi, Bluetooth) in OSINT. Captures probe requests, builds behavioral profiles, and uses WiGLE.net for geolocation.  

**Quick Navigation:**  
- [Foundational Concepts](advanced_wireless_osint.md#-foundational-concepts-and-theoretical-background)  
- [Tools of the Trade](advanced_wireless_osint.md#-tools-of-the-trade)  
- [Step-by-Step OSINT Workflow](advanced_wireless_osint.md#-step-by-step-osint-workflow)  
- [Advanced Techniques & Real-World Scenarios](advanced_wireless_osint.md#-advanced-techniques-and-real-world-scenarios)  
- [Defenses & Limitations](advanced_wireless_osint.md#-defenses-limitations-and-advanced-techniques)  
- [Troubleshooting & Compatibility](advanced_wireless_osint.md#-troubleshooting)  

---

### 3.4 [Burner Accounts](Burner_Accounts.md)  
**Description:**  
A comprehensive chapter on creating and operating burner identities, including temporary communication tools, sock puppets, secure email practices, and monitoring leak-sharing ecosystems.  

**Key Sections (with side navigation enabled):**  
- Part I: Temporary communication tools (emails, VoIP/SMS, international options)  
- Part II: Sock puppet accounts and compartmented identities  
- Part III: Secure email creation and OpSec best practices  
- Part IV: Leak monitoring and content-sharing ecosystems  
- Part V: End-to-end burner account workflow and lifecycle management  

---

# ✅ Final Notes  

This handbook is divided into three layers:  

1. **Environment Setup** – build and secure your investigative workstation  
2. **Core Tools** – learn the essential reconnaissance and OSINT utilities  
3. **Applied Use Cases** – practice real-world scenarios and workflows  

Together, these chapters form a **comprehensive OSINT training resource**, moving from technical setup to actionable investigations.  
