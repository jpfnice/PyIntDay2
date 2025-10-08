"""
Modify the following example in order to transform the script into:

 1) a multi-threaded script
    (for instance you could create 5 threads each of them in charge of computing 20 factorials)
    Note: use a queue.Queue to store the factorials
 2) a multi-process script
    (for instance you could create 5 processes each of them in charge of computing 20 factorials)
    Note: use a multiprocessing.Queue to store the factorials
    
You could then try to determine the most efficient version with the help of the module timeit
"""

import time
import random
random.seed(1) # To ensure we generate the same pseudo-random numbers at each run

# The list "dataset" contains 100 random int (in the range 1 to 15).
# We want to compute the factorial of this numbers.

dataset=[]
for i in range(100):
    dataset.append(random.randint(1,15))
    
def factorial(n): 
    total=1
    for i in range(1,n+1):
        time.sleep(0.002)
        total *= i
    return total   
 
def computation():
    # This function computes the factorial of the numbers present into the list
    # dataset and stores the computed values into a new list:
    return [(e,factorial(e)) for e in dataset] # list comprehension

result=computation()
print(result)

import timeit

# timeit can be used to measure the time it takes to execute the function
# computation()

number=5
result=timeit.timeit("computation()", setup="from __main__ import computation", number=number)

print(f"It took {result} to run the code {number} times -> average execution time: {result/number:.6f}")

# #print("The result:", computation())