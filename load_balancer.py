import socket
import threading

# Backend server pool (host, port)
backends = [("localhost", 8001), ("localhost", 8002)]
backend_index = 0
lock = threading.Lock()

def handle_client(client_socket):
    global backend_index
    
    # Round-robin selection
    with lock:
        host, port = backends[backend_index]
        backend_index = (backend_index + 1) % len(backends)
        
    # Connect to the selected backend server
    backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backend_socket.connect((host, port))
    
    # Forward request
    client_data = client_socket.recv(1024)
    backend_socket.sendall(client_data)
    
    # Get response form backend
    response = backend_socket.recv(4096)
    client_socket.sendall(response)
    
    # Close sockets
    client_socket.close()
    backend_socket.close()
    
def start_load_balancer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8080)) # Load balancer runs on port 8080
    server.listen(5)
    print("Load Balancer running on port 8080...")
    
    while True:
        client_sock, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock,))
        client_thread.start()
        
if __name__ == '__main__':
    start_load_balancer()