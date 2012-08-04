PooledProcessMixIn For Python
=============================
![Python Logo](http://www.python.org/images/python-logo.gif)

Fast Concurrent Pool of preforked-processes and threads Mix-in for python's socket server
Replace the usual ThreadingMixIn and ForkingMixIn

This is a pure-python module that provides asynchronous mix-in
similar to standard ThreadingMixIn and ForkingMixIn
but provides better performance by utilizing a pool
of processes forked at initialization time
each process allocate a pool of given number of threads


Installation and Dependencies
-----------------------------

This module has no external dependencies other than the standard python library.

To get the latest development snapshot type the following command

git clone https://github.com/muayyad-alsadi/python-PooledProcessMixIn.git

Example
-------


    from PooledProcessMixIn import PooledProcessMixIn
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    
    # ... define MyTestHandler somewhere
    
    class MyHTTPTest (PooledProcessMixIn, HTTPServer):
        def __init__(self):
            self._process_n=7  # if not set will default to number of CPU cores
            self._thread_n=64  # if not set will default to number of threads
            HTTPServer.__init__(self, ('127.0.0.1',8888), MyTestHandler)
            self._init_pool() # this is optional, will be called automatically
            print "listing on http://127.0.0.1:8888/"


Details
-------

You can set initial number of processes by setting `self._process_n` before calling `self._init_pool()`

You can set initial number of threads for each forked process by setting self._thread_n before calling `self._init_pool()`

You should call `self._init_pool()` AFTER super class `__init__` but
if you did not call it, it will be called automatically when we get first request

When Benchmarked against ThreadingMixIn and ForkingMixIn, it gives double performance (was able to handle about 1,500 request per second while other mix-ins reached 800 requests/second )

    siege -b -c 100 -t10s localhost:8888/test
          Date & Time,  Trans,  Elap Time,  Data Trans,  Resp Time,  Trans Rate,  Throughput,  Concurrent,    OKAY,   Failed
    2012-08-02 12:51:47,  14663,       9.58,           0,       0.01,     1530.58,        0.00,       22.87,   14663,       0
    2012-08-02 12:52:44,   7653,       9.58,           0,       0.04,      798.85,        0.00,       29.42,    7653,       5
    2012-08-02 12:53:14,   7726,       9.47,           0,       0.05,      815.84,        0.00,       43.57,    7726,       0


Can I use it to run my Django applications ?
--------------------------------------------

Yes, Django provides WSGI application which can be used like the wsgi-demo included in this packages

    import sys, os
        
    from PooledProcessMixIn import PooledProcessMixIn
    from wsgiref.simple_server import make_server, WSGIServer
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
        
    d=os.path.dirname(__file__)
    sys.path.insert(0, d)
    sys.path.insert(0, os.path.join(d, ".."))
        
    from django import VERSION as DJ_VERSION
    if DJ_VERSION>=(1,4):
        from django.core.wsgi import get_wsgi_application
    else:
        from django.core.handlers.wsgi import WSGIHandler as get_wsgi_application
        
    class WSGIServerPool(PooledProcessMixIn, WSGIServer):
        pass
        
    application = get_wsgi_application()
    make_server('127.0.0.1', 8080, application, server_class=WSGIServerPool).serve_forever()

