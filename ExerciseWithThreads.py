"""
Modify the following example in order to transform the script into:

 1) a multi-threaded script
    (for instance you could create 5 threads each of them in charge of computing 20 factorials)
 2) a multi-process script
    (for instance you could create 5 processes each of them in charge of computing 20 factorials)
    
You could then try to determine the most efficient version with the help of the module timeit

"""
import random
import threading
import time
import queue # contain some "threadsafe" data types (here we use Queue)
random.seed(1)   
 
dataset=[]
for i in range(100):
    dataset.append(random.randint(1,15))
    
def factorial(n):
    total=1
    for i in range(1,n+1):
        time.sleep(0.002)
        total *= i
    return total    

q=queue.Queue() 

def computeFactorial(data, q):
    for i in data:
        q.put((i,factorial(i)))
            
def versionWithThreads():

    numberOfThreads=5
    
    threads = []
    for i in range(numberOfThreads):
        t=threading.Thread(target=computeFactorial, args=(dataset[i*20:(i+1)*20], q))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        

versionWithThreads()

if __name__ == '__main__':       
    import timeit
    number=5
    result=timeit.timeit("versionWithThreads()", setup="from __main__ import versionWithThreads", number=number)
    print(f"It took {result} to run the code {number} times -> average execution time: {result/number:.6f}")
        
    # print("Here is what the queue contains:")
    # print("Q size:",q.qsize())
    # while not q.empty():
    #     print(q.get(), end="-")

