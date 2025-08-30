
# 📚 Google Dorking for OSINT

**Google Dorking** (also known as Google hacking) refers to using advanced search operators in Google to find specific, often hidden, pieces of information. It's a powerful and beginner-friendly OSINT technique used by cybersecurity professionals, journalists, and investigators.

---

## 🔍 What Is Google Dorking?

Google Dorking leverages the way Google indexes web content. By combining search terms with advanced operators, you can:

- Discover publicly exposed files
- Search within a specific domain
- Find login portals
- Identify vulnerable pages or misconfigurations
- Locate public documents, images, or directories

> ⚠️ **Ethical Reminder:** Use Google Dorking responsibly. Only access information that is publicly available and not protected by authentication or privacy settings.

---

## 🧠 Example Use Case: Find Only Face Images of a Person

This trick lets you refine Google Images to only show **face-type** images:

### Step-by-step:

1. **Search the name using quotes** for accuracy:
   ```
   "Elon Musk"
   ```

2. **Click on the 'Images' tab** on Google.

3. Click on:
   ```
   Tools → Type → Clipart
   ```

4. In the **URL**, find this parameter:
   ```
   tbs=itp:clipart
   ```

5. **Replace** `itp:clipart` with `itp:face`

6. Press Enter.

### ✅ Result:

Only face images of the target (e.g., Elon Musk) will be displayed.

### Example:

- Original:
  ```
  https://www.google.com/search?q="Elon+Musk"&...&tbs=itp:clipart
  ```

- Modified:
  ```
  https://www.google.com/search?q="Elon+Musk"&...&tbs=itp:face
  ```

---

## 🛠️ Core Google Dork Operators

| **Use Case** | **Operator** | **Example** |
|--------------|--------------|-------------|
| Search within a specific domain | `site:` | `site:nytimes.com cybersecurity` |
| Search multiple domains | `OR` | `"John Doe" site:facebook.com OR site:twitter.com` |
| Find specific file types | `filetype:` | `filetype:pdf machine learning` |
| Keywords in page title | `intitle:` | `intitle:"data privacy"` |
| All keywords in title | `allintitle:` | `allintitle:"cybersecurity law"` |
| Keywords in page text | `intext:` | `intext:"cyber threat"` |
| All keywords in text | `allintext:` | `allintext:"malware statistics 2024"` |
| Keywords in URL | `inurl:` | `inurl:"login"` |
| All keywords in URL | `allinurl:` | `allinurl:"admin login panel"` |
| Number ranges | `numrange:` | `numrange:2010-2020` |
| Filter by date | `before:` / `after:` | `filetype:pdf before:2020-01-01 after:2018-01-01` |
| Language-specific results | `lang:` | `site:gov.uk lang:en cybersecurity` |
| Wildcard keyword | `*` | `"password * leak"` |
| Related websites | `related:` | `related:bbc.com` |

---

## 🔍 Advanced Dorking Techniques

### 1. Search for Exposed Files in Open Directories
```text
intitle:"index of" "cisco" (pdf | doc | ppt)
```
Finds public folders listing Cisco-related documents.

---

### 2. Locate Documents on Misconfigured File Servers
```text
inurl:"/files/" "cisco" filetype:pdf
```
Targets URLs with `/files/`, a common folder on unsecured servers.

---

### 3. Discover Documents in Backup Folders
```text
inurl:backup "cisco" filetype:pdf
```
Identifies documents stored in backup folders—often overlooked during security audits.

---

### 4. Target Government or Organization Sites
```text
site:.gov "cisco" filetype:pdf
```
Refines results to government domains. You can change `.gov` to `.edu`, `.org`, or country-specific domains like `.fr`, `.de`.

---

### 5.  Multi-parameter search query 1
```text
("Spiderfoot") (intext:tutorial OR intext:"cheat sheet") (filetype:pdf OR filetype:ppt OR filetype:pptx)
```
Each group is in parentheses for clarity.Google treats whitespace as AND by default.

---
### 6.  Multi-parameter search query(2)
```text
"Google Dork" site:github.com (sheet OR list OR query OR advanced OR osint) after:2021-01-01
```
OR — any of these related keywords

---

## 🎯 Practical Tips for Effective Dorking

- Use quotes for **exact phrases**: `"john smith"` instead of `john smith`
- Combine operators for precise results:
  ```text
  site:linkedin.com "@gmail.com" "CTO"
  ```
- Wildcard `*` helps to guess unknown terms:
  ```text
  "CEO of * Corporation"
  ```
- Use `numrange:` to filter by years or values:
  ```text
  cyberattack statistics numrange:2010-2023
  ```

---

## ⚖️ Legal and Ethical Considerations

Google Dorking uses public search data indexed by Google. However:

- Do **not** access pages protected by login or authorization.
- Do **not** attempt to exploit vulnerabilities.
- Use this technique for ethical research, journalism, education, or organizational security testing with permission.

---

## ✅ Summary

Google Dorking is an essential OSINT skill that transforms basic search into a precision reconnaissance tool. By mastering search operators and refining queries, you can uncover valuable data hiding in plain sight.

---

## 📎 Suggested Next Steps

- Practice with safe searches like:
  ```text
  site:gov.uk "cybersecurity"
  intitle:"index of" filetype:pdf
  ```
- Combine this with tools like **SpiderFoot**, **theHarvester**, or **Recon-ng** for automated data extraction.
- Add browser extensions like **Shodan Plugin** to enhance in-browser reconnaissance.

---

###  **AI-Powered and Automated Tools**

* **DorkGPT** — An AI-powered tool that generates Google Dorking queries based on natural language prompts.  
   👉 [https://www.dorkgpt.com/](https://www.dorkgpt.com/?utm_source=chatgpt.com)

* **IntelTechniques Search Tool** — A comprehensive collection of OSINT search tools, including a Google Dork search interface that automates queries across multiple search engines and databases.  
   👉 [https://inteltechniques.com/tools/Search.html](https://inteltechniques.com/tools/Search.html?utm_source=chatgpt.com)

---

🕵️‍♂️ Google Dorks Cheat Sheet for Hidden Paths & Exposed Files
> 📋 *Table adapted from [this GitHub repository](https://github.com/sudosu01/-Google-Dorks-Cheat-Sheet-for-Hidden-Paths-Exposed-Files).*  
> Original author unknown. All credit to the creator.

| **Google Dork** | **What It Finds / Does** |
|------------------|--------------------------|
| `inurl:web.config` | Finds exposed ASP.NET configuration files. May contain DB connection strings, secrets. |
| `intitle:"index of" "web.config"` | Searches for open directory listings containing `web.config`. |
| `inurl:.htaccess` | Finds exposed `.htaccess` files used by Apache (can reveal rules, paths, restrictions). |
| `inurl:.htpasswd` | Looks for Apache password files (used with `.htaccess`). May reveal hashed passwords. |
| `inurl:.env` | Exposes `.env` files—used in Laravel, Node.js, etc. Often includes API keys, DB creds. |
| `ext:bak OR ext:old OR ext:backup inurl:admin` | Finds backup/old files in admin directories (may contain original code/configs). |
| `intitle:"index of" ".git"` | Shows exposed `.git` repositories—can leak full project source code. |
| `intitle:"index of" ".svn"` | Finds exposed Subversion (SVN) version control directories. |
| `filetype:sql "insert into" OR "create table"` | Searches for SQL database dumps, usually from MySQL or PostgreSQL. |
| `filetype:json "mongo" OR "password"` | Finds JSON files with MongoDB configs or other sensitive credentials. |
| `intitle:"index of" "error_log"` | Finds open error log files (can contain paths, errors, user info). |
| `intitle:"phpinfo()" "PHP Version"` | Locates PHP info pages — these expose server config, installed extensions. |
| `intitle:"index of" (config|backup|admin|database)` | Finds open directories with config/backup/admin/database files. |
| `inurl:wp-content/debug.log` | Finds exposed debug logs in WordPress installs — may include stack traces, errors. |

### Sheet List from the web :
  -
         - [hackersonlineclub.com/google-hacking](https://hackersonlineclub.com/google-hacking/)
         - [www.boxpiper.com/posts/google-dork-list](https://www.boxpiper.com/posts/google-dork-list)
         - [www.boxpiper.com/posts/top-35-google-dorks-list](https://www.boxpiper.com/posts/top-35-google-dorks-list)