import ipaddress

def analyse_ip(ip_str1, ip_str2):
    # Create IP interface objects
    ip1 = ipaddress.ip_interface(ip_str1)
    ip2 = ipaddress.ip_interface(ip_str2)
    
    print(f"Address 1: {ip1.ip}")
    print(f"Network 1: {ip1.network}")
    print(f"Netmask 1: {ip1.netmask}")
    print(f"Is private 1: {ip1.ip.is_private}")
    print(f"Is global 1: {ip1.ip.is_global}")
    
    print(f"\nAddress 2: {ip2.ip}")
    print(f"Network 2: {ip2.network}")
    print(f"Netmask 2: {ip2.netmask}")
    print(f"Is private 2: {ip2.ip.is_private}")
    print(f"Is global 2: {ip2.ip.is_global}")
    
    # Compare networks
    if ip1.network == ip2.network:
        print("\nBoth IP addresses belong to the same network.")
    else:
        print("\nThe IP addresses belong to different networks.")
    
    # Calculate broadcast address for both networks
    broadcast_address1 = ip1.network.broadcast_address
    broadcast_address2 = ip2.network.broadcast_address
    print(f"\nBroadcast address 1: {broadcast_address1}")
    print(f"Broadcast address 2: {broadcast_address2}")
    
    # Calculate first and last usable host addresses for both networks
    hosts1 = list(ip1.network.hosts())
    hosts2 = list(ip2.network.hosts())
    
    if hosts1:
        first_usable1 = hosts1[0]
        last_usable1 = hosts1[-1]
        print(f"\nFirst usable host address 1: {first_usable1}")
        print(f"Last usable host address 1: {last_usable1}")
        print(f"Number of usable hosts 1: {len(hosts1)}")
    else:
        print("\nNo usable host addresses in network 1.")
    
    if hosts2:
        first_usable2 = hosts2[0]
        last_usable2 = hosts2[-1]
        print(f"\nFirst usable host address 2: {first_usable2}")
        print(f"Last usable host address 2: {last_usable2}")
        print(f"Number of usable hosts 2: {len(hosts2)}")
    else:
        print("\nNo usable host addresses in network 2.")
    
    # List all hosts in both networks if they are small
    if ip1.network.num_addresses < 256:
        print("\nHosts in network 1:")
        for host in hosts1:
            print(host)
    
    if ip2.network.num_addresses < 256:
        print("\nHosts in network 2:")
        for host in hosts2:
            print(host)

# Example usage
analyse_ip('192.168.1.1/24', '192.168.2.1/24')
