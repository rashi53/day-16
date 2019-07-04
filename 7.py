#numpy operation
#axis
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
print("a:\n",a)
print("sum axis 0:",a.sum(axis=0))
print("sum axis 1:",a.sum(axis=1))
