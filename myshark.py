#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP
import datetime

print("""
███╗   ███╗██╗   ██╗███████╗██╗  ██╗ █████╗ ██████╗ ██╗  ██╗
████╗ ████║╚██╗ ██╔╝██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
██╔████╔██║ ╚████╔╝ ███████╗███████║███████║██████╔╝█████╔╝
██║╚██╔╝██║  ╚██╔╝  ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗
██║ ╚═╝ ██║   ██║   ███████║██║  ██║██║  ██║██║  ██║██║  ██╗
╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

        MyShark Packet Analyzer
""")

def process_packet(packet):

    if IP in packet:

        src = packet[IP].src
        dst = packet[IP].dst
        proto = "OTHER"

        if TCP in packet:
            proto = "TCP"

        elif UDP in packet:
            proto = "UDP"

        elif ICMP in packet:
            proto = "ICMP"

        time = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"[{time}] {proto} {src}  --->  {dst}")


print("[+] Starting packet capture...\n")

sniff(prn=process_packet, store=False)
