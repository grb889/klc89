# The Social-Engineer Toolkit (SET) — Comprehensive Master Guide

## Table of Contents

1\.  \[Spear-Phishing Attack Vectors\](#spear-phishing-attack-vectors)  
2\.  \[Website Attack Vectors\](#website-attack-vectors)  
3\.  \[Infectious Media Generator\](#infectious-media-generator)  
4\.  \[Create a Payload and Listener\](#create-a-payload-and-listener)  
5\.  \[Mass Mailer Attack\](#mass-mailer-attack)  
6\.  \[Arduino-Based Attack Vector\](#arduino-based-attack-vector)  
7\.  \[Wireless Access Point Attack Vector\](#wireless-access-point-attack-vector)  
8\.  \[QRCode Generator Attack Vector\](#qrcode-generator-attack-vector)  
9\.  \[Powershell Attack Vectors\](#powershell-attack-vectors)  
10\. \[Third Party Modules\](#third-party-modules)

\---

## **Introduction to the Social-Engineer Toolkit (SET)**

The Social-Engineer Toolkit (SET) is a Python-driven, open-source penetration testing framework used for social engineering attacks. It's designed to test an organization's security by simulating real-world attacks that target the human element, often the weakest link in security. SET is bundled with Kali Linux and has millions of downloads. It is intended strictly for ethical use with explicit consent.

\---

## **Getting Started: A Step-by-Step Tutorial for Beginners**

SET is menu-driven, making it accessible even for novices.

### **Step 1: Launch SET**  
Run the following in Kali Linux terminal (may require root):  
\`\`\`bash  
sudo setoolkit  
\`\`\`  
Upon launch, it may check for updates then present the main menu.

### **Step 2: Navigate the Main Menu**  
Options:  
1\. Social-Engineering Attacks (primary for most use cases)  
2\. Penetration Testing (Fast-Track)  
3\. Third Party Modules  
4\. Update the Social-Engineer Toolkit  
5\. Update SET Configuration  
6\. Help, Credits, and About  
7\. Exit SET

For beginners, choose option **1) Social-Engineering Attacks**. You will then see the list of attack vectors that form the basis of this guide.

\---

## **1. Spear-Phishing Attack Vectors** 

### **Use Case: Spear-Phishing Campaign Simulation**  
**Scenario:** A penetration tester is tasked with evaluating an organization's employee vulnerability to targeted phishing attacks using customized emails tailored with personal information gathered from OSINT.

**Objective:** To assess employee response to spear-phishing emails and gather data on successful clicks or credential submissions.

**Step-by-Step Tutorial:**  
1\.  Launch SET (\`sudo setoolkit\`).  
2\.  Select Option 1: Social-Engineering Attacks.  
3\.  Select **"Spear-Phishing Attack Vectors."**  
4\.  Choose **"Spear-Phishing Email Attack."**  
5\.  Import a pre-created email list containing targeted employee emails.  
6\.  Customize the email template with personal details (e.g., name, position, company projects) to increase authenticity.  
7\.  Select to send the phishing email with a link to a cloned login page hosted on the tester's server (credential harvester).  
8\.  Monitor SET terminal for any credentials or user interactions captured.  
9\.  Document findings to provide feedback and improve company security awareness.

**Explanation:** This use case shows how SET can be leveraged to simulate highly targeted phishing attacks, critical for assessing real-world risks. The tester must have permission, use safe lab environments, and ensure employees are debriefed afterward on recognizing social engineering attacks.

\---

## **2. Website Attack Vectors** 

### **Tutorial: Credential Harvesting with a Cloned Website**  
**Scenario:** An ethical hacker simulates a phishing test on their organization by cloning a common login page to assess employee awareness. This is a common attack that aims to capture a user's username and password by luring them to a fake website.

**Step-by-Step Instructions:**

1. From the SET menu, select **"Website Attack Vectors"**.  
2. Choose **"Credential Harvester Attack Method"**.  
3. Select **"Site Cloner"**.  
4. Enter the URL to clone, e.g., https://www.facebook.com or your target's internal webmail portal.  
5. SET will now ask for your IP address. **This is the critical part.** You must provide the IP address of your Kali machine, as it will act as the web server to host the cloned page and a listener to capture the credentials. If the target is on your local network, use your local IP (e.g., 192.168.1.50). If the target is external, you'll need to use a public IP address and configure port forwarding or use a tunneling service like ngrok.  
6. SET will automatically clone the site and start the web server and listener. When the victim enters their credentials on your fake site, the data will be sent (POSTed) back to your Kali machine and displayed in your terminal.

\---

## **3. Infectious Media Generator** 

#### **Tutorial: USB-Based Payload Delivery**

**Scenario:** A curious employee picks up a USB drive labeled "Confidential Employee Salaries" that was intentionally left in a public area of an office. They plug it into their computer, and a malicious payload executes, giving you a remote backdoor.

**Prerequisites:**

* A USB drive.  
* The **"Create a Payload and Listener"** module must be run **before** deploying the USB drive to set up your handler.

**Step-by-Step Instructions:**

1. From the main SET menu, choose **"Infectious Media Generator"**.  
2. Select a payload method (e.g., **"File-Format Exploits"** or **"Standard Metasploit Executable"**).  
3. Choose a specific payload (e.g., a Windows reverse TCP shell).  
4. SET will generate the malicious file (e.g., a .pdf.exe or a .exe).  
5. Configure the LHOST (your Kali machine's IP) and LPORT (e.g., 4444) for the connection.  
6. Transfer the generated malicious file to a USB drive and name it something enticing like 2025\_Q4\_Salary\_Adjustments.xls.exe.  
7. Once the victim plugs in the drive and runs the file, a connection will be established to the listener you have already set up.

*This attack tests physical security controls and user willingness to run unknown files.*


\---

## **4. Create a Payload and Listener** 

### **Tutorial: Metasploit Integration**  
**Concept:** This module is the foundation for all attacks in SET that involve a payload calling back to your machine. It's a critical utility used to generate standalone payloads and, most importantly, to start the **Multi/Handler listener** in Metasploit. The handler is a listener that sits in a listening state waiting for an incoming connection from a malicious payload that has been executed on a target machine. This is a crucial step that must be completed **before** you attempt to run any payload-based attack.

**Step-by-Step Instructions:**  
1\.  Select **"Create a Payload and Listener"** from the SET menu.  
2\.  Choose **"Listener Options"**.  
3\.  Select **"Start Multi/Handler"**.  
4\.  Configure the payload type (e.g., \`windows/meterpreter/reverse_tcp\`), LHOST, and LPORT.  
5\.  SET will launch the Metasploit handler in the background. This listener is essential for receiving connections from:  
    *   Infectious Media payloads  
    *   PowerShell attacks  
    *   Arduino-based attacks  
    *   Any other payload that calls back to your machine.

\---

## **5. Mass Mailer Attack**

### **Tutorial: Broad Phishing Campaign**  
**Concept:** Unlike the targeted spear-phishing option, the Mass Mailer is designed to send a generic phishing email to a large list of addresses. It's useful for testing baseline awareness across a whole organization.

**Step-by-Step Instructions:**  
1\.  Select **"Mass Mailer Attack"**.  
2\.  Choose to use a pre-built HTML email template or create your own.  
3\.  Provide the path to a text file containing the list of email addresses.  
4\.  Set the "From" address to something seemingly legitimate (e.g., \`IT-Support@yourcompany.com\`).  
5\.  Configure your email relay (e.g., a local SMTP server or Gmail app password).  
6\.  Send the email and monitor the credential harvester or other linked attack vector for results.

\---

## **6. Arduino-Based Attack Vector (Teensy USB HID Attack)** 

### **Tutorial: Physical USB Drop Attack**  
**Concept:** This attack uses a programmable microcontroller board like a Teensy or Arduino Leonardo. These devices can be programmed to emulate a Human Interface Device (HID), like a keyboard. When plugged into a target computer, they are automatically recognized, and the device can be pre-programmed to execute a series of keystrokes at lightning speed to open a terminal and download/execute a malicious payload.

**Scenario:** A physical penetration tester gains brief access to a target's office. They plug a pre-programmed Teensy device into an unattended computer to establish a remote backdoor.

**Prerequisites:**  
*   A Teensy++ USB 2.0 development board (or similar HID-compatible Arduino).  
*   The \`teensy_loader\` software on your Kali machine (\`sudo apt install teensy-loader\`).

**Step-by-Step Instructions:**  
1\.  **Launch SET and select the vector:**  
    \`\`\`bash  
    sudo setoolkit  
    \`\`\`  
    Select: **1) Social-Engineering Attacks**  
    Select: **6) Arduino-Based Attack Vector**

2\.  **Configure the Payload:**  
    *   SET will present a menu of pre-configured attack payloads. A common choice is:  
        *   **1) Windows Reverse TCP Shell** \- Creates a shell that calls back to your machine.  
    *   You will be prompted for your Kali Linux machine's **LHOST** (your IP address) and **LPORT** (a port to listen on, e.g., 443 or 4444).

3\.  **Generate and Prepare the Payload:**  
    *   SET will generate the malicious C++ code designed for the Teensy and save it to a file. It will display the path (e.g., \`/usr/share/set/src/teensy/teensy.ino\`).  
    *   **Critical Step:** You must now open the Arduino IDE on your Kali machine.  
    *   Install the Teensyduino add-on for the IDE (from the PJRC website).  
    *   Open the \`.ino\` file generated by SET in the Arduino IDE.  
    *   Select the correct board (e.g., Teensy++ 2.0) and USB Type (usually "Keyboard").  
    *   Verify and compile the code. With the Teensy board plugged in, press its program button and upload the code from the Arduino IDE.

4\.  **Set Up the Listener:**  
    *   Before deploying the device, you must start a listener to catch the reverse shell connection. In SET's main menu, use:  
        *   **4) Create a Payload and Listener** \-\> **Listener Options** \-\> **Start Multi/Handler**  
    *   Configure the handler with the same LHOST and LPORT you used for the payload.

5\.  **Deploy:**  
    *   The Teensy is now a malicious USB stick. Plug it into the target machine. It will impersonate a keyboard and automatically type the commands to establish a reverse connection to your machine, granting you access.

**Warning:** This is a highly invasive physical attack. Explicit permission for physical testing is an absolute requirement.

\---

## **7. Wireless Access Point Attack Vector (Evil Twin Attack)** 

### **Tutorial: Rogue Access Point Setup**  
**Concept:** SET can help you create a rogue wireless access point (an "Evil Twin") that mimics a legitimate corporate or public network (e.g., "Company_Guest"). When users connect to this malicious Wi-Fi, you can intercept their traffic, perform SSL stripping, and redirect them to credential-harvesting portals.

**Scenario:** Testing the awareness of employees regarding Wi-Fi security. The tester sets up a malicious AP with a name similar to the corporate network in a nearby location.

**Prerequisites:**

* A Kali Linux machine.  
* **A wireless card capable of monitor mode and packet injection.** This is a significant hardware requirement that many standard laptops do not meet. It's often easier to use a USB-based wireless card designed for penetration testing.  
* Knowledge of the target's legitimate SSID (network name).

**Step-by-Step Instructions:**  
1\.  **Launch SET and select the vector:**  
    \`\`\`bash  
    sudo setoolkit  
    \`\`\`  
    Select: **1) Social-Engineering Attacks**  
    Select: **7) Wireless Access Point Attack Vector**

2\.  **Configure the Rogue Access Point:**  
    *   SET will guide you through configuration. First, it will likely ask for the interface for the rogue AP (e.g., \`wlan0\`).  
    *   It will then ask for the SSID. Enter a convincing name (e.g., \`CompanyName_Public\`).  
    *   You will be asked to select a network type. For a credential harvester, choose:  
        *   **1) Fake AP \- Harvest Credentials without Jamming**  
    *   SET will now set up the rogue AP and a DHCP server and may automatically launch a credential harvester.

3\.  **Integrate with a Cloned Site:**  
    *   During the setup, SET will likely prompt you to clone a website for credential harvesting. You can enter the URL of the target's captive portal or a common site like a webmail login.  
    *   Any user who connects and tries to browse will be presented with this cloned login page. Their credentials will be captured in the SET terminal.

4\.  **Deploy and Monitor:**  
    *   Let the rogue AP run. Users might connect automatically if their devices have connected to a similarly named network before.  
    *   Monitor the SET terminal for any captured credentials and HTTP traffic.

**Note:** This attack is often combined with manual jamming of the real access point using a tool like \`mdk4\` to force devices to connect to your stronger malicious signal.

\---

## **8. QRCode Generator Attack Vector** 

### **Tutorial: QR Code Phishing Campaign**  
**Concept:** This technique leverages the widespread trust and use of QR codes. SET generates a QR code that embeds a malicious URL. When scanned, the victim is redirected to a credential-harvesting site or a payload-dropping page, all while believing they are interacting with a legitimate, physical object like a poster or flyer.

**Why it's effective:**  
*   **Obfuscates the URL:** The victim never sees the suspicious link.  
*   **High Trust Factor:** QR codes are used by reputable companies everywhere.  
*   **Physical World Bypass:** This attack bridges the digital and physical social engineering worlds, bypassing email filters entirely.

**Scenario:** A penetration tester places a professionally printed poster with a QR code in common areas offering a fake "Free Company Swag" giveaway.

**Prerequisites:**  
*   Kali Linux machine with SET.  
*   The machine's IP address.  
*   A simple web server (like Apache) started: \`sudo systemctl start apache2\`.

**Step-by-Step Instructions:**  
1\.  **Launch SET and Navigate to the Attack Vector:**  
    \`\`\`bash  
    sudo setoolkit  
    \`\`\`  
    Select: **1) Social-Engineering Attacks**  
    Select: **8) QR Code Generator Attack Vector**

2\.  **Configure the QR Code Attack:**  
    *   SET will ask for the IP address for the POSTING server. This is your Kali machine's IP (e.g., \`192.168.1.50\`).  
    *   Next, you will be prompted to select the attack type. Choose:  
        *   **1) URL (Phishing or Other)** for a credential harvester.  
    *   Enter the full URL you want the victim to be redirected to. To integrate with SET's harvester, you can use \`http://\<YOUR_KALI_IP\>/\`.

3\.  **Generate the QR Code:**  
    *   SET will generate a PNG image file (\`/var/www/html/qrcode_attack.png\`) and host it automatically.  
    *   **Crucially, it will also display the QR code directly in the terminal.** You can take a screenshot of this terminal output to test with your phone.

4\.  **Deploy the QR Code:**  
    *   The generated PNG is placed in Kali's web root (\`/var/www/html/\`). You can download it by visiting \`http://\<YOUR_KALI_IP\>/qrcode_attack.png\` from another machine on the network.  
    *   Print this QR code and place it on a realistic poster or flyer.

5\.  **Capture Credentials:**  
    *   When an employee scans the code, their phone will open the malicious login page you configured.  
    *   Any credentials they enter will be captured and saved by SET, and you will see the data in real-time within the SET terminal window.

**Post-Test Analysis:** Document how many times the QR code was scanned and how many credentials were submitted.

\---

## **9. Powershell Attack Vectors**   
### **Tutorial: Fileless PowerShell Attack**  
**Concept:** PowerShell is a powerful scripting language built into Windows that is often overlooked by traditional antivirus software. SET's PowerShell attacks generate malicious scripts that can be delivered via email or a website to download and execute payloads entirely in memory, leaving minimal traces on the target's disk.

**Scenario:** Bypassing antivirus software during a spear-phishing campaign by embedding a malicious PowerShell command in a Word document or a link within an email.

**Step-by-Step Instructions:**  
1\.  **Launch SET and select the vector:**  
    \`\`\`bash  
    sudo setoolkit  
    \`\`\`  
    Select: **1) Social-Engineering Attacks**  
    Select: **9) Powershell Attack Vectors**

2\.  **Choose an Attack Method:**  
    SET offers several PowerShell options. The most common is:  
    *   **1) Powershell Alphanumeric Shellcode Injector** \- This encodes a payload into an alphanumeric string that can be executed via a single PowerShell command.

3\.  **Generate the Payload:**  
    *   Select your payload type (e.g., **1) Windows Reverse TCP Shell**).  
    *   Enter your **LHOST** (Kali IP) and **LPORT** (listening port).  
    *   SET will generate a long, obfuscated PowerShell command. It will look something like:  
        \`powershell \-Ep Bypass \-Command "& { ... \[LONG_ALPHANUMERIC_STRING\] ... }"\`  
    *   **Copy this entire command.**

4\.  **Delivery and Execution:**  
    *   **Email Delivery:** Paste this command into a Word macro. When the document is opened and macros are enabled, it will execute the PowerShell payload.  
    *   **Web Delivery:** You can serve this command from a website. A common trick is to have a victim copy and paste a "fix" or "plugin installer" command directly into their PowerShell terminal.  
    *   SET can automate this web delivery through the **2) Web Attack Vectors** \-\> **3) PowerShell Alphanumeric Shellcode Injector** menu.

5\.  **Catch the Shell:**  
    *   Before the victim executes the payload, set up a listener in SET (**4) Create a Payload and Listener** \-\> **Listener Options** \-\> **Start Multi/Handler**).  
    *   Once the victim runs the command, you will receive a reverse shell on your listener.

\---

## **10. Third Party Modules** 

### **Tutorial: Extending SET's Capabilities**  
**Concept:** This menu option allows you to import and use external modules that are not officially part of the core SET framework. These can be custom attack vectors, new integration tools, or scripts written by the community.

**How to Use:**  
1\.  Select **"Third Party Modules"** from the main SET menu.  
2\.  You will be presented with a list of available modules that have been added to the appropriate directory.  
3\.  Select a module to execute it.  
4\.  These modules often come with their own setup and configuration instructions. Always read any provided README files.

**Note:** The availability and functionality of these modules depend on the user manually adding them. The core SET installation may not have any third-party modules by default.

\---

## **Navigation and Best Practices for Beginners**

*   **Always** test in isolated environments with explicit, written permission. Never test on unauthorized systems.  
*   Understand the legal implications of each attack vector, especially physical (Arduino) and wireless ones.  
*   Read prompts and settings carefully. A misconfigured IP address will cause the attack to fail.  
*   Combine SET with frameworks like Metasploit for advanced payload handling and persistence.  
*   For web attacks, ensure your Apache server is running: \`sudo systemctl start apache2\`.  
*   Maintain ethical standards. **Always debrief** targets after a test to turn the attack into a training opportunity. The goal is to improve security, not to punish users.  
*   Stay updated. Use option **4) Update the Social-Engineer Toolkit** regularly to get the latest features and security patches.  
