import socket
import requests
import threading

# Function to fetch weather data from Open-Meteo API
def fetch_weather_data():
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=51.4742&longitude=-0.0355&current_weather=true")
        if response.status_code == 200:
            data = response.json()
            weather_data = data["current_weather"] if "current_weather" in data else {}
            temperature = weather_data["temperature"] if "temperature" in weather_data else "N/A"
            wind_speed = weather_data["windspeed"] if "windspeed" in weather_data else "N/A"
            condition = weather_data["weathercode"] if "weathercode" in weather_data else "N/A"
            return f"Goldsmiths University - Temp: {temperature}°C, Wind Speed: {wind_speed} km/h, Condition Code: {condition}"
        else:
            return "Failed to fetch weather data"
    except:
        return "Error occurred while fetching weather data"

# TCP Server - Handles incoming weather data requests
def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 65436))
    s.listen(5)
    print("Server running...")
    while True:
        c, addr = s.accept()
        print(f"Connected to {addr}")
        c.send(fetch_weather_data().encode())
        c.close()

# Run server in a separate thread
threading.Thread(target=tcp_server, daemon=True).start()

# TCP Client - Requests weather data
def tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 65436))
    print("Received Weather Info: " + s.recv(1024).decode())
    s.close()

# Example usage
tcp_client()
