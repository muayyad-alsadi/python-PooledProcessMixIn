#! /usr/bin/python

from PooledProcessMixIn import PooledProcessMixIn
from wsgiref.simple_server import make_server, WSGIServer

class WSGIServerPool(PooledProcessMixIn, WSGIServer):
    pass

if __name__ == '__main__':
    
    # the two lines below needed for the demo app
    import os
    from threading import currentThread
    
    def application(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        yield 'PPID=[%d] PID=[%d] thread=[%s] uri=[%s] from [%s]' % (os.getppid(), os.getpid(), currentThread().name, environ['PATH_INFO'], environ['REMOTE_ADDR'],)

    host='127.0.0.1'
    port=8080
    server=make_server(host, port, application, server_class=WSGIServerPool)
    try:
        server.serve_forever()
    finally:
        server.shutdown()
