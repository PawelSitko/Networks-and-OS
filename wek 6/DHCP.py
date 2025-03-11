# dhcp_simple.py - Simplified DHCP Simulator

# Server Configuration
server = {
    "ip_pool": ["192.168.1.100", "192.168.1.101", "192.168.1.102"],
    "leases": {}
}

# Client Configuration
clients = [
    {"mac": "AA:BB:CC:DD:EE:FF", "ip": None},
    {"mac": "11:22:33:44:55:66", "ip": None},
    {"mac": "77:88:99:AA:BB:CC", "ip": None},
]

def send_discover(client):
    """Step 1: Client sends a DHCP DISCOVER message."""
    print(f"\n[CLIENT {client['mac']}] Step 1: Sending DHCP DISCOVER")
    return {
        "type": "DISCOVER",
        "mac": client["mac"]
    }

def make_offer(discover):
    """Step 2: Server responds with a DHCP OFFER message."""
    print(f"\n[SERVER] Step 2: Making DHCP OFFER for {discover['mac']}")
    if not server["ip_pool"]:
        print("No IPs available!")
        return None

    offered_ip = server["ip_pool"].pop(0)  # Assign first available IP
    return {
        "type": "OFFER",
        "mac": discover["mac"],
        "ip": offered_ip
    }

def send_request(offer):
    """Step 3: Client sends a DHCP REQUEST message."""
    print(f"\n[CLIENT {offer['mac']}] Step 3: Sending DHCP REQUEST for {offer['ip']}")
    return {
        "type": "REQUEST",
        "mac": offer["mac"],
        "ip": offer["ip"]
    }

def send_ack(request):
    """Step 4: Server sends a DHCP ACK message."""
    print(f"\n[SERVER] Step 4: Sending DHCP ACK for {request['mac']}")
    server["leases"][request["mac"]] = request["ip"]
    return {
        "type": "ACK",
        "mac": request["mac"],
        "ip": request["ip"]
    }

def main():
    """Runs the DHCP Simulation for multiple clients"""
    print("=== Simple DHCP Simulation ===")

    for client in clients:
        # Step 1: Client starts process
        discover = send_discover(client)

        # Step 2: Server responds
        offer = make_offer(discover)
        if not offer:
            print(f"No available IP for {client['mac']}.")
            continue

        # Step 3: Client continues
        request = send_request(offer)

        # Step 4: Server finalizes
        ack = send_ack(request)

        # Update client IP
        client["ip"] = ack["ip"]

        print("\n=== Result ===")
        print(f"Client {client['mac']} got IP: {client['ip']}")
    
    print("\n=== Final Server Leases ===")
    print(server["leases"])

if __name__ == "__main__":
    main()
