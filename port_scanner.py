
**Code (port_scanner.py)**  
```python
import socket

# Function to scan ports
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} for open ports...")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target_ip, port)) == 0:  # Check if port is open
            print(f"Port {port} is open")
        s.close()

# Replace with the target IP address
target = "192.168.1.1"  
scan_ports(target, 1, 100)  # Scans ports 1 to 100
