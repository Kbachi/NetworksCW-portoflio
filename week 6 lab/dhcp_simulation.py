# DHCP Simulation

# Server Configuration
dhcp_server = {
    "ip_pool": ["192.168.1.100", "192.168.1.101", "192.168.1.102"],
    "leases": {}
}

# Client Configuration
dhcp_client = {
    "mac": "AA:BB:CC:DD:EE:FF",
    "ip": None
}

def send_discover():
    print("\n[CLIENT] Sending DHCP DISCOVER")
    return {"type": "DISCOVER", "mac": dhcp_client["mac"]}

def make_offer(discover):
    print("\n[SERVER] Sending DHCP OFFER")
    if not dhcp_server["ip_pool"]:
        print("No IP addresses available!")
        return None
    offered_ip = dhcp_server["ip_pool"].pop(0)
    return {"type": "OFFER", "mac": discover["mac"], "ip": offered_ip}

def send_request(offer):
    print("\n[CLIENT] Sending DHCP REQUEST")
    return {"type": "REQUEST", "mac": offer["mac"], "ip": offer["ip"]}

def send_ack(request):
    print("\n[SERVER] Sending DHCP ACK")
    dhcp_server["leases"][request["mac"]] = request["ip"]
    return {"type": "ACK", "mac": request["mac"], "ip": request["ip"]}

def main():
    print("=== Simple DHCP Simulation ===")
    
    # Client initiates DHCP process
    discover = send_discover()
    offer = make_offer(discover)
    if not offer:
        return
    
    request = send_request(offer)
    ack = send_ack(request)
    
    # Assign IP to the client
    dhcp_client["ip"] = ack["ip"]
    
    print("\n=== DHCP Lease Result ===")
    print(f"Client {dhcp_client['mac']} obtained IP: {dhcp_client['ip']}")
    print("Current Server Leases:", dhcp_server["leases"])

if __name__ == "__main__":
    main()
