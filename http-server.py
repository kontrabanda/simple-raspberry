#!/usr/bin/python
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 9000


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/foo': {'status': 200},
            '/bar': {'status': 302},
            '/baz': {'status': 404},
            '/qux': {'status': 500}
        }

        if self.path in paths:
            self.success_message()
        else:
            self.error_message()

    def success_message(self):
        content = '''
        { "name":"John", "age":30, "city":"New York"}
        '''
        response = self.create_message(200, content)
        self.wfile.write(response)

    def error_message(self):
        response = self.create_message(500, '{"error": "Error!"}')
        self.wfile.write(response)

    def create_message(self, status_code, content):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return bytes(content, 'UTF-8')

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
