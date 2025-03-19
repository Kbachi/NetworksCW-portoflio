import socket
import datetime
import threading

# TCP Server - File Receiver
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65433))
    server_socket.listen(5)
    print("TCP Server is ready to receive files...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        
        with open('received_file.txt', 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        print("File received and saved as 'received_file.txt'!")
        
        client_socket.close()

# Run the server
server_socket_thread = threading.Thread(target=tcp_server, daemon=True)
server_socket_thread.start()

# TCP Client - File Sender
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65433))
    
    start_time = datetime.datetime.now()
    with open('file_to_send.txt', 'rb') as f:
        client_socket.sendfile(f)
    end_time = datetime.datetime.now()
    
    print("File sent successfully!")
    print(f"Time taken to send: {end_time - start_time}")
    
    client_socket.close()

# Example usage
tcp_client()
