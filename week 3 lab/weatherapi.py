import socket
import requests

# Function to fetch weather data from Open-Meteo API
def fetch_weather_data():
    api_url1 = "https://api.open-meteo.com/v1/forecast?latitude=51.4742&longitude=-0.0355&current_weather=true"  # Goldsmiths University
    api_url2 = "https://api.open-meteo.com/v1/forecast?latitude=51.5299&longitude=-0.1278&current_weather=true"  # British Library
    
    response1 = requests.get(api_url1)
    response2 = requests.get(api_url2)
    
    if response1.status_code == 200 and response2.status_code == 200:
        weather_data1 = response1.json()
        weather_data2 = response2.json()
        temp1 = weather_data1["current_weather"]["temperature"]
        wind_speed1 = weather_data1["current_weather"]["windspeed"]
        condition1 = weather_data1["current_weather"]["weathercode"]
        
        temp2 = weather_data2["current_weather"]["temperature"]
        wind_speed2 = weather_data2["current_weather"]["windspeed"]
        condition2 = weather_data2["current_weather"]["weathercode"]
        
        message = (f"Goldsmiths University - Temp: {temp1}°C, Wind Speed: {wind_speed1} km/h, Condition Code: {condition1}\n"
                   f"British Library - Temp: {temp2}°C, Wind Speed: {wind_speed2} km/h, Condition Code: {condition2}")
    else:
        message = "Failed to fetch weather data"
    
    return message

# Function to send weather data via UDP
def send_weather_data():
    message = fetch_weather_data()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 65433)
    client_socket.sendto(message.encode(), server_address)
    print("Weather data sent!")
    client_socket.close()

send_weather_data()
