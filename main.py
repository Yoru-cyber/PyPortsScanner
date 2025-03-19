import socket
import sys
import re
def scan_ports(start_port, stop_port, address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        for port in range(start_port, stop_port+1):
            try:
               conn = s.connect_ex((address,port))
               print(conn)
               if conn == 0:
                   print(f'{port} is open')
               else:
                   print(f'{port} is closed')
            except socket.error:
                print('Error on connection')

def isIpValid(ip: str):
    validIpv4 = re.search(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}", ip)
    if validIpv4 is not None:
        return True
    return False
def isValidDomain(domain: str):
    validDomain = re.search(r"^(((?!-))(xn--|_)?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$", domain)
    if validDomain is not None:
        return True
    return False
    
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("No arguments provided")
        exit()
    arg = args[1]
    if arg != "" or None:
        ipValid = isIpValid(arg)
        if ipValid is True:
            scan_ports(22, 443, arg)
        domainValid = isValidDomain(arg)
        if domainValid is True:
            scan_ports(440, 443, arg)
        else:
            print("No valid arguments")
            exit()
