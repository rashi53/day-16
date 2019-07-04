#numpy operation
#sin,cos,tan
import numpy as np
import matplotlib.pyplot as plt
##x=np.arange(-1,3*np.pi,0.1)
x=([1,2,3,4,5,6,7,8,9,10])
print("X:\n",x)
y=np.array([4,7,1,3,2,8,9,6,5,10])
##y=np.sin(x)
print("Y:\n",y)
plt.plot(x,y)
plt.show()
