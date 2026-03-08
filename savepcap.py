from scapy.utils import wrpcap

packets = []

def save_packet(packet):
    packets.append(packet)

def save_file():
    wrpcap("capture.pcap", packets)
    print("[+] Packets saved to capture.pcap")
