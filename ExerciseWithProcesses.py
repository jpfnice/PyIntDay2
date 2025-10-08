import random
import multiprocessing
import time

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

def computeFactorial(data, q):
    for i in data:
        q.put((i,factorial(i)))

def main():
    
    numberOfProcesses=5
    q=multiprocessing.Queue()
     
    procs=[]  
    for i in range(numberOfProcesses):
        t=multiprocessing.Process(target=computeFactorial, args=(dataset[i*20:(i+1)*20], q))
        t.start()
        procs.append(t)
        
    for t in procs:
        t.join()
    
#         
#     while not q.empty():
#         print(q.get())
        

if __name__ == '__main__':       
    import timeit
    number=5
    result=timeit.timeit("main()", setup="from __main__ import main", number=number)
    print(f"It took {result} to run the code {number} times -> average execution time: {result/number:.6f}")
    
  
 
 