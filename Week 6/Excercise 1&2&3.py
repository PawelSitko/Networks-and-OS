import ipaddress
import socket

def analyse_ip(ip_str):
    """Analyse an IP address and provide network details."""
    try:
        # Create an IP network object with strict=False to allow host addresses
        network = ipaddress.ip_network(ip_str, strict=False)

        print("\n===== IP Address Analysis =====")
        print(f"Address: {network.network_address}")
        print(f"Network: {network}")
        print(f"Netmask: {network.netmask}")
        print(f"Broadcast Address: {network.broadcast_address}")

        # Calculate first and last usable host
        hosts = list(network.hosts())  # Get all host addresses
        if hosts:
            print(f"First Usable Host: {hosts[0]}")
            print(f"Last Usable Host: {hosts[-1]}")
        else:
            print("No usable hosts (this is a /31 or /32 subnet).")

        # Number of usable hosts
        num_usable_hosts = len(hosts)
        print(f"Number of Usable Hosts: {num_usable_hosts}")

        # Check if the IP is private or public
        is_private = network.network_address.is_private
        is_global = network.network_address.is_global
        print(f"Is Private: {is_private}")
        print(f"Is Public (Global): {is_global}")

        # List all hosts in the network (only for small networks)
        if network.num_addresses < 256:
            print("\nHosts in network:")
            for host in hosts:
                print(host)

    except ValueError:
        print("Invalid IP address format. Please provide a valid IPv4 address with CIDR.")

# ===== Exercise 2: Analyse your own device's IP Address =====
def get_local_ip():
    """Retrieve the local machine's IP address and analyze it."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\n===== Local Device IP Analysis =====")
    print(f"Your Computer Name: {hostname}")
    print(f"Your Local IP Address: {local_ip}")

    # Convert local IP to CIDR format (assuming /24 subnet for local networks)
    local_ip_cidr = f"{local_ip}/24"
    analyse_ip(local_ip_cidr)

# ===== Exercise 3: Get University Website IP Address and Analyse It =====
def get_website_ip(domain):
    """Retrieve the IP address of a given website and analyze it."""
    try:
        website_ip = socket.gethostbyname(domain)
        print(f"\n===== {domain} IP Analysis =====")
        print(f"Website IP Address: {website_ip}")

        # Convert website IP to CIDR format (assuming default /24 subnet)
        website_ip_cidr = f"{website_ip}/24"
        analyse_ip(website_ip_cidr)

    except socket.gaierror:
        print(f"Could not resolve the IP address of {domain}. Check your internet connection.")

# ===== RUN EXERCISES =====
# Exercise 1: Analyze a given IP
analyse_ip('192.168.1.1/24')

# Exercise 2: Analyze your own IP
get_local_ip()

# Exercise 3: Analyze the university website IP (change domain as needed)
get_website_ip('gold.ac.uk')
