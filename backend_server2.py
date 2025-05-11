from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response from Backend Server 2")
        
server = HTTPServer(('localhost', 8002), SimpleHandler)
print("Backend Server 2 running on port 8002...")
server.serve_forever()