import socket
import base64

# Dictionary to store username-password pairs and track IP addresses
credentials = {"user1": "password1", "user2": "password2"}
ips = {}

# Function to decode Base64 message
def decode_message(encoded_message):
    try:
        return base64.b64decode(encoded_message).decode()
    except Exception as e:
        print(f"Decoding error: {e}")
        return ""

# UDP Server - Receive Data with Authentication and IP Tracking
def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 65433))
    print("UDP Server is ready to receive data...")
    
    while True:
        d, addr = s.recvfrom(2048)
        decoded = decode_message(d)
        
        # Check if it is an authentication attempt
        if "AUTH:" in decoded:
            parts = decoded.split(":")
            if len(parts) == 3:
                username, password = parts[1], parts[2]
                if username in credentials and credentials[username] == password:
                    ips[addr[0]] = username  # Store IP and associated username
                    s.sendto("AUTH_SUCCESS".encode(), addr)
                    print(f"User {username} authenticated from {addr[0]}")
                else:
                    s.sendto("AUTH_FAILED".encode(), addr)
                    print(f"Failed authentication attempt from {addr[0]}")
            else:
                s.sendto("AUTH_FAILED".encode(), addr)
                print(f"Malformed authentication attempt from {addr[0]}")
        else:
            # Ensure sender is authenticated before processing messages
            if addr[0] in ips:
                print(f"Received from {ips[addr[0]]} ({addr[0]}): {decoded}")
            else:
                print(f"Unauthorised message received from {addr[0]}")
                s.sendto("AUTH_REQUIRED".encode(), addr)

udp_server()
