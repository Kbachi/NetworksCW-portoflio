import socket
import threading
import base64

clients = []

def encode_message(message):
    return base64.b64encode(message.encode()).decode()

def decode_message(encoded_message):
    return base64.b64decode(encoded_message).decode()

# TCP Server - Handles encrypted chat
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            encoded_message = client_socket.recv(1024)
            if not encoded_message:
                break
            message = decode_message(encoded_message)
            print(f"Message from {client_address}: {message}")
            broadcast(encoded_message, client_socket)
        except:
            break
    print(f"Connection closed: {client_address}")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65435))
    server_socket.listen(5)
    print("Base64 chat server started...")
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

# Run server in a separate thread
server_thread = threading.Thread(target=tcp_server, daemon=True)
server_thread.start()

# TCP Client - Sends and receives encrypted messages
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65435))
    
    def receive_messages():
        while True:
            try:
                encoded_message = client_socket.recv(1024)
                if not encoded_message:
                    break
                message = decode_message(encoded_message)
                print(f"\nBase64 message received: {message}")
            except:
                break
    
    threading.Thread(target=receive_messages, daemon=True).start()
    
    while True:
        message = input("Enter message: ")
        if message.lower() == "exit":
            break
        encoded_message = encode_message(message)
        client_socket.send(encoded_message.encode())
    
    client_socket.close()

# Example usage
tcp_client()
