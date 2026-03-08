#!/bin/bash

echo "[+] Installing MyShark dependencies..."

pkg update -y
pkg install python -y

pip install scapy

echo "[+] Installation complete"
echo "Run with: python myshark.py"
