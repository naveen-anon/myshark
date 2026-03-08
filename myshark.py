from scapy.all import sniff, IP
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from filters import detect_protocol
from geoip import get_location
from dashboard import show_packet
from savepcap import save_packet
from graph import update_graph

console = Console()

packet_count = 0


banner = Text("""
███╗   ███╗██╗   ██╗███████╗██╗  ██╗ █████╗ ██████╗ ██╗  ██╗
████╗ ████║╚██╗ ██╔╝██╔════╝██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
██╔████╔██║ ╚████╔╝ ███████╗███████║███████║██████╔╝█████╔╝
██║╚██╔╝██║  ╚██╔╝  ╚════██║██╔══██║██╔══██║██╔══██╗██╔═██╗
██║ ╚═╝ ██║   ██║   ███████║██║  ██║██║  ██║██║  ██║██║  ██╗
╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
""", style="bold green")

console.print(Panel(banner, title="[red]MyShark v2[/red]", subtitle="[cyan]Network Packet Analyzer[/cyan]"))


def process(packet):

    global packet_count

    if IP in packet:

        src = packet[IP].src
        dst = packet[IP].dst

        proto = detect_protocol(packet)
        location = get_location(src)

        time = datetime.datetime.now().strftime("%H:%M:%S")

        proto_color = {
            "HTTP": "yellow",
            "DNS": "cyan",
            "TCP": "green",
            "UDP": "magenta",
            "OTHER": "white"
        }

        color = proto_color.get(proto, "white")

        console.print(
            f"[bold blue]{time}[/bold blue] "
            f"[{color}]{proto}[/{color}] "
            f"[green]{src}[/green] ➜ "
            f"[red]{dst}[/red] "
            f"[dim]{location}[/dim]"
        )

        save_packet(packet)

        packet_count += 1
        update_graph(packet_count)


console.print("[bold green][+] Starting packet capture...[/bold green]\n")

sniff(prn=process, store=False)
