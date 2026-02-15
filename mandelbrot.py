import numpy as np
import matplotlib.pyplot as plt

def iterate(n, x0, C):
    x = x0
    for i in range(n):
        x= x**2 + C
        if x>abs(2):
            return i
    return n

n=100

x= np.linspace(-3, 3, 1000)
y = np.linspace(-3, 3, 1000)

X, Y =np.meshgrid(x, y)
Z= X+Y*1j


escape = np.zeros(Z.shape)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        escape[i, j] = iterate(n, 0, Z[i, j])

plt.imshow(escape, extent=[-3, 3, -3, 3], origin='lower')
plt.colorbar(label='Escape iteration')
plt.xlabel('Re(C)')
plt.ylabel('Im(C)')
plt.title('Mandelbrot Set')
plt.show()
