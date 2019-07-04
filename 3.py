#Numpy v/s List
#less memory,fast,convenient
import numpy as np
import time
import sys
SIZE=10000000
L1=list(range(SIZE))
L2=list(range(SIZE))
start=time.time()
result=[(x+y)for x,y in zip(L1,L2)]

print("time taken by the list operation:",(time.time()-start)*100000)
#numpy array
A1=np.arange(SIZE)
A2=np.arange(SIZE)
start=time.time()
result=A1+A2
print("time taken by numpy array operation:", (time.time()-start)*100000)
