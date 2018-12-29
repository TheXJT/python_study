from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.gca(projection='3d')
x,y=np.mgrid[-5:5:0.1,-5:5:0.1]
z=(x**2+y**2)/2
ax.plot_surface(x,y,z)
plt.show()