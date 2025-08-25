### **Email Forensic Investigation**

An email is more than just a simple message; it is a digital artifact containing a wealth of technical information. This document outlines a professional, step-by-step methodology for conducting a full email forensic investigation to uncover the true origin of a message and determine if it is legitimate, spam, or a sophisticated spoof.

### **Phase 1: Initial Data Collection and Verification**

**Step 1: Understand the Deception of the "From" Field**

The "From" field, as displayed in an email client, is the easiest part of an email to forge and should never be trusted as the sole indicator of authenticity. This is due to the foundational design of the Simple Mail Transfer Protocol (SMTP), which did not prioritize security in its early development.

An email address in the SMTP protocol has two key components:

* **The "Envelope From" (MAIL FROM):** This is the address used by mail servers for delivery and for sending non-delivery reports, also known as "bounces".  
* **The "Header From" (From):** This is the address that appears to the recipient in their email client.

A crucial flaw in the system is that these two addresses do not have to match. An attacker can tell a mail server to send a message from one address (spammer@123.net) while displaying a completely different one (president@whitehouse.gov) in the header. They achieve this without needing to compromise the target's account credentials, simply by using a malicious mail server or script to forge the email headers.

Attackers commonly achieve this through three primary methods:

* **Using an Open Relay Server:** A misconfigured mail server that allows anyone on the internet to send email through it. An attacker can connect and specify any "From" address they choose.  
* **Using a Malicious/Rogue SMTP Server:** A spoofer can operate their own email server, allowing them to program it to generate and send emails with any From header they desire.  
* **Phishing Kits and Automated Tools:** Pre-packaged tools widely available on the dark web make it easy for even non-technical individuals to craft and send spoofed emails in bulk.

---

## **Examples of Pre-Built Spoofing & Phishing Kits**

### **BlackEye**
- Very popular phishing toolkit (open-source, also cloned by threat actors).  
- Provides ready-made templates to mimic Facebook, Gmail, Instagram, PayPal, etc.  
- Often used with tunneling services (Ngrok, Serveo) to make phishing pages publicly accessible.  
- **OSINT clue:** If you see `ngrok.io` or `serveo.net` URLs in phishing campaigns, they may be BlackEye-based.  

### **ZPhisher**
- Bash-based toolkit, successor to BlackEye in some ways.  
- 30 phishing templates for major platforms (Netflix, LinkedIn, Twitter, etc.).  
- Simplifies credential capture by generating fake login pages quickly.  

### **SocialFish**
- Phishing framework with Python backend.  
- Integrates with Ngrok for easy public hosting.  
- Known for its modular design: attackers can pick a template, deploy it in minutes.  

### **Evilginx2 (Advanced MITM Phishing)**
- Unlike template kits, this performs a **reverse proxy attack**.  
- Intercepts traffic between user and legitimate site → can steal **session cookies** (bypasses 2FA).  
- **OSINT marker:** SSL certificates from Let’s Encrypt, suspicious subdomains mimicking real services.  

---

**OSINT Upgrade: Open Relay Identification**

* Use OSINT tools like **Shodan** or **Censys** to identify open relay mail servers still exposed on the internet. This provides actionable intelligence on the types of infrastructure attackers can leverage.

---


### **Phase 2: Deciphering the Headers \- The Digital Trail**

**Step 2: Obtain the Full Email Headers**

The full email headers are the most critical evidence in any investigation. They contain the true technical routing information and act as a log of the email's journey from its origin.

* **How to retrieve them:** Every major email client has an option to view the "original" or "full" headers.  
  * **Outlook:** File \-\> Properties \-\> Internet headers   
  * **Gmail:** More options (three dots) \-\> Show original   
  * **Apple Mail:** View \-\> Message \-\> Raw Source 

The headers will be a block of text containing fields like

Received, Return-Path, SPF, DKIM, and Message-ID. Copy this entire block into a text editor for analysis.

**Step 3: Analyze the Received Headers**

The Received headers are a chain of records, each added by a server that handled the email. They must be read from the bottom up to trace the email's path from its origin to you.

* **IP Addresses:** Use tools like **nslookup** or **whois** to check the IP addresses in the Received headers and identify the server's location and owner.  
* **Timestamps:** Analyze the timestamps. A large time gap between servers could indicate a delay or manipulation, while a suspiciously short gap between distant servers could be a red flag.  
* **Consistency Check:** Compare the Received headers to the "From" address. A mismatch between the originating IP address and the claimed sender's network is a strong indicator of spoofing.

**OSINT Upgrade**:

* Use tools like ipinfo.io, whois.domaintools.com, or AbuseIPDB to get ownership and abuse reports.  
* Cross-reference IP with public blacklists (Spamhaus, Talos Intelligence).  
* If IP belongs to a cloud provider (AWS, GCP, OVH), suspect throwaway virtual machines.

**Step 4: Check the Return-Path and Message-ID**

* **Return-Path:** This header specifies where non-delivery or "bounce" messages should be sent. This is often the true sender's address. If the  
* Return-Path differs from the From address, it is a significant red flag for spoofing.  
* **Message-ID:** This is a unique identifier assigned by the sending server. Its format can offer clues about the software used.

**Step 5: Verify Sender Authentication**

Modern email systems use three primary authentication methods to combat spoofing. These are critical for determining an email's legitimacy.

* **SPF (Sender Policy Framework):** A DNS record that specifies which mail servers are authorized to send email for a domain. A  
* pass result confirms authorization, while fail or softfail indicates an unauthorized server.  
* **DKIM (DomainKeys Identified Mail):** Adds a digital signature to the email header to verify that the content has not been tampered with and that the sender is legitimate. A valid signature indicates authenticity.  
* **DMARC (Domain-based Message Authentication, Reporting & Conformance):** A policy that tells a receiving mail server what to do with an email that fails SPF or DKIM check. Look for  
* Authentication-Results headers for the final verdict.

**OSINT Upgrade**:

* Use **mxtoolbox.com** or **dmarcian.com** to query SPF/DKIM/DMARC.  
* Note: Many phishing domains lack DMARC, or set DMARC to “none” to avoid rejection.  
* If DKIM fails → extract **d=domain.com** value → investigate domain age and registrar.

**Tutorial Using `mxtoolbox.com`:**

1. Open your web browser and navigate to `mxtoolbox.com`.  
2. In the main search bar, enter the domain name you wish to investigate (e.g., `google.com`).  
3. Click the dropdown menu next to the search bar and select the specific record type you want to query: `SPF Record Lookup`, `DKIM Record Lookup`, or `DMARC Record Lookup`.  
4. Click the search button. The tool will display the DNS record, providing details about the sender authentication configuration for that domain.

**Tutorial Using `dmarcian.com`:**

1. Navigate to `dmarcian.com/dmarc-inspector/`.  
2. In the input field, enter the domain name you're investigating.  
3. The tool will automatically run a DMARC check and provide a simple report on the domain's DMARC, SPF, and DKIM statu

---

### **Phase 3: Content, Metadata, and OSINT**

**Step 6: Analyze Message Body, URLs, and Attachments**

Even with valid headers, the content can reveal a fraudulent intent.

* **Suspicious URLs:** Hover over links without clicking them. Check if the URL matches the company it claims to represent. Use URL reputation tools to check for known malicious links.  
* **Urgency and Threats:** Emails that demand immediate action or threaten account suspension are classic social engineering tactics.  
* **Metadata in Attachments:** Do not open attachments directly. Analyze their metadata using a viewer to find clues such as the author's name, the program used to create the file, or the computer's name.

**Attachment Analysis**:

* Extract metadata with `exiftool`, `oletools`, or **VirusTotal**.  
* Malicious docs may contain macros → sandbox in **Cuckoo Sandbox** or **Any.Run**.

**OSINT Upgrade: Researching Phishing Infrastructure**

* [**GitHub Repositories**](https://github.com/topics/phishing-kit)**:** These resources provide practical examples of tools used by attackers, which can be useful for studying phishing infrastructure:  
  * **M4cs/BlackEye-Python:** A phishing kit with Serveo subdomain creation support, useful for studying infrastructure design.  
  * **Err0r-ICA/Phishbait:** A working phishing tool with templates for numerous websites, useful for understanding contemporary tactics.  
  * **curtbraz/PhishAPI:** A web-based phishing suite with real-time alerting, an excellent case study in automated phishing.  
  * **0xDanielLopez/phishing\_kits:** Catalogs real-world phishing kits for exploring attacker tactics.  
  * **t4d/StalkPhish:** A Python tool that aggregates phishing kits for investigative research and threat hunting.  
  * **duo-labs/phish-collect:** A project designed to harvest phishing kits at scale, useful for studying automation techniques.  
* **Sample Phishing Emails:** Collect sample emails from public repositories like **PhishTank** or **Spamhaus** for pattern recognition training.

### **Summary: Spam vs. Spoof**

* **Spam:** Often has a valid sender and may pass some or all authentication checks. The headers are usually consistent with the sender's mail server. The goal is mass distribution for advertising or scams.  
* **Spoof:** The headers are manipulated to impersonate a legitimate sender. Key indicators include a mismatch between the  
* From and Return-Path headers, failed SPF/DKIM/DMARC checks, and an originating IP address that is not from the claimed sender's network.

By following this comprehensive methodology, you can move past the surface-level deception and uncover the true origins of a malicious email. This skill is fundamental to protecting yourself and your organization from a wide range of cyber threats.

