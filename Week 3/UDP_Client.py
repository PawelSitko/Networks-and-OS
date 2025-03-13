import socket
import threading

def receive_messages(sock):
    """Background thread function to listen for messages from the server."""
    while True:
        try:
            data, _ = sock.recvfrom(2048)
            print("\nMessage from chat: " + data.decode())
        except Exception as e:
            print("An error occurred:", e)
            break

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 65433)
    
    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()
    
    print("Enter messages to send, write exit to stop")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        # Send the message to the server
        client_socket.sendto(message.encode(), server_address)
    
    client_socket.close()

if __name__ == "__main__":
    main()
