# Python Load Balancer Practice

This is a basic load balancing setup in Python using socket programming and `http.server`.  
Two backend servers serve basic GET responses, and the load balancer forwards client requests to them in a round-robin manner.

## How to Run

1. Run `backend_server1.py`:
2. Run `backend_server2.py`:

3. Start the Load Balancer:

4. Send requests to the Load Balancer (e.g., open http://localhost:8080 in your browser or use `curl`).

## Ports

- Backend Server 1: `8001`
- Backend Server 2: `8002`
- Load Balancer: `8080`