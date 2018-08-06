import random as ra
import numpy as np
import math
import matplotlib.pyplot as plt

simulations = 10000
waiting_time = 30
waiting_times = []
x = np.arange(0, 300, 0.01)
y = np.exp(-x/30)/30

for i in range(simulations):
    tim = -waiting_time * math.log(ra.random(), math.e)
    waiting_times.append(tim)

plt.hist(waiting_times, bins=24, density=True)
plt.plot(x, y, color="red", lw=2)
plt.show()
