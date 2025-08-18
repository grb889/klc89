# **🛰️ Advanced Wireless OSINT Workflow: A Comprehensive Guide**

This guide details a powerful, multi-tool workflow for conducting Open-Source Intelligence (OSINT) investigations using wireless signals. By combining a portable data capture device with advanced logging and analysis software, we can move beyond simple location data to build detailed behavioral profiles.

## **🔧 Tools of the Trade**

This workflow is built on a synergistic combination of hardware and software.

* **ESP32 Marauder:** A small, portable Wi-Fi and Bluetooth reconnaissance device. Its primary function in this workflow is to passively sniff and capture probe requests from nearby devices, logging their MAC addresses and SSID history.  
* **Raspberry Pi:** A versatile, low-cost microcomputer. It serves as a dedicated, mobile platform for running the data logging and analysis software.  
* **Kismet:** A powerful wireless network detector, packet sniffer, and intrusion detection system. It is the central hub for logging all captured wireless data into a structured database, which can be enriched with GPS coordinates if a module is connected.  
* **"Chasing Your Tail" Script:** A Python-based analysis tool designed to work with the Kismet database. It specializes in detecting the persistent presence of a device over time, a key indicator of surveillance or a targeted individual's routine. The GitHub repository for the script is **https://github.com/ArgeliusLabs/Chasing-Your-Tail-NG**.  
* **WiGLE.net:** A massive, crowdsourced database of wireless networks and their geographical locations. It is an invaluable resource for cross-referencing captured SSIDs with real-world locations.

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