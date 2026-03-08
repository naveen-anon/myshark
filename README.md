# 🦈 MyShark – Lightweight Network Analyzer

MyShark is a lightweight **Wireshark-style network analyzer** written in Python.  
It works in **Termux and Kali NetHunter (rootless)** environments and provides a hacker-style colorful terminal interface.

MyShark captures network packets and shows useful information such as:

- Source IP
- Destination IP
- Protocol type
- IP geolocation
- Live packet traffic

---

# ⚡ Features

- 📡 Live packet capture
- 🎯 Protocol filter (HTTP / DNS / TCP / UDP)
- 🌍 IP Geolocation lookup
- 💾 Save captured packets to **PCAP**
- 📊 Live traffic graph
- 💻 Hacker-style colorful terminal dashboard
- 📱 Works on **Termux and Kali NetHunter**

---

# 🗂 Project Structure

```
myshark/
 ├── myshark.py
 ├── filters.py
 ├── geoip.py
 ├── dashboard.py
 ├── savepcap.py
 ├── graph.py
 ├── requirements.txt
 └── install.sh
```

---

# ⚙️ Requirements

Python 3.8+

Libraries used:

- scapy
- rich
- requests
- matplotlib

---

# 📦 Installation

Clone the repository

```
git clone https://github.com/yourusername/myshark.git
```

Open project folder

```
cd myshark
```

Run installer

```
chmod +x install.sh
bash install.sh
```

---

# ▶️ Usage

Start MyShark

```
python myshark.py
```

Example output

```
[22:14:02] HTTP 192.168.1.5 ➜ 142.250.183.78 India - Delhi
[22:14:04] DNS 192.168.1.5 ➜ 8.8.8.8 USA - California
[22:14:06] TCP 192.168.1.5 ➜ 104.16.132.229 USA
```

Captured packets will be saved as

```
capture.pcap
```

You can open this file in **Wireshark** for deeper analysis.

---

# ⚠️ Disclaimer

This tool is created for **educational and ethical security research purposes only**.

Do not use this tool to monitor networks without proper authorization.

The developer is not responsible for misuse.

---

# 👨‍💻 Author

**naveen_anon**

---

# ⭐ Support

If you like this project, give it a **star on GitHub ⭐**
