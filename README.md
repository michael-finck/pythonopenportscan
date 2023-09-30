+# Scan for Open Ports Script

This Python script demonstrates a basic port scanning technique for penetration testing.
It checks specified ports on a target host to determine if they are open or closed.

## Usage

1. Install Python (if not already installed) from [Python Official Website](https://www.python.org/).

2. Clone the repository or download the `openportscan.py` file.

3. Open the script and modify the target host and ports to scan as needed:
   ```python
   target_host = "example.com"  # Replace with the target host (IP or domain)
   ports_to_scan = [22, 80, 443, 8080]  # Ports to scan

Run the script:
python openportscan.py


Port Scanning

The port_scan() function in the script attempts to connect to each specified port on the target host.

    If a connection is successful, it indicates that the port is open.
    If a connection is unsuccessful, the port is considered closed.


In this README:

1. **Title and Description**: Provides an overview of the script's purpose and functionality.

2. **Usage**: Guides users on how to use the script, including installation, modifying the script for their specific use, and running the script.

3. **Port Scanning**: Explains the port scanning technique used in the script.

Feel free to modify and tailor this README to suit the specific needs and details of your project.
