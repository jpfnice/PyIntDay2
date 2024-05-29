
import numpy as np

from scipy.special import factorial
np.random.seed(1)

dataset=np.random.randint(low=1,high=15,size=100)

def computation():
    return factorial(dataset)
    
import timeit
print(timeit.timeit("computation()", setup="from __main__ import computation", number=1000))

# for v,fv in zip(dataset,factorial(dataset)):
#     print(f"factorial {v} is {fv}")