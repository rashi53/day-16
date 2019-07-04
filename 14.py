import numpy as np
import matplotlib.pyplot as plt
#create data
N=500
x=np.random.rand(N)
y=np.random.rand(N)
colors=(0,1,0)
area=np.pi*3
#plot
plt.scatter(x,y,s=area,c=colors,alpha=0.9)
plt.title("scatter chart plot pythonspot.com")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
