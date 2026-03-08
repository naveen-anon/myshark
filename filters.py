from scapy.all import TCP, UDP, DNS, Raw

def detect_protocol(packet):

    if packet.haslayer(DNS):
        return "DNS"

    if packet.haslayer(TCP):

        if packet.haslayer(Raw):
            payload = str(packet[Raw].load)

            if "HTTP" in payload:
                return "HTTP"

        return "TCP"

    if packet.haslayer(UDP):
        return "UDP"

    return "OTHER"
