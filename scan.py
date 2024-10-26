import subprocess
import os
import platform
import requests
import threading
from requests.auth import HTTPDigestAuth
from lxml import etree
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Progressbar

# Constants
API_ENDPOINT = "/ISAPI/System/deviceInfo"

def install_nmap():
    """Check if Nmap is installed. If not, install it."""
    try:
        subprocess.run(["nmap", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        if platform.system() == "Windows":
            download_and_install_nmap()
        elif platform.system() in ["Linux", "Darwin"]:
            os.system("sudo apt-get update && sudo apt-get install nmap -y")
        else:
            messagebox.showerror("Error", "Unsupported platform. Please install Nmap manually.")
            return

def download_and_install_nmap():
    """Download and install Nmap silently on Windows."""
    nmap_url = "https://nmap.org/dist/nmap-7.94-setup.exe"
    installer_path = os.path.join(os.getcwd(), "nmap_installer.exe")

    response = requests.get(nmap_url, stream=True)
    with open(installer_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    subprocess.run([installer_path, "/S"], check=True)
    os.remove(installer_path)
    messagebox.showinfo("Info", "Nmap installed. Restart the application if necessary.")

def scan_open_ports(ip):
    """Scan the given IP address for open ports using Nmap."""
    try:
        result = subprocess.run(["nmap", "-sS", "-p-", ip], stdout=subprocess.PIPE, text=True)
        return parse_nmap_output(result.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to scan ports: {e}")
        return []

def parse_nmap_output(output):
    """Parse Nmap output to extract open ports."""
    open_ports = []
    for line in output.splitlines():
        if "open" in line:
            try:
                port = int(line.split("/")[0])
                open_ports.append(port)
            except ValueError:
                continue
    return open_ports

def test_camera(ip, port, username, password):
    """Test the camera API on a given IP and port with provided credentials."""
    url = f"http://{ip}:{port}{API_ENDPOINT}"
    try:
        response = requests.get(url, auth=HTTPDigestAuth(username, password), timeout=5)
        if response.status_code == 200:
            return parse_device_info(response.content)
    except requests.RequestException as e:
        print(f"Error connecting to {url}: {e}")
    return None

def parse_device_info(xml_content):
    """Parse XML content to extract the device name."""
    try:
        root = etree.fromstring(xml_content)
        ns = {'ns': 'http://www.hikvision.com/ver20/XMLSchema'}
        device_name = root.find('ns:deviceName', ns).text
        return device_name
    except Exception as e:
        print(f"Error parsing XML: {e}")
    return None

def start_scan_thread():
    """Start the scanning process in a background thread."""
    thread = threading.Thread(target=start_scan)
    thread.start()

def start_scan():
    """Main scanning logic."""
    ip = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not ip or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    scan_button.config(state=tk.DISABLED)
    progress_bar.start()

    install_nmap()
    open_ports = scan_open_ports(ip)

    working_cameras = []
    for i, port in enumerate(open_ports):
        update_progress(i + 1, len(open_ports))
        device_name = test_camera(ip, port, username, password)
        if device_name:
            working_cameras.append(f"{device_name} is working at {ip}:{port}")

    progress_bar.stop()
    scan_button.config(state=tk.NORMAL)

    display_results(working_cameras)

def update_progress(current, total):
    """Update the progress bar."""
    progress = int((current / total) * 100)
    progress_bar["value"] = progress

def display_results(cameras):
    """Display the list of working cameras."""
    result_box.config(state=tk.NORMAL)
    result_box.delete(1.0, tk.END)

    if cameras:
        result_box.insert(tk.END, "\n".join(cameras))
    else:
        result_box.insert(tk.END, "No working cameras found.")

    result_box.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Camera Port Scanner")

tk.Label(root, text="Enter IP Address:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=2, column=1, padx=5, pady=5)

scan_button = tk.Button(root, text="Start Scan", command=start_scan_thread)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

progress_bar = Progressbar(root, mode="determinate", length=300)
progress_bar.grid(row=4, column=0, columnspan=2, pady=10)

result_box = scrolledtext.ScrolledText(root, width=50, height=10, state=tk.DISABLED)
result_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
