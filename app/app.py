from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        app_name = os.getenv("APP_NAME", "OMNIOPS")
        env = os.getenv("ENV", "dev")

        message = f"""
        <h1>🚀 {app_name} running in Kubernetes</h1>
        <p>Environment: {env}</p>
        """
        self.wfile.write(message.encode())

PORT = 80
server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Server running on port {PORT}", flush=True)
server.serve_forever()

