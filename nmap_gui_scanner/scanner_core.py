#scanner_core.py
import subprocess
import json
import datetime
import socket

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

def get_scan_command(target, option):
    commands = {
        "Comprehensive": ['nmap', '-Pn', '-sS', '-sV', '-O', '-p', '1-65535', '-T4', target],
        "Fast": ['nmap', '-Pn', '-sS', '-sV', '-p', '1-1024', '-T3', target],
        "UDP": ['nmap', '-Pn', '-sU', '-sV', '-p', '1-1024', target],
        "Vuln Scan": ['nmap', '-Pn', '--script', 'vuln', target],
        "Aggressive": ['nmap', '-Pn', '-sS', '-sV', '-p', '1-65535', '-T5', '-A', target],
    }
    return commands.get(option, None)

def run_nmap(command):
    try:
        result = subprocess.run(command + ['-oX', '-'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None

def save_output_json(parsed_data, filename="scan_result"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"results/{filename}_{timestamp}.json"
    with open(filepath, "w") as f:
        json.dump(parsed_data, f, indent=4)
    return filepath