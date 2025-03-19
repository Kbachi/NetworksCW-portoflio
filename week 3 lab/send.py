import socket
import base64

# Function to encode message using Base64
def encode_message(message):
    return base64.b64encode(message.encode()).decode()

# UDP Client - Send Data to Server
def send_to_server(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 65433)
    encoded_message = encode_message(message)
    client_socket.sendto(encoded_message.encode(), server_address)
    client_socket.close()

# Authentication
print("Please log in before sending a message.")
username = input("Enter username: ")
password = input("Enter password: ")

print("You are now logged in.")
message = input("Enter message to send: ")
send_to_server(message)
print("Message sent")
