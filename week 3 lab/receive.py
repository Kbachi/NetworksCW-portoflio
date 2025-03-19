import socket
import base64

# Dictionary to store username-password pairs and track IP addresses
user_credentials = {"user1": "password1", "user2": "password2"}
user_ips = {}

# Function to decode Base64 message
def decode_message(encoded_message):
    return base64.b64decode(encoded_message).decode()

# UDP Server - Receive Data with Authentication and IP Tracking
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 65433))
    print("UDP Server is ready to receive data...")
    
    while True:
        data, client_address = server_socket.recvfrom(2048)
        decoded_data = decode_message(data)
        
        # Check if it is an authentication attempt
        if decoded_data.startswith("AUTH:"):
            _, username, password = decoded_data.split(":")
            if username in user_credentials and user_credentials[username] == password:
                user_ips[client_address[0]] = username  # Store IP and associated username
                server_socket.sendto("AUTH_SUCCESS".encode(), client_address)
                print(f"User {username} authenticated from {client_address[0]}")
            else:
                server_socket.sendto("AUTH_FAILED".encode(), client_address)
                print(f"Failed authentication attempt from {client_address[0]}")
        else:
            # Ensure sender is authenticated before processing messages
            if client_address[0] in user_ips:
                print(f"Received from {user_ips[client_address[0]]} ({client_address[0]}): {decoded_data}")
            else:
                print(f"Unauthorised message received from {client_address[0]}")
                server_socket.sendto("AUTH_REQUIRED".encode(), client_address)

udp_server()
