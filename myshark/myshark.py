#!/usr/bin/env python3
import argparse

from myshark.core.banner import show
from myshark.core.offline import analyze
from myshark.modules import dns, http, tls


def main():
    show()

    parser = argparse.ArgumentParser(
        description="MYSHARK – Hacker Style Offline Wireshark CLI"
    )

    parser.add_argument(
        "mode",
        choices=["analyze", "dns", "http", "tls"],
        help="Analysis mode"
    )

    parser.add_argument(
        "pcap",
        help="PCAP file for offline analysis"
    )

    args = parser.parse_args()

    if args.mode == "analyze":
        analyze(args.pcap)
    elif args.mode == "dns":
        dns.show(args.pcap)
    elif args.mode == "http":
        http.show(args.pcap)
    elif args.mode == "tls":
        tls.show(args.pcap)


if __name__ == "__main__":
    main()
