# Hikvision Camera Tester Documentation

Welcome to the official documentation for **Hikvision Camera Tester**!  
This tool allows you to test and monitor Hikvision cameras over **static IPs** with support for **port forwarding** and **digest authentication**.

---

## **Getting Started**

### **Installation**

There are two ways to use this tool:

#### **Option 1: Use the EXE File**

1. Download the latest EXE from the **[Releases](https://github.com/<your-username>/hikvision-camera-tester/releases)** section.
2. Double-click the EXE to run the tool.
3. Make sure your **firewall and antivirus** are not blocking the EXE.

#### **Option 2: Run the Python Script**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<your-username>/hikvision-camera-tester.git
   cd hikvision-camera-tester
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Python script**:
   ```bash
   python camera_gui.py
   ```

---

## **Usage Instructions**

1. **Open the application** (either the EXE or Python script).
2. Enter the **IP address**, **username**, and **password** for the Hikvision camera.
3. Click **Start Scan**.
4. The tool will:
   - Scan for **open ports** using Nmap.
   - Try to **authenticate** with the Hikvision API.
5. If successful, a **list of working cameras** will be displayed.

---

## **Nmap Installation**

- If **Nmap** is not installed, the tool will automatically attempt to install it.
- For manual installation, download Nmap from the [official site](https://nmap.org).

---

## **Troubleshooting**

- **EXE not running**: Make sure your **antivirus software** isn’t blocking the file.
- **Nmap installation failed**: Run the application with **administrator privileges**.
- **No cameras found**: Double-check your IP address, username, password, and port forwarding settings on the router.

---

## **Project Structure**

```
hikvision-camera-tester/
│
├── docs/                  # Documentation website
│   └── index.md           # Main documentation page
├── dist/                  # Contains the EXE file
├── scan.py                # Python script
├── README.md              # Project overview
├── LICENSE                # License file
├── requirements.txt       # Python dependencies
```

---

## **Contributing**

We welcome contributions from the community!

1. **Fork the repository**.
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Added a new feature"
   ```
4. **Push the changes**:
   ```bash
   git push origin feature-branch
   ```
5. **Create a pull request** on GitHub.

---

## **License**

This project is licensed under the **MIT License**.  
See the [LICENSE](https://github.com/<your-username>/hikvision-camera-tester/blob/main/LICENSE) file for more details.

---

## **Acknowledgments**

- **[Hikvision](https://www.hikvision.com/)** for their camera API documentation.
- **[Nmap](https://nmap.org/)** for providing a powerful network scanner.
- **Tkinter** for the GUI framework.

---

## **Contact**

For questions or issues, open an **[issue on GitHub](https://github.com/<your-username>/hikvision-camera-tester/issues)**.

---

**Keywords**: Hikvision, IP Camera, Port Scanning, Nmap, Security Camera, Static IP, Router Port Forwarding, Python, EXE, Digest Authentication
