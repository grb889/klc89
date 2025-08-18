
# 📡 theHarvester — OSINT Tool for Domain Reconnaissance

`theHarvester` is an open-source OSINT (Open-Source Intelligence) tool designed for gathering emails, subdomains, IPs, and URLs using passive techniques. It's often used during the initial stages of penetration testing or red teaming to build a profile of a target domain.

---

## 🛠️ What Can theHarvester Do?

- Collect data **passively** (no interaction with the target’s infrastructure)
- Enumerate:
  - Subdomains
  - Emails
  - Hosts/IPs
  - Employee names
  - API endpoints
- Sources include:
  - Search engines (Google, Bing, DuckDuckGo, Yahoo)
  - Public repositories (GitHub, Shodan, crt.sh, RAPIDNS)
  - DNS brute-forcing with wordlists
- Output formats: JSON, XML, HTML

---

## ⚙️ Basic Syntax

```bash
theHarvester -d [domain] -b [source] [options]
```

- `-d`: Target domain (e.g. `example.com`)
- `-b`: Data source (e.g. `google`, `bing`, `crtsh`, `all`)
- `-l`: Result limit
- `-f`: Save results to a file
- `-w`: Wordlist file for brute-force
- `-c`: Enable DNS brute-force
- `-v`: Verbose output
- `-q`: Quiet mode (suppress warnings)
- `-n`: DNS resolution
- `--screenshot`: Capture screenshots of discovered subdomains

---

## 📘 Usage Examples (With Descriptions)

### 1. Basic DNS Brute-Force
```bash
theHarvester -d example.com -c -w subdomains.txt
```
Performs brute-force against DNS using a wordlist.

### 2. Save Results to File (JSON/XML)
```bash
theHarvester -d example.com -c -w subdomains.txt -f result_output
```
Exports results for later review.

### 3. Subdomain Screenshots
```bash
theHarvester -d example.com -c -w subdomains.txt --screenshot screenshots/
```
Visual capture of exposed interfaces.

### 4. Limit Scan Results
```bash
theHarvester -d example.com -l 50 -c -w subdomains.txt
```
Quick scan with up to 50 results.

### 5. Multi-Source Scan
```bash
theHarvester -d example.com -b all -c -w subdomains.txt -q
```
Pulls from all supported sources.

### 6. Verbose Output
```bash
theHarvester -d example.com -v -c -w subdomains.txt
```
In-depth output during scan.

### 7. Brute + DNS Lookup
```bash
theHarvester -d example.com -c -n -w subdomains.txt
```
Combines brute-forcing with DNS resolution.

### 8. Custom DNS Resolvers
```bash
theHarvester -d example.com -r resolvers.txt -c -w subdomains.txt
```
Useful for avoiding DNS filtering.

### 9. Screenshots + Output
```bash
theHarvester -d example.com --screenshot screenshots/ -c -w subdomains.txt -f full_results
```
Complete visual and structured data dump.

### 10. Aggressive Enumeration
```bash
theHarvester -d example.com -l 1000 -c -w subdomains.txt
```
Deep dive for high-value domains.

### 11. API Endpoint Scan
```bash
theHarvester -d example.com -a -w endpoints.txt
```
Finds undocumented APIs.

### 12. API + Brute Force
```bash
theHarvester -d example.com -a -c -w endpoints.txt
```
Comprehensive endpoint enumeration.

### 13. RAPIDNS Source
```bash
theHarvester -d example.com -b rapiddns -c -w subdomains.txt
```
Great for passive DNS visibility.

### 14. Yahoo Source + Save
```bash
theHarvester -d example.com -b yahoo -c -w subdomains.txt -f yahoo_report
```
Useful fallback when Google limits are reached.

### 15. CRT.sh + Screenshots
```bash
theHarvester -d example.com -b crtsh -c -w subdomains.txt --screenshot screenshots/
```
Enumerates cert transparency logs.

### 16. Offset Start
```bash
theHarvester -d example.com -S 100 -l 200 -c -w subdomains.txt
```
Skips first 100, fetches next 200 results.

### 17. Quiet Mode
```bash
theHarvester -d example.com -b all -c -w subdomains.txt -q
```
Suppresses warnings — useful for automation.

### 18. Alternate Wordlist
```bash
theHarvester -d example.com -c -w /usr/share/seclists/Discovery/DNS/namelist.txt
```
Use extensive or customized wordlists.

### 19. DuckDuckGo Source
```bash
theHarvester -d example.com -b duckduckgo -c -w subdomains.txt
```

### 20. Passive Only (No DNS)
```bash
theHarvester -d example.com -w subdomains.txt
```
Avoids triggering alerts.

### 21. Subdomain Takeover Check
```bash
theHarvester -d example.com -c -w subdomains.txt -t
```

### 22. Virtual Host Enumeration
```bash
theHarvester -d example.com -n -v -c -w subdomains.txt
```

### 23. Short Scan with Report
```bash
theHarvester -d example.com -l 25 -f short_scan -c -w subdomains.txt
```

### 24. Combine RAPIDNS + SiteDossier
```bash
theHarvester -d example.com -b rapiddns,sitedossier -c -w subdomains.txt
```

### 25. Full API Scan + Output
```bash
theHarvester -d example.com -a -w endpoints.txt -f apiscan_report
```

### 26. Internal Environment
```bash
theHarvester -d test.internal -c -w internal_subs.txt -f testenv_report
```

### 27. GitHub Code Search
```bash
theHarvester -d example.com -b github-code -c -w subdomains.txt
```

### 28. CRT.sh + RAPIDNS
```bash
theHarvester -d example.com -b crtsh,rapiddns -c -w subdomains.txt
```

### 29. Quiet Screenshot Run
```bash
theHarvester -d example.com --screenshot out/ -c -w subdomains.txt -q
```

### 30. Batch Multiple Domains
```bash
for domain in domain1.com domain2.com; do
  theHarvester -d $domain -b all -c -w subdomains.txt -q -f $domain;
done
```

---

## 🧠 Pro Tips

- Use curated wordlists like SecLists:
  ```bash
  /usr/share/seclists/Discovery/DNS/
  ```
- For stealth, combine `-q` and `-n`
- Automate and log using `-f` for structured output
- Ideal for pre-engagement reconnaissance

---

## ⚖️ Legal Disclaimer

> **Always obtain proper authorization before scanning any domain. Unauthorized reconnaissance may violate ethical, legal, or organizational rules.**

