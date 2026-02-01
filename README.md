# 🦈 MYSHARK

**Offline Wireshark-Style Network Analyzer (CLI)**  
A hacker-friendly, terminal-based PCAP analysis tool built with Python & TShark.  
Designed for **Kali Linux, NetHunter, Termux (offline analysis)**.

---

## 🔥 Why MYSHARK?

Most tools need GUI or heavy setup.  
**MYSHARK works fully in terminal**, focuses on **PCAP analysis**, and feels like a **SOC / hacker console**.

---

## 🚀 Features

- 📦 Offline PCAP analysis (no live sniff required)
- 📊 Protocol analysis (DNS / HTTP / TLS)
- 📄 Auto report generation (TXT + JSON)
- 🛡️ Scan & suspicious behavior detection (basic)
- 🧩 Modular structure (easy to extend)
- ⚡ Lightweight & fast
- 🐧 Works on Kali Linux & NetHunter

---

## 📦 Installation

### Clone repository
```bash
git clone https://github.com/naveen-anon/myshark.git
cd myshark
```
### Requirements
Python 3.x
tshark (Wireshark CLI)
Install tshark on Kali:
> - sudo apt install tshark

## 🛠 Usage

> - myshark <mode> <pcap_file>
Available Modes
Mode
Description
analyze
Full PCAP overview & summary
dns
Extract DNS queries
http
Extract HTTP hosts & URIs
tls
TLS metadata (SNI / cert info)
### 🧪 Example 
Analyze full PCAP:
> - myshark analyze traffic.pcap
**DNS** analysis:
> - myshark dns traffic.pcap
**HTTP** traffic:
> - myshark http web.pcap
**TLS** sessions:
> - myshark tls secure.pcap
## 📄 Reports
After analysis, MYSHARK can generate:
report.txt → Human readable
report.json → Machine readable
Report includes:
Protocol counts
Top IPs
Packet statistics
Conversations summary
## 📁 Project Structure

myshark/
├── myshark/
│   ├── core/        # Engine & analyzers
│   ├── modules/     # DNS / HTTP / TLS modules
│   ├── utils/       # Colors, helpers
│   └── detectors/   # Scan / attack detection (future)
├── setup.py
├── README.md
└── requirements.txt
## ⚠️ Limitations
Live sniffing depends on system permissions
Best suited for offline PCAP analysis
Advanced detection modules are WIP
## 🤝 Contributing
Contributions are welcome!
Fork the repo
Add new modules / detectors
Improve reports
Submit a pull request
## 📜 License
MIT License
Free to use, modify, and distribute.
## 👨‍💻 Author
naveen-anon
GitHub: https://github.com/naveen-anon
MYSHARK — Think like a SOC analyst, work like a hacker 🦈
