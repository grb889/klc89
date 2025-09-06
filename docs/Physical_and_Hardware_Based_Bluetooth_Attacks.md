# **Chapter 2: Physical and Hardware-Based Bluetooth Attacks**

## **Table of Contents**
1. [Introduction to Hardware-Based Bluetooth Attacks](#introduction-to-hardware-based-bluetooth-attacks)  
2. [RF Signal Analysis with Software-Defined Radios](#rf-signal-analysis-with-software-defined-radios)  
3. [Hardware Sniffing with Ubertooth](#hardware-sniffing-with-ubertooth)  
4. [Advanced Hardware Attack Platforms](#advanced-hardware-attack-platforms)  
5. [Bluetooth Jamming and Denial of Service](#bluetooth-jamming-and-denial-of-service)  
6. [Physical Layer Attack Scenarios](#physical-layer-attack-scenarios)  
7. [Hardware-Based Post-Exploitation](#hardware-based-post-exploitation)  
8. [Countermeasures and Detection](#countermeasures-and-detection)  


## **Introduction to Hardware-Based Bluetooth Attacks**

Hardware-based Bluetooth attacks operate at the physical (RF) and link layers, providing capabilities that software-only approaches cannot achieve. These attacks can:

* **Capture encrypted traffic** during pairing exchanges  
* **Perform passive monitoring** without device interaction  
* **Execute jamming attacks** to disrupt communications  
* **Analyze RF characteristics** for device fingerprinting  
* **Bypass software-level security controls**

### **Key Hardware Platforms Overview**

| Platform | Frequency Range | Bluetooth Support | Cost Range | Use Cases |
| ----- | ----- | ----- | ----- | ----- |
| Ubertooth One | 2.4 GHz ISM | BR/EDR, BLE | $120-150 | Passive sniffing, jamming |
| HackRF One | 1 MHz \- 6 GHz | All (with software) | $300-400 | RF analysis, signal generation |
| BladeRF 2.0 | 47 MHz \- 6 GHz | All (with software) | $420-680 | High-performance SDR |
| LimeSDR | 100 kHz \- 3.8 GHz | All (with software) | $300-500 | Full-duplex operations |
| YARD Stick One | Sub-1 GHz | None (different bands) | $100-150 | IoT/Sub-GHz analysis |

## **RF Signal Analysis with Software-Defined Radios**

### **HackRF One Setup and Configuration**

#### **Initial Setup and Driver Installation**

\# Install HackRF drivers and tools  
sudo apt-get update  
sudo apt-get install hackrf libhackrf-dev hackrf-tools

\# Verify HackRF detection  
hackrf\_info

\# Update firmware if needed  
hackrf\_spiflash \-w hackrf\_one\_usb.bin

\# Test basic functionality  
hackrf\_transfer \-r test\_capture.bin \-f 2400000000 \-s 20000000 \-n 1000000

#### **GNU Radio Setup for Bluetooth Analysis**

\# Install GNU Radio and additional modules  
sudo apt-get install gnuradio gnuradio-dev gr-osmosdr

\# Install Bluetooth-specific GNU Radio blocks  
git clone https://github.com/greatscottgadgets/gr-bluetooth.git  
cd gr-bluetooth  
mkdir build && cd build  
cmake ..  
make \-j4  
sudo make install  
sudo ldconfig

\# Install additional analysis tools  
pip3 install matplotlib scipy numpy

### **Bluetooth Spectrum Analysis**

#### **Basic RF Spectrum Monitoring**

\#\!/usr/bin/env python3  
"""  
Bluetooth RF Spectrum Analyzer  
Monitors 2.4 GHz ISM band for Bluetooth activity  
"""

import numpy as np  
import matplotlib.pyplot as plt  
from gnuradio import gr, blocks, analog, filter  
from gnuradio import uhd  
import time  
import threading

class BluetoothSpectrumAnalyzer:  
    def \_\_init\_\_(self, center\_freq=2.44e9, sample\_rate=20e6, gain=30):  
        self.center\_freq \= center\_freq  
        self.sample\_rate \= sample\_rate  
        self.gain \= gain  
        self.fft\_size \= 2048  
        self.running \= False  
          
    def setup\_flowgraph(self):  
        """Setup GNU Radio flowgraph for spectrum analysis"""  
        self.tb \= gr.top\_block()  
          
        \# HackRF source  
        self.hackrf\_source \= osmosdr.source(args="hackrf=0")  
        self.hackrf\_source.set\_center\_freq(self.center\_freq)  
        self.hackrf\_source.set\_sample\_rate(self.sample\_rate)  
        self.hackrf\_source.set\_freq\_corr(0)  
        self.hackrf\_source.set\_gain(self.gain)  
          
        \# FFT and power calculation  
        self.fft \= filter.fft\_vcc(self.fft\_size, True, (), True)  
        self.c2mag2 \= blocks.complex\_to\_mag\_squared(self.fft\_size)  
        self.integrate \= blocks.integrate\_ff(1000, self.fft\_size)  
        self.sink \= blocks.vector\_sink\_f(self.fft\_size)  
          
        \# Connect blocks  
        self.tb.connect(self.hackrf\_source, self.fft, self.c2mag2,   
                       self.integrate, self.sink)  
      
    def analyze\_bluetooth\_channels(self):  
        """Analyze Bluetooth channel activity"""  
        \# Bluetooth channels: 2402 MHz \+ k MHz, k \= 0,1,2...78  
        bluetooth\_channels \= \[2402 \+ k for k in range(79)\]  
        channel\_power \= {}  
          
        print("Analyzing Bluetooth channel activity...")  
          
        for channel\_freq in bluetooth\_channels:  
            print(f"Scanning channel {channel\_freq \- 2402}: {channel\_freq} MHz")  
              
            \# Tune to channel frequency  
            self.hackrf\_source.set\_center\_freq(channel\_freq \* 1e6)  
            time.sleep(0.1)  \# Allow settling  
              
            \# Collect samples  
            self.tb.start()  
            time.sleep(1)  \# 1 second capture  
            self.tb.stop()  
              
            \# Calculate average power  
            data \= np.array(self.sink.data())  
            avg\_power \= np.mean(data) if len(data) \> 0 else 0  
            channel\_power\[channel\_freq \- 2402\] \= avg\_power  
              
            \# Clear sink for next iteration  
            self.sink.reset()  
          
        return channel\_power  
      
    def detect\_bluetooth\_devices(self):  
        """Detect active Bluetooth devices based on RF patterns"""  
        print("Starting Bluetooth device detection...")  
          
        \# Monitor frequency hopping patterns  
        hop\_sequence \= \[\]  
        detection\_time \= 30  \# seconds  
          
        start\_time \= time.time()  
        while time.time() \- start\_time \< detection\_time:  
            \# Quick scan across all channels  
            for channel in range(79):  
                freq \= (2402 \+ channel) \* 1e6  
                self.hackrf\_source.set\_center\_freq(freq)  
                  
                \# Brief capture  
                self.tb.start()  
                time.sleep(0.01)  \# 10ms  
                self.tb.stop()  
                  
                \# Check for activity  
                data \= np.array(self.sink.data())  
                if len(data) \> 0 and np.max(data) \> np.mean(data) \* 2:  
                    hop\_sequence.append((time.time(), channel))  
                  
                self.sink.reset()  
          
        return self.analyze\_hopping\_patterns(hop\_sequence)  
      
    def analyze\_hopping\_patterns(self, hop\_sequence):  
        """Analyze frequency hopping to identify devices"""  
        devices \= \[\]  
          
        if len(hop\_sequence) \< 10:  
            return devices  
          
        \# Group hops by time windows (625μs slots)  
        time\_windows \= {}  
        for timestamp, channel in hop\_sequence:  
            window \= int(timestamp \* 1600\)  \# 625μs slots  
            if window not in time\_windows:  
                time\_windows\[window\] \= \[\]  
            time\_windows\[window\].append(channel)  
          
        \# Identify potential piconets  
        for window, channels in time\_windows.items():  
            if len(channels) \> 5:  \# Minimum activity threshold  
                device \= {  
                    'timestamp': window / 1600.0,  
                    'channels': channels,  
                    'pattern\_strength': len(channels)  
                }  
                devices.append(device)  
          
        return devices

\# Usage example  
if \_\_name\_\_ \== "\_\_main\_\_":  
    analyzer \= BluetoothSpectrumAnalyzer()  
    analyzer.setup\_flowgraph()  
      
    \# Analyze channel activity  
    channel\_activity \= analyzer.analyze\_bluetooth\_channels()  
      
    \# Display results  
    active\_channels \= \[(ch, power) for ch, power in channel\_activity.items()   
                      if power \> np.mean(list(channel\_activity.values())) \* 1.5\]  
      
    print(f"\\nActive Bluetooth channels detected: {len(active\_channels)}")  
    for channel, power in active\_channels:  
        print(f"Channel {channel}: {power:.2e} power units")

#### **Advanced RF Fingerprinting**

\#\!/usr/bin/env python3  
"""  
Bluetooth Device RF Fingerprinting  
Identifies devices based on RF characteristics  
"""

import numpy as np  
import scipy.signal as signal  
from scipy.fft import fft, fftfreq  
import matplotlib.pyplot as plt

class BluetoothRFFingerprinter:  
    def \_\_init\_\_(self, sample\_rate=20e6):  
        self.sample\_rate \= sample\_rate  
        self.device\_signatures \= {}  
          
    def capture\_device\_signature(self, device\_mac, duration=10):  
        """Capture RF signature for a specific device"""  
        print(f"Capturing RF signature for device {device\_mac}")  
          
        \# This would interface with your SDR hardware  
        \# For example purposes, we'll simulate the process  
        signature\_data \= self.extract\_rf\_features(device\_mac, duration)  
        self.device\_signatures\[device\_mac\] \= signature\_data  
          
        return signature\_data  
      
    def extract\_rf\_features(self, device\_mac, duration):  
        """Extract RF fingerprinting features"""  
        features \= {}  
          
        \# Simulate RF capture \- in real implementation, this would  
        \# interface with HackRF or similar SDR  
          
        \# 1\. Carrier Frequency Offset (CFO)  
        features\['cfo'\] \= self.measure\_carrier\_offset(device\_mac)  
          
        \# 2\. I/Q Imbalance  
        features\['iq\_imbalance'\] \= self.measure\_iq\_imbalance(device\_mac)  
          
        \# 3\. Phase Noise Characteristics  
        features\['phase\_noise'\] \= self.measure\_phase\_noise(device\_mac)  
          
        \# 4\. Power Spectral Density  
        features\['psd'\] \= self.measure\_power\_spectrum(device\_mac)  
          
        \# 5\. Modulation Characteristics  
        features\['modulation'\] \= self.analyze\_modulation(device\_mac)  
          
        return features  
      
    def measure\_carrier\_offset(self, device\_mac):  
        """Measure carrier frequency offset"""  
        \# Placeholder for CFO measurement  
        \# In practice, this would analyze the received signal  
        \# to determine frequency offset from expected carrier  
        return np.random.normal(0, 1000\)  \# Hz offset  
      
    def measure\_iq\_imbalance(self, device\_mac):  
        """Measure I/Q imbalance characteristics"""  
        \# I/Q imbalance affects constellation  
        amplitude\_imbalance \= np.random.normal(0, 0.1)  
        phase\_imbalance \= np.random.normal(0, 0.05)  
          
        return {  
            'amplitude': amplitude\_imbalance,  
            'phase': phase\_imbalance  
        }  
      
    def measure\_phase\_noise(self, device\_mac):  
        """Analyze phase noise characteristics"""  
        \# Phase noise affects signal quality  
        close\_in\_noise \= np.random.normal(-80, 5\)  \# dBc/Hz  
        far\_out\_noise \= np.random.normal(-120, 10\)  \# dBc/Hz  
          
        return {  
            'close\_in': close\_in\_noise,  
            'far\_out': far\_out\_noise  
        }  
      
    def measure\_power\_spectrum(self, device\_mac):  
        """Analyze power spectral density"""  
        \# Create synthetic PSD for demonstration  
        freqs \= np.linspace(-10e6, 10e6, 1000\)  
          
        \# Bluetooth signal has characteristic spectral shape  
        center\_power \= np.random.normal(-30, 5\)  
        spectral\_rolloff \= np.random.normal(0.8, 0.1)  
          
        psd \= center\_power \- spectral\_rolloff \* np.abs(freqs) / 1e6  
          
        return {  
            'frequencies': freqs.tolist(),  
            'power': psd.tolist(),  
            'center\_power': center\_power,  
            'rolloff': spectral\_rolloff  
        }  
      
    def analyze\_modulation(self, device\_mac):  
        """Analyze modulation characteristics"""  
        \# Bluetooth uses GFSK modulation  
        modulation\_index \= np.random.normal(0.32, 0.05)  \# Typical for Bluetooth  
        symbol\_rate \= 1e6  \# 1 Msps for Bluetooth  
          
        return {  
            'type': 'GFSK',  
            'modulation\_index': modulation\_index,  
            'symbol\_rate': symbol\_rate  
        }  
      
    def compare\_signatures(self, signature1, signature2):  
        """Compare two RF signatures for similarity"""  
        similarity\_score \= 0  
        total\_features \= 0  
          
        \# Compare CFO  
        cfo\_diff \= abs(signature1\['cfo'\] \- signature2\['cfo'\])  
        cfo\_similarity \= max(0, 1 \- cfo\_diff / 5000\)  \# Normalize by 5kHz  
        similarity\_score \+= cfo\_similarity  
        total\_features \+= 1  
          
        \# Compare I/Q imbalance  
        iq\_diff \= abs(signature1\['iq\_imbalance'\]\['amplitude'\] \-   
                     signature2\['iq\_imbalance'\]\['amplitude'\])  
        iq\_similarity \= max(0, 1 \- iq\_diff / 0.5)  
        similarity\_score \+= iq\_similarity  
        total\_features \+= 1  
          
        \# Compare phase noise  
        phase\_diff \= abs(signature1\['phase\_noise'\]\['close\_in'\] \-   
                        signature2\['phase\_noise'\]\['close\_in'\])  
        phase\_similarity \= max(0, 1 \- phase\_diff / 20\)  
        similarity\_score \+= phase\_similarity  
        total\_features \+= 1  
          
        return similarity\_score / total\_features  
      
    def identify\_device(self, unknown\_signature, threshold=0.8):  
        """Identify device based on RF signature"""  
        best\_match \= None  
        best\_score \= 0  
          
        for known\_mac, known\_signature in self.device\_signatures.items():  
            score \= self.compare\_signatures(unknown\_signature, known\_signature)  
              
            if score \> best\_score:  
                best\_score \= score  
                best\_match \= known\_mac  
          
        if best\_score \> threshold:  
            return best\_match, best\_score  
        else:  
            return None, best\_score

\# Advanced spectrum analysis functions  
def analyze\_bluetooth\_interference():  
    """Analyze interference sources in 2.4 GHz band"""  
    interference\_sources \= {  
        'wifi\_channels': \[2412, 2437, 2462\],  \# MHz  
        'microwave': 2450,  
        'zigbee': \[2405, 2410, 2415, 2420, 2425, 2430, 2435, 2440, 2445, 2450,  
                  2455, 2460, 2465, 2470, 2475, 2480\]  
    }  
      
    print("Analyzing 2.4 GHz band interference...")  
      
    \# This would use actual SDR measurements  
    for source, frequencies in interference\_sources.items():  
        print(f"\\n{source.upper()} Analysis:")  
        if isinstance(frequencies, list):  
            for freq in frequencies:  
                print(f"  {freq} MHz: Analyzing...")  
        else:  
            print(f"  {frequencies} MHz: Analyzing...")

\# Signal jamming detection  
def detect\_jamming\_attacks():  
    """Detect potential jamming attacks on Bluetooth"""  
    print("Monitoring for Bluetooth jamming attacks...")  
      
    \# Monitor power levels across Bluetooth spectrum  
    normal\_noise\_floor \= \-90  \# dBm  
    jamming\_threshold \= \-60   \# dBm  
      
    \# This would interface with actual SDR hardware  
    for channel in range(79):  
        freq \= 2402 \+ channel  
        \# power\_level \= measure\_power\_at\_frequency(freq)  
        power\_level \= np.random.normal(-85, 10\)  \# Simulated  
          
        if power\_level \> jamming\_threshold:  
            print(f"WARNING: Potential jamming detected on channel {channel} "  
                  f"({freq} MHz): {power\_level:.1f} dBm")

## **Hardware Sniffing with Ubertooth**

### **Ubertooth One Setup and Configuration**

#### **Initial Setup**

\# Install Ubertooth tools  
sudo apt-get install ubertooth

\# Update Ubertooth firmware  
ubertooth-dfu \-d bluetooth\_rxtx.dfu

\# Verify installation  
ubertooth-util \-v

\# Basic spectrum analysis  
ubertooth-specan \-G

\# Start basic packet capture  
ubertooth-rx \-f capture.pcap

### **Passive Bluetooth Sniffing**

#### **Basic Packet Capture**

\#\!/bin/bash  
\# Comprehensive Ubertooth sniffing setup

echo "=== UBERTOOTH PASSIVE SNIFFING SETUP \==="

\# Step 1: Prepare capture environment  
CAPTURE\_DIR="bluetooth\_capture\_$(date \+%Y%m%d\_%H%M%S)"  
mkdir \-p $CAPTURE\_DIR  
cd $CAPTURE\_DIR

\# Step 2: Start spectrum analysis to identify active channels  
echo "Step 1: Analyzing spectrum for active channels..."  
ubertooth-specan \-G \> spectrum\_analysis.txt &  
SPECAN\_PID=$\!  
sleep 30  
kill $SPECAN\_PID

\# Step 3: Identify target devices  
echo "Step 2: Identifying target devices..."  
ubertooth-rx \-t 30 \> device\_discovery.txt

\# Parse discovered devices  
echo "Discovered devices:"  
grep \-E "(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}" device\_discovery.txt | sort \-u

\# Step 4: Start comprehensive packet capture  
echo "Step 3: Starting packet capture..."  
ubertooth-rx \-f bluetooth\_packets.pcap &  
RX\_PID=$\!

\# Step 5: BLE advertising packet capture  
echo "Step 4: Capturing BLE advertising packets..."  
ubertooth-btle \-f \-t 300 \> ble\_advertising.txt &  
BLE\_PID=$\!

echo "Capture running... Press Ctrl+C to stop"  
trap "kill $RX\_PID $BLE\_PID; exit" INT  
wait

#### **Advanced Sniffing with Filtering**

\#\!/usr/bin/env python3  
"""  
Advanced Ubertooth packet analysis and filtering  
"""

import subprocess  
import time  
import json  
import re  
from datetime import datetime

class UbertoothAdvancedSniffer:  
    def \_\_init\_\_(self, output\_dir="capture\_session"):  
        self.output\_dir \= output\_dir  
        self.target\_devices \= \[\]  
        self.capture\_filters \= {}  
          
    def setup\_capture\_session(self):  
        """Setup comprehensive capture session"""  
        subprocess.run(\['mkdir', '-p', self.output\_dir\])  
          
        \# Create session configuration  
        session\_config \= {  
            'start\_time': datetime.now().isoformat(),  
            'target\_devices': self.target\_devices,  
            'filters': self.capture\_filters  
        }  
          
        with open(f"{self.output\_dir}/session\_config.json", 'w') as f:  
            json.dump(session\_config, f, indent=2)  
      
    def discover\_active\_devices(self, duration=60):  
        """Discover active Bluetooth devices"""  
        print(f"Discovering devices for {duration} seconds...")  
          
        \# Run device discovery  
        cmd \= \['ubertooth-rx', '-t', str(duration)\]  
        result \= subprocess.run(cmd, capture\_output=True, text=True)  
          
        \# Parse MAC addresses from output  
        mac\_pattern \= r'(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}'  
        discovered\_macs \= re.findall(mac\_pattern, result.stdout)  
          
        \# Remove duplicates and store  
        unique\_macs \= list(set(\[''.join(mac) for mac in discovered\_macs\]))  
        self.target\_devices \= unique\_macs  
          
        print(f"Discovered {len(unique\_macs)} unique devices")  
        return unique\_macs  
      
    def capture\_pairing\_exchange(self, target\_mac=None, timeout=300):  
        """Capture Bluetooth pairing exchange"""  
        print("Monitoring for pairing exchanges...")  
          
        output\_file \= f"{self.output\_dir}/pairing\_capture.pcap"  
          
        if target\_mac:  
            \# Target specific device  
            cmd \= \['ubertooth-rx', '-f', output\_file, '-t', str(timeout)\]  
        else:  
            \# Monitor all devices  
            cmd \= \['ubertooth-rx', '-f', output\_file, '-t', str(timeout)\]  
          
        \# Start capture process  
        process \= subprocess.Popen(cmd, stdout=subprocess.PIPE,   
                                 stderr=subprocess.PIPE, text=True)  
          
        \# Monitor for pairing indicators  
        pairing\_detected \= False  
        start\_time \= time.time()  
          
        while time.time() \- start\_time \< timeout:  
            \# Check for pairing-related packets  
            if process.poll() is None:  \# Process still running  
                time.sleep(1)  
                \# In a real implementation, you'd parse the live output  
                \# to detect pairing-specific packet types  
            else:  
                break  
          
        process.terminate()  
        return output\_file  
      
    def analyze\_frequency\_hopping(self, target\_mac, duration=120):  
        """Analyze frequency hopping patterns"""  
        print(f"Analyzing frequency hopping for {target\_mac}")  
          
        hop\_log \= f"{self.output\_dir}/hopping\_analysis.txt"  
          
        \# Capture hopping sequence  
        cmd \= \['ubertooth-rx', '-t', str(duration)\]  
        process \= subprocess.Popen(cmd, stdout=subprocess.PIPE,   
                                 stderr=subprocess.PIPE, text=True)  
          
        hop\_sequence \= \[\]  
        for line in iter(process.stdout.readline, ''):  
            if target\_mac in line:  
                \# Extract channel information  
                \# This is simplified \- real implementation would parse  
                \# actual packet headers for channel information  
                timestamp \= time.time()  
                \# channel \= extract\_channel\_from\_packet(line)  
                channel \= hash(line) % 79  \# Simplified for example  
                hop\_sequence.append((timestamp, channel))  
          
        \# Analyze hopping pattern  
        return self.analyze\_hopping\_sequence(hop\_sequence)  
      
    def analyze\_hopping\_sequence(self, hop\_sequence):  
        """Analyze frequency hopping sequence for patterns"""  
        if len(hop\_sequence) \< 10:  
            return {"error": "Insufficient data for analysis"}  
          
        channels \= \[hop\[1\] for hop in hop\_sequence\]  
        timestamps \= \[hop\[0\] for hop in hop\_sequence\]  
          
        \# Calculate hop timing  
        hop\_intervals \= \[timestamps\[i+1\] \- timestamps\[i\]   
                        for i in range(len(timestamps)-1)\]  
          
        analysis \= {  
            'total\_hops': len(hop\_sequence),  
            'unique\_channels': len(set(channels)),  
            'avg\_hop\_interval': sum(hop\_intervals) / len(hop\_intervals),  
            'channel\_distribution': {ch: channels.count(ch) for ch in set(channels)}  
        }  
          
        return analysis  
      
    def capture\_ble\_advertising(self, duration=300):  
        """Capture BLE advertising packets"""  
        print("Capturing BLE advertising packets...")  
          
        output\_file \= f"{self.output\_dir}/ble\_advertising.txt"  
        cmd \= \['ubertooth-btle', '-f', '-t', str(duration)\]  
          
        with open(output\_file, 'w') as f:  
            subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE)  
          
        return self.parse\_ble\_advertising(output\_file)  
      
    def parse\_ble\_advertising(self, input\_file):  
        """Parse BLE advertising packets for device information"""  
        devices \= {}  
          
        with open(input\_file, 'r') as f:  
            for line in f:  
                if 'ADV\_IND' in line or 'ADV\_NONCONN\_IND' in line:  
                    \# Parse advertising packet  
                    \# This is simplified \- real parsing would handle  
                    \# the complete BLE advertising packet structure  
                      
                    \# Extract MAC address  
                    mac\_match \= re.search(r'(\[0-9A-F\]{2}:){5}\[0-9A-F\]{2}', line)  
                    if mac\_match:  
                        mac \= mac\_match.group(0)  
                          
                        if mac not in devices:  
                            devices\[mac\] \= {  
                                'first\_seen': time.time(),  
                                'packet\_count': 0,  
                                'advertisement\_types': set(),  
                                'rssi\_values': \[\]  
                            }  
                          
                        devices\[mac\]\['packet\_count'\] \+= 1  
                        devices\[mac\]\['last\_seen'\] \= time.time()  
                          
                        \# Extract RSSI if available  
                        rssi\_match \= re.search(r'RSSI:\\s\*(-?\\d+)', line)  
                        if rssi\_match:  
                            devices\[mac\]\['rssi\_values'\].append(int(rssi\_match.group(1)))  
          
        return devices

\# Example usage  
if \_\_name\_\_ \== "\_\_main\_\_":  
    sniffer \= UbertoothAdvancedSniffer("bluetooth\_analysis\_session")  
    sniffer.setup\_capture\_session()  
      
    \# Discover devices  
    devices \= sniffer.discover\_active\_devices(duration=30)  
      
    if devices:  
        print(f"\\nMonitoring devices: {devices}")  
          
        \# Capture pairing if available  
        pairing\_file \= sniffer.capture\_pairing\_exchange(timeout=60)  
          
        \# Analyze frequency hopping for first device  
        if devices:  
            hopping\_analysis \= sniffer.analyze\_frequency\_hopping(devices\[0\], duration=60)  
            print(f"\\nHopping analysis: {hopping\_analysis}")  
          
        \# Capture BLE advertising  
        ble\_devices \= sniffer.capture\_ble\_advertising(duration=60)  
        print(f"\\nBLE devices discovered: {len(ble\_devices)}")




