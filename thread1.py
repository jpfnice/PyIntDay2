''' The Thread class constructor '''
import threading
import time

def worker(nb):
    """thread worker function"""
    print('Worker', nb)
    time.sleep(nb)
    print("End of worker", nb)
    return

print("In the main script")

t1 = threading.Thread(args=[10], target=worker)
#t1.daemon=True
t1.start()

t2 = threading.Thread(args=(10,),target=worker)
t2.start()

t3 = threading.Thread(args=(10,),target=worker)
t3.start()

print("End of the main script") 



