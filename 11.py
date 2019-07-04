#numpy operation

import numpy as np
import matplotlib.pyplot as plt
objects=('python','c++','java','perl','scala','lisp')
x_pos=np.arange(len(objects))
performance=[10,3,6,8,2,7]
plt.bar(x_pos,performance,align='center')
##plt.xticks(x_pos,objects)
plt.ylabel('usage')
plt.title('programming language usage')
plt.show()
