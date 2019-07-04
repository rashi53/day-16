#numpy operation
#matrix operation
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#concatenate
#vertical stacking
print("np.vstack:\n",np.vstack((a,b)))
print("np.hstack:\n",np.hstack((a,b)))
print(a.ravel())
