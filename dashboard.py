from rich.console import Console
from rich.table import Table

console = Console()

def show_packet(time, proto, src, dst, location):

    table = Table(title="MyShark Live Capture")

    table.add_column("Time")
    table.add_column("Protocol")
    table.add_column("Source")
    table.add_column("Destination")
    table.add_column("Geo")

    table.add_row(time, proto, src, dst, location)

    console.print(table)
