from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response form Backend Server 1")
        
server = HTTPServer(('localhost', 8001), SimpleHandler)
print("Backend Server 1 running on port 8001...")
server.serve_forever()