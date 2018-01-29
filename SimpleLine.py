import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2


plt.figure(num=3,figsize=(8,5))
plt.plot(x,y1)
plt.plot(x,y2,color='r',linestyle='--',linewidth=0.1)
plt.xlim(-1,3)
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.show()