import socket
import subprocess
import requests

# 1. Finding Website IP Address
def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        print(f"The IP address of {website_url} is {ip_address}")
    except socket.gaierror:
        print(f"Unable to get the IP address for {website_url}")

website = input("Enter the website URL (without 'https://'): ")
get_ip_address(website)

# 2. Trace Route
def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("tracert command not found. Make sure it's available.")
    except Exception as e:
        print(f"An error occurred: {e}")

domain = input("Enter the website or IP address: ")
tracert(domain)

# 3. Simple HTTP Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('www.example.com', 80)
client_socket.connect(server_address)
request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
client_socket.send(request.encode())
response = client_socket.recv(4096)
print(response.decode())
client_socket.close()

# 4. Simple HTTP Client using requests
response = requests.get('http://www.example.com')
print(response.text)

# 5. HTTP Requests Types
# GET Request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())

# POST Request
data = {
    "title": "Sample Post",
    "body": "This is an example post body.",
    "userId": 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.json())

# PUT Request
updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post content has been updated.",
    "userId": 1
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_data)
print(response.json())

# DELETE Request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Resource successfully deleted.")