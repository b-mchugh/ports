import socket
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

if bool(os.environ.get('APP_PORT')):
    PORT = os.environ.get('APP_PORT')
else:
    PORT = '8080'

class RH(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = ['Hi ' + self.address_string() + '<br>\n',
            'Date: ' + self.date_time_string() + '<br>\n']
        print("! \033[31m Red \033[33m Yellow \033[32m Green \033[0m!")
        for i in message:
            self.wfile.write(bytes(i, "utf8"))
        return

def run():
    server_address = (IP, int(PORT))
    httpd = HTTPServer(server_address, RH)
    httpd.serve_forever()
run()
