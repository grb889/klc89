#scanner_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import os
import xml.etree.ElementTree as ET
from threading import Thread
from queue import Queue
from scanner_core import resolve_target, get_scan_command, run_nmap, save_output_json

os.makedirs("results", exist_ok=True)

def parse_nmap_xml(xml_data):
    result = {"ports": []}
    try:
        root = ET.fromstring(xml_data)
        for host in root.findall('host'):
            for port in host.findall(".//port"):
                port_id = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service = port.find('service').get('name')
                result["ports"].append({
                    "port": port_id,
                    "protocol": protocol,
                    "state": state,
                    "service": service
                })
    except Exception as e:
        result["error"] = str(e)
    return result

def on_scan():
    target = target_entry.get().strip()
    scan_type = scan_option.get()
    resolved = resolve_target(target)

    if not resolved:
        messagebox.showerror("Invalid Target", "Could not resolve domain/IP.")
        return

    command = get_scan_command(target, scan_type)
    if not command:
        messagebox.showerror("Invalid Scan", "Scan option not recognized.")
        return

    status_label.config(text="Running scan...", foreground="blue")
    scan_button.config(state=tk.DISABLED) # Disable button while scanning
    
    # Use a queue to get results back from the thread
    result_queue = Queue()
    
    # Start the scan in a separate thread
    scan_thread = Thread(target=run_scan_thread, args=(command, result_queue))
    scan_thread.start()
    
    # Start a check for the thread's completion
    window.after(100, check_scan_status, scan_thread, result_queue)

def run_scan_thread(command, result_queue):
    xml_output = run_nmap(command)
    result_queue.put(xml_output)

def check_scan_status(thread, queue):
    if thread.is_alive():
        window.after(100, check_scan_status, thread, queue)
    else:
        xml_output = queue.get()
        if not xml_output:
            status_label.config(text="Scan failed.", foreground="red")
            scan_button.config(state=tk.NORMAL)
            return

        parsed = parse_nmap_xml(xml_output)
        json_path = save_output_json(parsed)

        output_text.delete("1.0", tk.END)
        for item in parsed.get("ports", []):
            output_text.insert(tk.END, f"{item['port']}/{item['protocol']} - {item['state']} - {item['service']}\n")

        status_label.config(text=f"Scan complete. Saved to {json_path}", foreground="green")
        scan_button.config(state=tk.NORMAL) # Re-enable the button

window = tk.Tk()
window.title("NexusSec GUI Nmap Scanner")
window.geometry("700x500")

tk.Label(window, text="Target (IP or domain):").pack(pady=5)
target_entry = tk.Entry(window, width=50)
target_entry.pack(pady=5)

tk.Label(window, text="Scan Type:").pack(pady=5)
scan_option = ttk.Combobox(window, values=["Comprehensive", "Fast", "UDP", "Vuln Scan", "Aggressive"])
scan_option.pack(pady=5)
scan_option.current(0)

scan_button = tk.Button(window, text="Run Scan", command=on_scan, bg="darkgreen", fg="white")
scan_button.pack(pady=10)

output_text = tk.Text(window, wrap="word", height=15)
output_text.pack(padx=10, pady=10, fill="both", expand=True)

status_label = tk.Label(window, text="", fg="blue")
status_label.pack(pady=5)

window.mainloop()