import random as ra
import matplotlib.pyplot as plt
import numpy as np

simulations = 1000

half = 0
third = 0
sixth = 0

for i in range(simulations):
    spin = ra.random()
    if spin < 0.5:
        half+=1
    elif spin < (5/6):
        third +=1
    else:
        sixth += 1

x = ['half','third','sixth']
widht = [1/2, 1/3, 1/6]
heights = [2*half/simulations, 3*third/simulations, 6*sixth/simulations]
plt.bar(np.arange(len(x)),heights, align='center', alpha=0.5, width=widht)
plt.xticks(np.arange(len(x)), x)
plt.show()
