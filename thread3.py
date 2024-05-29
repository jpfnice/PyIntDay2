''' 
Logging facility
join() and isAlive()
''' 
import logging

import threading
import time

logging.basicConfig(level=logging.WARNING,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    logging.debug('Starting') # info() warning() error() ...
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t = threading.Thread(name='my_service', target=my_service)
#t.daemon=True
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
w.join()

t.start()

#w.join(0.5) # Wait for 0.5 s for the termination of thread w
print('w.isAlive()', w.is_alive())

#t.join() # wait for thread t to finish its execution
