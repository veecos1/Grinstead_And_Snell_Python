import random as ra
import numpy as np
import math
import matplotlib.pyplot as plt

simulations = 10000
waiting_time = 30
xs = []
x1 = np.arange(0, 1, 0.001)
y1 = [2 - 2*x for x in x1]

for i in range(simulations):
    x = ra.random()
    y = ra.random()
    if x + y <= 1:
        xs.append(x)

plt.hist(xs, bins=10, density=True)
plt.plot(x1, y1, color="red", lw=2)
plt.show()
#constant is 1/2
