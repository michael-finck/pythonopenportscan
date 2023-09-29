import socket

def port_scan(target_host, port):
    """
    Scans a specific port on a target host to check for open or closed status.

    Args:
        target_host (str): The target host (IPv4/IPv6 address or domain name).
        port (int): The port number to scan.

    Returns:
        str: Result indicating if the port is open, closed, or an error occurred.
    """
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout for the connection attempt

        # Attempt to connect to the target port
        sock.connect((target_host, port))
        sock.close()
        return f"Port {port} is open."

    except socket.error:
        return f"Port {port} is closed."

if __name__ == "__main__":
    target_host = "www.myexample.com"  # Replace with the target host (IP or domain)
    ports_to_scan = [22, 80, 443, 8080]  # Ports to scan

    for port in ports_to_scan:
        result = port_scan(target_host, port)
        print(result)
