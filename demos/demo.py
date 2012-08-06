#! /usr/bin/python

import time
import os

from PooledProcessMixIn import PooledProcessMixIn
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from threading import currentThread

class MyTestHandler (BaseHTTPRequestHandler):
    """
    Test Web application that outputs parent process id PPID, PID, thread, and URI and client address 
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        #time.sleep(0.5)
        self.wfile.write('PPID=[%d] PID=[%d] thread=[%s] uri=[%s] from [%s]' % (os.getppid(), os.getpid(), currentThread().name, self.path, self.client_address[0],))
        if self.path=='/shutdown':
            print "testing software shutting down."
            self.server.shutdown()
        

class MyHTTPTest (PooledProcessMixIn, HTTPServer):
    def __init__(self):
        HTTPServer.__init__(self, ('127.0.0.1',8888), MyTestHandler)
        self._init_pool() # this call is optional
        print "listening on http://127.0.0.1:8888/"

test=MyHTTPTest()
try: test.serve_forever()
finally: test.shutdown()
print "Done."

