PooledProcessMixIn For Python
=============================

.. image:: http://www.python.org/images/python-logo.gif
  :alt: Python Logo
  :align: right

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

::

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

You can set initial number of processes by setting self._process_n before calling self._init_pool()

You can set initial number of threads for each forked process by setting self._thread_n before calling self._init_pool()

You should call self._init_pool() AFTER super class __init__ but
if you did not call it, it will be called automatically when we get first request

When Benchmarked against ThreadingMixIn and ForkingMixIn, it gives double performance (was able to handle about 1,500 request per second while other mix-ins reached 800 requests/second )

::
    siege -b -c 100 -t10s localhost:8888/test

::
    2012-08-02 12:51:47,  14663,       9.58,           0,       0.01,     1530.58,        0.00,       22.87,   14663,       0
    2012-08-02 12:52:44,   7653,       9.58,           0,       0.04,      798.85,        0.00,       29.42,    7653,       5
    2012-08-02 12:53:14,   7726,       9.47,           0,       0.05,      815.84,        0.00,       43.57,    7726,       0

