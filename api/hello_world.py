from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(("AutoBuild : Hello " + self.headers.get('x-forwarded-for')).encode())
        return