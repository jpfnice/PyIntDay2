''' The join() and enumerate() methods '''
import random
import threading
import time
import logging
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker():
    """thread worker function"""
    pause = random.randint(1,5)
    numbers.put(pause)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')
    return

numbers=queue.Queue()

for i in range(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()

while not numbers.empty():
    print(numbers.get())
    
# A treatment is now performed: all the threads except the "main thread" are terminated
# ....