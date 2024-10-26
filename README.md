# Hikvision Camera Tester

![Project Banner](https://img.shields.io/badge/Hikvision-Camera%20Tester-brightgreen)  
A simple tool to **scan Hikvision cameras** over **static IPs** with **port forwarding enabled on the router**. This project provides a GUI application for testing cameras, checking their status, and displaying open ports using **Nmap** and **Digest Authentication**.

## Features

- **Port scanning** with Nmap for any given IP.
- **Digest authentication support** for Hikvision devices.
- **Tkinter-based GUI** for easy usage.
- Automatic **Nmap installation** if missing.
- Generates a list of **working cameras**.

## Requirements

- Windows 10/11 (for the EXE version)  
- Python 3.12+ (for the script version)  
- Administrator rights (if Nmap installation is triggered)

## Installation

### 1. Download the EXE  
You can download the standalone EXE from the **[Releases](https://github.com/<your-username>/hikvision-camera-tester/releases)** section.

### 2. Run the Python Script

To run the Python script manually:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/hikvision-camera-tester.git
   cd hikvision-camera-tester
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python camera_gui.py
   ```

## How It Works

1. **Provide the IP address, username, and password**.
2. The app **scans open ports** using Nmap.
3. It tries to **authenticate with Hikvision's API**.
4. If successful, it **displays the list of working cameras** in the GUI.

## Documentation

Full documentation can be found **[here](https://<your-username>.github.io/hikvision-camera-tester/)**.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hikvision API Documentation](https://www.hikvision.com)
- [Nmap Network Scanner](https://nmap.org/)

---

**Keywords**: Hikvision, camera tester, IP camera, Nmap, port scanning, router port forwarding, digest authentication, security cameras, static IP, Python EXE



