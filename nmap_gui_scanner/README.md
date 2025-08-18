# NexusSec GUI Nmap Scanner

## 🛠 What This Is
A GUI-based Nmap scanner built with Python and Tkinter, capable of scanning hosts and exporting results in JSON format.

## 🚀 How to Use

### Prerequisites
- Python 3.x
- Nmap installed (`sudo apt install nmap` or [Nmap Download](https://nmap.org/download.html))

### Run the Scanner
```bash
python scanner_gui.py
```

### Available Scan Types
- **Comprehensive**: Full TCP scan (1–65535), OS detection, service version.
- **Fast**: Top 1024 TCP ports.
- **UDP**: UDP scan of ports 1–1024.
- **Vuln Scan**: Uses NSE `vuln` scripts to find known vulnerabilities.
- **Aggressive**: Version detection, OS detection, traceroute, and scripts.

## 🔍 Understanding Results

The JSON file will contain entries like:
```json
{
  "ports": [
    {
      "port": "80",
      "protocol": "tcp",
      "state": "open",
      "service": "http"
    }
  ]
}
```

### 🚩 What to Look For

- **Open Ports**: Services running and potentially exposed.
- **High Ports (1024+)**: Might be admin panels or internal apps.
- **Services with Vulnerabilities**: Use `Vuln Scan` to detect known issues.

### 🛡️ Potential Weakness Indicators

| Indicator         | Meaning                                 |
|------------------|------------------------------------------|
| `state: open`     | Port is exposed                         |
| `service: unknown`| Possibly misconfigured or nonstandard   |
| UDP ports         | Often exploited due to lack of filtering|
| Version banners   | Can reveal outdated software            |

Always get permission before scanning targets!

## 📂 Output Location
Scan results are saved as JSON in the `results/` folder.

---

Developed by NexusSec.
