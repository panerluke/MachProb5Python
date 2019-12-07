import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 199, 200)
y = np.linspace(0, 199, 200)
x = eval(input('Please input function x(n): '))

for z in range(200):
    if y[z] == 0:
        y[z] = -1.5*x[z] + 2*x[z + 1] - 0.5*x[z + 2]
    elif y[z] > 0 and y[z] <= 198:
        y[z] = 0.5*x[z + 1] - 0.5*x[z - 1]
    elif y[z] == 199:
        y[z] = 1.5*x[z] - 2*x[z - 1] + 0.5*x[z - 2]

plt.plot(n, x)
plt.plot(n, y)
plt.legend(['x(n)', 'y(n)'])
plt.xlabel('n')
plt.ylabel('x, y')