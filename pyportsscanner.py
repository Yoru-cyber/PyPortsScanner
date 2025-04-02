import argparse
import socket

from rich import print
from rich.console import Console
from rich.table import Table


def scan_ports(start_port: int, stop_port: int, address):
    table = Table(title="Results")
    table.add_column("Port", justify="right", style="cyan", no_wrap=True)
    table.add_column("State", justify="right", no_wrap=True)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        for port in range(start_port, stop_port + 1):
            try:
                # Check for type _Address
                conn = s.connect_ex((address, port))
                if conn == 0:
                    print(f"port [green]{port}[/green] is open")
                    table.add_row(f"{port}", f"[green]{True}[/green]")
                else:
                    print(f"port [red]{port}[/red] is closed")
                    table.add_row(f"{port}", f"[red]{False}[/red]")
            except socket.error:
                print("Error on connection")
    console = Console()
    console.print(table)


# USELESS
# def isIpValid(ip: str):
#    validIpv4 = re.search(
#        r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}",
#        ip,
#    )
#    if validIpv4 is not None:
#        return True
#    return False
#
#
# def isValidDomain(domain: str):
#    validDomain = re.search(
#        r"^(((?!-))(xn--|_)?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$",
#        domain,
#    )
#    if validDomain is not None:
#        return True
#    return False


if __name__ == "__main__":
    console = Console()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ip_domain", help="The domain or IPv4 to test"
    )  # pyright: ignore[reportUnusedCallResult]
    parser.add_argument(
        "start_port",
        help="Port value where the scanning will start. Default: 22",
        default=22,
        type=int,
    )  # pyright: ignore[reportUnusedCallResult]
    parser.add_argument(
        "stop_port",
        help="Port value where the scanning will stop. Default: 80",
        default=80,
        type=int,
    )  # pyright: ignore[reportUnusedCallResult]
    args = parser.parse_args()
    with console.status("[bold magenta]Running...") as status:
        scan_ports(args.start_port, args.stop_port, args.ip_domain)
    exit()
