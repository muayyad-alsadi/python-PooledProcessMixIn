# -*- coding: UTF-8 -*-
"""
A pure-python module that provides asynchronous mix-in
similar to standard ThreadingMixIn and ForkingMixIn
but provides better performance by utilizing a pool
of processes forked at initialization time
each process allocate a pool of given number of threads

Copyright © 2012, Muayyad Alsadi <alsadi@gmail.org>
Released under the same terms as of Python 
http://docs.python.org/license.html
"""

import time # might be used for shutdown
import socket

from multiprocessing import Process, Event, Semaphore, Value, cpu_count
from threading import Thread
from SocketServer import BaseServer # for shutdown

__author__ = 'Muayyad Saleh Alsadi'
__version__ = '0.0.2'
__license__ = 'PSFL'

class PooledProcessMixIn:
    """
A Mix-in added by inheritance to any Socket Server like BaseHTTPServer to provide concurrency through
A Pool of forked processes each having a pool of threads
    """
    def _handle_request_noblock(self):
        if not getattr(self, '_pool_initialized', False): self._init_pool()
        self._event.clear()
        self._semaphore.release()
        self._event.wait()

    def _real_handle_request_noblock(self):
        try:
            # next line will do self.socket.accept()
            request, client_address = self.get_request()
        except socket.error:
            self._event.set()
            return
        self._event.set()
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
                self.shutdown_request(request)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)


    def _init_pool(self):
        self._pool_initialized = True
        self._process_n = getattr(self, '_process_n', max(2, cpu_count()))
        self._thread_n = getattr(self, '_thread_n', 64)
        self._keep_running = Value('i', 1)
        self._shutdown_event = Event()
        self._shutdown_event.clear()
        self._event = Event()
        self._semaphore = Semaphore(1)
        self._semaphore.acquire()
        self._maintain_pool()
    
    def _maintain_pool(self):
        self._processes = []
        for i in range(self._process_n):
            t = Process(target=self._process_loop)
            t.start()
            self._processes.append(t)

    def _process_loop(self):
        threads = []
        for i in range(self._thread_n):
            t = Thread(target=self._thread_loop)
            t.setDaemon(0)
            t.start()
            threads.append(t)
        # we don't need this because they are non-daemon threads
        # but this did not work for me
        # FIXME: replace this with event
        self._shutdown_event.wait()
        #for t in threads: t.join()

    def _thread_loop(self):
        while(self._keep_running.value):
            self._semaphore.acquire() # wait for resource
            self._real_handle_request_noblock()

    def pool_shutdown(self):
        self._keep_running.value = 0
        self._shutdown_event.set()

    def shutdown(self):
        self.pool_shutdown()
        BaseServer.shutdown(self) # super(BaseServer).shutdown()
        # TODO: is the below needed ?
        #time.sleep(1) # give them 1 second for clean shutdown
        #for p in self._processes: p.terminate()

