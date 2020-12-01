#!/usr/bin/env python3

'''
3 Time zones
'''

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

def get_time(timezone:str=None) -> str:
    '''
    Helper function that gets the time using `zdump`
    '''
    import subprocess

    if timezone is None:
        # fill in automatically
        # strip newline
        timezone = subprocess.check_output(['cat', '/etc/timezone']).rstrip()
    else:
        timezone = bytes(timezone, 'utf-8')

    # returns output as byte string
    output = subprocess.check_output(['zdump', timezone])
    current_time = output.split()[4]

    return current_time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''
    This rudimentary HTTP request handler
    accepts a GET request in one of the following forms:

    "GET / HTTP/1.1"
    "GET /?timezone={TIMEZONE} HTTP/1.1"

    If `timezone={TIMEZONE}` is not specified,
    or an invalid timezone is specified,
    the server returns the time in its own timezone.

    Otherwise, the server will return the time in that timezone.

    Example:
    "GET /?timezone=America%2FLos_Angeles HTTP/1.1"
    '''
    def do_GET(self):
        timezone = None
        split_path = self.path.split('=')
        if len(split_path) == 2:
            # timezone = html.unescape(split_path[1])
            timezone = urllib.parse.unquote(split_path[1])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(get_time(timezone))

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    '''
    Driver function
    I would usually use Express or Flask for this
    but decided to keep it very simple for this assignment
    '''
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving!")
    httpd.serve_forever()

run(handler_class=SimpleHTTPRequestHandler)
