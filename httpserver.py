#!/usr/bin/python
import time
import configparser
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from lightingled import light_test
from simplelcd import  print_msg


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self.message_dispatcher()

    def message_dispatcher(self):
        if self.path == '/light':
            lighting_thread = threading.Thread(target=light_test)
            lighting_thread.start()
            self.success_message('{ "msg":"Success"}')
        else if self.path == '/lcd':
            print_msg('Test! TEST! Test!')
            self.success_message('{ "msg":"Success"}')
        else:
            self.error_message()

    def success_message(self, content):
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
    config = configparser.ConfigParser()
    config.read('config.ini')
    host_name = config['DEFAULT']['HOST_NAME']
    port_number = int(config['DEFAULT']['PORT_NUMBER'])
    print(host_name + ' ' + str(port_number))

    httpd = server_class((host_name, port_number), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (host_name, port_number))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (host_name, port_number))
