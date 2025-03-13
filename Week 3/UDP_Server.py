import socket

# Create UDP socket and bind it to an address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
server_socket.bind(server_address)

print(f"UDP Chat Server is running on {server_address[0]}:{server_address[1]}")

# Set to keep track of connected client addresses
clients = set()

while True:
    # Receive data from a client
    data, client_address = server_socket.recvfrom(2048)
    message = data.decode()
    print(f"Received from {client_address}: {message}")
    
    # Add the client to the set if new
    if client_address not in clients:
        clients.add(client_address)
        print(f"New client joined: {client_address}")
    
    # Broadcast the message to all clients except the sender
    for addr in clients:
        if addr != client_address:
            server_socket.sendto(data, addr)
