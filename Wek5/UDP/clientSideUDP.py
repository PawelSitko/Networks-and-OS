import socket
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('localhost', 65433))

message = input('send a message to the server: ')
startTime = datetime.now()
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
endTime = datetime.now()
print(f"Server response: {response.decode()}")

timeTaken = str(endTime-startTime)

print(f"Server response: {response.decode()}")
print(f"Elapsed time: {timeTaken}")

#file_path = "Users/pawelsitko/Desktop/WEK5/speedLog.txt"

with open("speedLog.txt", "a") as timeLog:
    timeLog.write(f"Elapsed time(UDP): {timeTaken}\n")

client_socket.close()