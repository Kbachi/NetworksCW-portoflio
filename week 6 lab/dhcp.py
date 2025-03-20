import ipaddress

def analyse_ip(ip_str1, ip_str2):
    # Create IP interface objects
    ip1 = ipaddress.ip_interface(ip_str1)  # First IP
    ip2 = ipaddress.ip_interface(ip_str2)  # Second IP
    
    print("Address 1:", ip1.ip)
    print("Network 1:", ip1.network)
    print("Netmask 1:", ip1.netmask)
    print("Is private 1:", ip1.ip.is_private)
    print("Is global 1:", ip1.ip.is_global)
    
    print("Address 2:", ip2.ip)
    print("Network 2:", ip2.network)
    print("Netmask 2:", ip2.netmask)
    print("Is private 2:", ip2.ip.is_private)
    print("Is global 2:", ip2.ip.is_global)
    
    # Compare networks
    if ip1.network == ip2.network:
        print("Both IP addresses belong to the same network.")
    else:
        print("The IP addresses belong to different networks.")
    
    # Calculate broadcast address for both networks
    broadcast_address1 = ip1.network.broadcast_address
    broadcast_address2 = ip2.network.broadcast_address
    print("Broadcast address 1:", broadcast_address1)
    print("Broadcast address 2:", broadcast_address2)
    
    # Calculate first and last usable host addresses for both networks
    hosts1 = list(ip1.network.hosts())
    hosts2 = list(ip2.network.hosts())
    
    if len(hosts1) > 0:
        first_usable1 = hosts1[0]
        last_usable1 = hosts1[-1]
        print("First usable host address 1:", first_usable1)
        print("Last usable host address 1:", last_usable1)
        print("Number of usable hosts 1:", len(hosts1))
    else:
        print("No usable host addresses in network 1.")
    
    if len(hosts2) > 0:
        first_usable2 = hosts2[0]
        last_usable2 = hosts2[-1]
        print("First usable host address 2:", first_usable2)
        print("Last usable host address 2:", last_usable2)
        print("Number of usable hosts 2:", len(hosts2))
    else:
        print("No usable host addresses in network 2.")
    
    if len(list(ip1.network.hosts())) < 256:
        print("Hosts in network 1:")
        for host in hosts1:
            print(host)
    
    if len(list(ip2.network.hosts())) < 256:
        print("Hosts in network 2:")
        for host in hosts2:
            print(host)

analyse_ip('192.168.1.1/24', '192.168.2.1/24')
