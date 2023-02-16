import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
    # return (np. sin(2)*np. cos(pi))/np


x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax2 = fig.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', shade=True, lightsource=True)

plt.show()