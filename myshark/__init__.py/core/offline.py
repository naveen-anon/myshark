from myshark.core.engine import run
from myshark.utils.colors import G, W
def analyze(pcap):
    print(G + f"[+] Analyzing PCAP → {pcap}\n" + W)
    run(["tshark", "-r", pcap])
  
