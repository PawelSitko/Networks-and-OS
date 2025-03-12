import socket
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))

message = input('send a message to the server: ')
startTime = datetime.now()
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
endTime = datetime.now()
print(f"Server response: {response.decode()}")

timeTaken = str(endTime-startTime)

print(f"Server response: {response.decode()}")
print(f"Elapsed time: {timeTaken}")


with open("speedLog.txt", "a") as timeLog:
    timeLog.write(f"Elapsed time (TCP): {timeTaken}\n")

client_socket.close()