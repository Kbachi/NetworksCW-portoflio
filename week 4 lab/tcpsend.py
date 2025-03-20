import socket
import datetime
import threading

# TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(5)  # Allow up to 5 pending connections
    print("TCP Server is waiting")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        
        data = client_socket.recv(1024)
        if data:
            print(f"Received: {data.decode()}")
            client_socket.sendall(data)
            
            # Logging received data to a file
            with open('received_data.txt', 'a') as f:
                f.write(f"{datetime.datetime.now()} - {client_address}: {data.decode()}\n")
                print("Data logged.")
            
        client_socket.close()

# Run server in a separate thread
threading.Thread(target=tcp_server, daemon=True).start()

# TCP Client
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))
    
    start_time = datetime.datetime.now()
    message = input("Enter message: ")
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024)
    end_time = datetime.datetime.now()
    
    print(f"Server response: {response.decode()}")
    print(f"Time taken: {end_time - start_time}")
    
    client_socket.close()

# Example usage
tcp_client()
