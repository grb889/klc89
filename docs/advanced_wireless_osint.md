# **🛰️ Advanced Wireless OSINT Workflow: A Comprehensive Guide**

This guide details a powerful, multi-tool workflow for conducting Open-Source Intelligence (OSINT) investigations using wireless signals. By combining a portable data capture device with advanced logging and analysis software, we can move beyond simple location data to build detailed behavioral profiles.

```markdown
## 📡 Foundational Concepts and Theoretical Background

Before applying the workflow and tools, it is essential to understand the underlying technologies and protocols that make wireless OSINT feasible. These concepts explain **why** the workflow works and highlight both its strengths and limitations.

### 🔊 How Wi-Fi and Bluetooth Work

Both Wi-Fi and Bluetooth operate using **radio frequency (RF) communication**, where devices encode and transmit data through radio waves. In Wi-Fi:

- **SSID (Service Set Identifier):** A human-readable name of a wireless network (e.g., `HomeNetwork`, `Airport_Free_WiFi`). It is what users see when selecting a network.
- **BSSID (Basic Service Set Identifier):** The unique **MAC address** of a wireless access point (AP) broadcasting that SSID. Unlike SSIDs, which may be duplicated across many networks, the BSSID is globally unique to the hardware interface.

This distinction is crucial: while SSIDs indicate *what* a network is called, BSSIDs identify *where* and *which device* is broadcasting it.

Bluetooth works similarly, using **device identifiers** (BD_ADDR) to manage connections. While less network-centric than Wi-Fi, Bluetooth advertising packets still reveal unique identifiers and device capabilities, which can be logged and analyzed in OSINT investigations.

---

### 📶 The Power of Probe Requests

When a Wi-Fi-enabled device (e.g., smartphone, laptop) is not connected to a network, it often sends out **probe requests**. These are broadcast frames asking: *“Is my known network here?”*

- A probe request may contain the SSIDs of networks the device has previously connected to.
- By capturing these frames, an analyst can reconstruct a **digital breadcrumb trail** of the user’s prior connections.
- Example: If a phone probes for `CafeRoma_WiFi` and `UniLibrary_5GHz`, this reveals not only the device’s owner’s movement history but also probable places they frequent.

This makes probe requests a **goldmine for tracking**. Even without connecting to any network, devices inadvertently leak valuable historical and behavioral data.

---

### 🛡️ MAC Address Randomization

Historically, probe requests revealed a device’s true MAC address, making long-term tracking trivial. To mitigate this, modern operating systems (iOS, Android, Windows, Linux) introduced **MAC address randomization**, which alters the device’s source MAC in probe requests.

- **Goal:** Prevent persistent identification by changing the MAC each time (or at least periodically).
- **Challenge for OSINT:** This disrupts correlation between sessions, making it harder to say with certainty that two probe sets belong to the same device.

However, randomization is not foolproof. Analysts can still track devices by leveraging:

1. **SSID Patterns** – A user’s personal “set” of known networks is often unique.  
2. **Probe Timing & Frequency** – Devices have characteristic rhythms in how often and when they send probes.  
3. **Cross-Layer Fingerprinting** – Combining RSSI (signal strength), chipset quirks, or supported standards to link randomized sessions together.

Thus, while MAC randomization raises the bar, persistent identifiers and behavioral fingerprints remain exploitable.

---



## **🔧 Tools of the Trade**

This workflow is built on a synergistic combination of hardware and software.

* **ESP32 Marauder:** A small, portable Wi-Fi and Bluetooth reconnaissance device. Its primary function in this workflow is to passively sniff and capture probe requests from nearby devices, logging their MAC addresses and SSID history.  
* **Raspberry Pi:** A versatile, low-cost microcomputer. It serves as a dedicated, mobile platform for running the data logging and analysis software.  
* **Kismet:** A powerful wireless network detector, packet sniffer, and intrusion detection system. It is the central hub for logging all captured wireless data into a structured database, which can be enriched with GPS coordinates if a module is connected.  
* **"Chasing Your Tail" Script:** A Python-based analysis tool designed to work with the Kismet database. It specializes in detecting the persistent presence of a device over time, a key indicator of surveillance or a targeted individual's routine. The GitHub repository for the script is **https://github.com/ArgeliusLabs/Chasing-Your-Tail-NG**.  
* **WiGLE.net:** A massive, crowdsourced database of wireless networks and their geographical locations. It is an invaluable resource for cross-referencing captured SSIDs with real-world locations.

## 🛠️ Deeper Tool-Specific Technical Details

While the workflow introduces the tools conceptually, a practical OSINT investigation requires deeper technical mastery. This chapter provides a detailed breakdown of the most critical tools, their configuration, and hands-on usage strategies.

---

### 🔹 ESP32 Marauder

The **ESP32 Marauder** is a portable reconnaissance platform built on the ESP32 chipset. Its strength lies in its versatility and low-power portability.

#### Modes of Operation
- **Probe Request Sniffer:** Captures probe requests from nearby devices. This is the most relevant mode for OSINT, as it reveals SSID histories and device presence without transmitting.
- **Beacon Sniffer:** Listens for beacon frames from access points. Useful for mapping local APs and correlating them with WiGLE data.
- **Deauthentication Attack:** Forces clients to disconnect from APs by sending deauth frames. While technically supported, this is not typically relevant for ethical OSINT and crosses into offensive operations.

#### Firmware Flashing Tutorial
1. **Install Prerequisites:** Download and install [esptool.py](https://github.com/espressif/esptool).
2. **Connect Device:** Plug the ESP32 board into USB.
3. **Flash Firmware:**
   ```bash
   esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin
4. **Access Interface:** After boot, connect to the ESP32’s Wi-Fi AP (default SSID: `Marauder_AP`, password: `marauder`) and navigate to `192.168.4.1` in a browser.

#### **Configuration via Web UI**

* **Mode Selection:** Choose “Sniffer” mode for passive OSINT.

* **Logging:** Enable CSV/JSON export for probe requests.

* **Filters:** Configure filters to exclude your own devices for ethical operation.

---

### **🔹 Kismet**

Kismet is the **central data aggregation hub** for wireless OSINT, providing structured databases and extensible analysis.

#### **Setup & Configuration**

**Enable Monitor Mode:**

 `ip link set wlan1 down`  
`iw dev wlan1 set type monitor`  
`ip link set wlan1 up`

1. 

**Start Kismet:**

 `kismet -c wlan1`

2.  The `-c` flag specifies the capture interface.

#### **Common Command-Line Flags**

* `--no-ncurses`: Run headless without UI.

* `--log-prefix`: Define log file naming scheme.

* `--gps /dev/ttyUSB0`: Enable GPS logging if a module is attached.

#### **Querying the Kismet Database**

Kismet stores captured data in **SQLite format** (`kismet.db`).

Example queries using `sqlite3`:

List all probed SSIDs:

 `SELECT ssid FROM probe_requests;`

* 

Devices seen on a specific day:

 `SELECT device, first_time, last_time FROM devices WHERE first_time LIKE '2025-08-16%';`

* 

SSIDs with geolocation data:

 `SELECT ssid, lat, lon FROM devices WHERE lat IS NOT NULL;`

* 

This transforms raw packet captures into actionable intelligence.

---

### **🔹 WiGLE.net**

WiGLE is a **global crowdsourced database** of Wi-Fi networks, essential for contextualizing captured SSIDs.

#### **Search Types**

* **SSID Search:** Finds networks by their broadcast name. Good for matching common hotspots.

* **BSSID Search:** Uses AP MAC addresses for precise identification.

* **Map-Based Search:** Allows geospatial exploration of networks. Useful when narrowing down probable locations of a target device’s known SSIDs.

#### **Interpreting Results**

* **Number of Sightings:** Indicates how many times the network has been reported to WiGLE. A higher count suggests it is a permanent or widely-used AP.

* **Last Seen Date:** Helps determine whether the network is still active.

* **Coordinates:** Provides latitude/longitude of sightings. These can be imported into mapping tools for travel pattern analysis.

#### **Example Workflow**

1. Capture `CafeRoma_WiFi` in a probe request.
2. Search on WiGLE by SSID → Results show multiple locations across the city.
3. Refine with BSSID (if known) → Isolate the specific coffee shop branch frequented by the device owner.



## **🔁 Step-by-Step OSINT Workflow**

This process is a methodical progression from data capture to final analysis.

### **Step 1: On-Site Reconnaissance with the ESP32 Marauder**

The ESP32 Marauder is your primary field tool. Its small size and battery-powered operation make it ideal for discreet, on-the-go data collection. Simply power on the device and set it to Sniffer or Probe Request Monitor mode to begin.

* **Captured Data:** The Marauder captures two critical pieces of information: the **MAC address** of the device sending the probe request and the **SSID history**—a list of network names the device is searching for. This history is essentially a digital breadcrumb trail of where the device has been.

### **Step 2: Continuous Logging with Kismet on Raspberry Pi**

For a professional investigation, you need more than a simple list; you need a structured database.

* **Hardware Setup:** Connect a Wi-Fi adapter that supports **monitor mode** to your Raspberry Pi. This is a crucial requirement, as it allows the device to passively listen to all network traffic without having to connect to a network.  
* **Data Aggregation:** The data captured by the ESP32 Marauder can be streamed to a Kismet instance running on the Raspberry Pi. This creates a centralized, continuously updating database of all detected devices and networks, timestamped and, with a GPS module, geotagged.

### **Step 3: Pattern Analysis with the "Chasing Your Tail" Script**

This is where the magic happens. The raw data is transformed into actionable intelligence. The "Chasing Your Tail" script analyzes the Kismet database to find patterns that human observation might miss.

* **Behavioral Profiling:** The script looks for devices that repeatedly appear in the same location or in close proximity to the investigator's device over specific time intervals. By analyzing the frequency and timing of probe requests, it can identify a device's routine.  
* **Example Output:** The script can generate a summary output that clearly shows a device's first and last seen times, a list of probed SSIDs, and locations where it has been detected, creating a detailed profile of a target's habits.

{  
  "device\_mac": "AA:BB:CC:DD:EE:FF",  
  "first\_seen": "2025-08-16T08:00:00Z",  
  "last\_seen": "2025-08-16T09:45:00Z",  
  "probe\_ssids": \["HomeNetwork24", "CafeRoma\_WiFi", "Airport\_Free\_WiFi"\],  
  "locations\_detected": \["Downtown Hub", "Transit Center"\]  
}

### **Step 4: Historical Context and Corroboration with WiGLE.net**

The final step is to validate the collected data with a historical record. The SSID list from the captured probe requests can be used as a primary pivot for searches.

* **Search and Correlate:** Search for each captured SSID on WiGLE.net. The database will provide GPS coordinates, last seen dates, and the number of sightings for that network.  
* **Inference:** By cross-referencing your live data with WiGLE's historical data, you can build a comprehensive location profile, inferring a person's probable home address, workplace, and travel habits.

## 🔬 Advanced Techniques and Real-World Scenarios

Once the basics of wireless capture and logging are understood, the next step is to transform raw data into **actionable intelligence**. This section expands on advanced analysis strategies, case studies, and the real-world implications of probe request–based investigations.

---

### 📍 SSID-Based Geolocation Walkthrough (Case Study)

**Step 1 – Capture**  
Suppose a probe request capture yields the following SSID list from a single device:

{
  "probe_ssids": ["CoffeeShop_WiFi", "Airport_Free_WiFi", "HomeNetwork"]
}

**Step 2 – Correlate**  
 Each SSID can be queried against **WiGLE.net**:

* **CoffeeShop\_WiFi →** Resolves to a local café chain in the downtown district.  
* **Airport\_Free\_WiFi →** Matches the international airport’s public Wi-Fi network.  
* **HomeNetwork →** Mapped to a residential router in a suburban neighborhood.

**Step 3 – Analyze**  
 By aligning these SSIDs with time and location data:

* The device routinely appears near *CoffeeShop X* in the morning.  
* It subsequently probes for *Airport\_Free\_WiFi*, suggesting travel patterns.  
* The recurring presence of *HomeNetwork* implies a fixed residence.

**Inference:** This person likely lives in the identified suburb, commutes into the city, and travels frequently via the named airport.

---

### **👣 Behavioral Profiling and Motion Signatures**

The **“Chasing Your Tail”** script can be extended beyond simple time stamps to create **motion signatures**:

* **Signal Strength (RSSI):** Tracking fluctuations in RSSI across multiple captures allows reconstruction of a device’s movement relative to the sensor.

* **Probe Sequences:** The order and timing of probed SSIDs create a behavioral fingerprint, indicating whether a device is in transit, stationary, or following a habitual route.

* **Routine Extraction:** Over repeated observations, a device’s “daily rhythm” emerges, such as commute windows, break times, or recurring locations.

This transforms sporadic probe requests into a **predictive behavioral model**.

---

### **📡 Client vs. Access Point Tracking**

It is critical to distinguish between **client devices** (phones, laptops) and **access points** (home routers, hotspots):

* **Client Tracking:**

  * Achieved via **probe requests**.  
  * Ephemeral, behavior-rich, but limited by MAC randomization.  
  * Reveals movement, habits, and previously visited networks.

* **Access Point Tracking:**

  * Achieved via **beacon frames** and AP BSSIDs.  
  * Persistent, location-fixed identifiers.  
  * Indexed extensively in WiGLE, making them ideal for geolocation.

**Key Point:**  
 WiGLE’s strength lies in its **AP-based indexing** (SSID \+ BSSID). Client devices cannot be directly searched in WiGLE; instead, the SSIDs probed by clients must be cross-referenced against the AP database.



## **🛡️ Defenses, Limitations, and Advanced Techniques**

While this workflow is powerful, it is not foolproof. A skilled OSINT practitioner must be aware of its limitations.

* **MAC Randomization:** Modern devices randomize their MAC addresses to prevent tracking. The "Chasing Your Tail" script's reliance on SSID patterns and device persistence helps mitigate this limitation.  
* **WiGLE.net Constraints:** The WiGLE database does not index client device MAC addresses. Only SSIDs and access point MAC addresses (BSSIDs) are searchable.

### **Advanced Device Fingerprinting Techniques**

To overcome the challenges of MAC randomization, an analyst can employ advanced fingerprinting techniques:

* **SSID Patterns:** The unique combination of SSIDs a device probes for can be a unique identifier.  
* **Probe Request Timing:** The specific frequency and timing of probe requests can create a motion signature or behavioral profile.  
* **Hardware Quirks:** Variations in chipset behavior (e.g., from different operating systems like Android or iOS) can serve as distinguishing features.  
* **Signal Strength Profile:** Tracking the Received Signal Strength Indicator (RSSI) of a device over time creates a "motion signature" that can be used to identify it.

By combining these indicators, it's possible to build a persistent and accurate profile of a device even when its MAC address is randomized.

## **✅ Summary of the Workflow**

| Element | Used For | Searchable on WiGLE? |
| :---- | :---- | :---- |
| **SSID Names** | Inferring past locations and travel history | ✅ Yes |
| **Device MAC** | Local correlation only | ❌ No |
| **BSSID (AP MAC)** | Finding routers/APs | ✅ Yes |

This workflow provides a comprehensive, ethical, and powerful approach to wireless OSINT by combining real-time capture, automated logging, and powerful analysis to move from simple data collection to actionable intelligence.

## 🔧 Troubleshooting

Even with a well-structured workflow, technical obstacles are common in wireless OSINT. This section provides a set of practical remedies for frequent issues, along with notes on hardware and software compatibility. By consulting this reference, analysts can minimize downtime and ensure smoother field operations.

---

### ⚠️ Common Issues and Fixes

**1. Wi-Fi Adapter Will Not Enter Monitor Mode**  
- **Cause:** Not all Wi-Fi adapters support monitor mode or packet injection.  
- **Fix:**  
  - Verify support with:  
    ```bash
    iw list | grep -A 10 "Supported interface modes"
    ```  
    Look for `* monitor`.  
  - If unsupported, replace the adapter with a known compatible chipset (see below).  

---

**2. Kismet Does Not Detect the Adapter**  
- **Cause:** Driver modules may not be loaded or permissions are insufficient.  
- **Fix:**  
  - Confirm the interface appears in `ip link`.  
  - Ensure the user is in the `netdev` group or run Kismet with `sudo`.  
  - Check driver availability; for example, Realtek chipsets often need out-of-tree drivers.  

---

**3. “Chasing Your Tail” Script Fails Due to Dependencies**  
- **Cause:** Missing Python libraries or incorrect environment.  
- **Fix:**  
  - Install requirements from the repository:  
    ```bash
    pip install -r requirements.txt
    ```  
  - Verify Python version ≥ 3.8.  
  - If SQLite bindings are missing, install via:  
    ```bash
    sudo apt install python3-sqlite
    ```  

---

**4. Raspberry Pi Performance Bottlenecks**  
- **Cause:** Kismet with GPS logging and multiple adapters can strain lower-end Pis.  
- **Fix:**  
  - Use Raspberry Pi 4 (2GB+ RAM).  
  - Disable non-essential logging modules.  
  - Offload analysis to a laptop after capture.  

---

### 🖥️ Hardware and Software Compatibility

**Recommended Wi-Fi Adapters (Monitor Mode & Injection Support):**  
- Alfa AWUS036NHA (Atheros AR9271 chipset, robust for field work).  
- Alfa AWUS036ACH (Realtek RTL8812AU, requires driver install).  
- TP-Link TL-WN722N v1 (Atheros AR9271; *avoid v2/v3*, which lack monitor mode).  

**Raspberry Pi Models:**  
- Raspberry Pi 4 Model B (best performance).  
- Raspberry Pi 3B+ (works, but limited under heavy load).  

**Linux Distributions:**  
- **Kali Linux (Debian-based):** Best supported for wireless security tools.  
- **Raspberry Pi OS Lite:** Lightweight, stable base for Kismet.  
- **Ubuntu Server for ARM:** Also compatible, but ensure latest kernel/driver packages are installed.  

---

## 📍 Placement in Document

Insert this **Troubleshooting** section **after** the current **“✅ Summary of the Workflow”**.  
This placement ensures readers finish the methodological workflow, then have immediate access to practical solutions if problems arise during replication.
