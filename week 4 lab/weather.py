import socket
import requests

# Function to fetch weather data from Open-Meteo API
def fetch_weather_data():
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=51.4742&longitude=-0.0355&current_weather=true"  # Goldsmiths University
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        weather_data = response.json().get("current_weather", {})
        temperature = weather_data.get("temperature", "N/A")
        wind_speed = weather_data.get("windspeed", "N/A")
        condition = weather_data.get("weathercode", "N/A")
        
        message = f"Goldsmiths University - Temp: {temperature}°C, Wind Speed: {wind_speed} km/h, Condition Code: {condition}"
    else:
        message = "Failed to fetch weather data"
    
    return message

# TCP Server - Handles incoming weather data requests
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65436))
    server_socket.listen(5)
    print("Weather API TCP Server is running...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        weather_info = fetch_weather_data()
        client_socket.sendall(weather_info.encode())
        client_socket.close()

# Run server in a separate thread
import threading
server_thread = threading.Thread(target=tcp_server, daemon=True)
server_thread.start()

# TCP Client - Requests weather data
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65436))
    
    weather_info = client_socket.recv(1024).decode()
    print(f"Received Weather Info: {weather_info}")
    
    client_socket.close()

# Example usage
tcp_client()
