#Numpy v/s List
#less memory,fast,convenient
import numpy as np
import sys
S=list(range(1000))
#memory occupied by one element*size of list
print("memory occupied by list:",sys.getsizeof(999)*len(S))
D=np.arange(1000)
print("memory occupied by numpy array:",D.itemsize*D.size)
