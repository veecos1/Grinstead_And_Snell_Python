import random as ra
import matplotlib.pyplot as plt
import numpy as np

simulations = 1000

third = 0
fourth = 0
fifth = 0
sixth = 0
twentieth = 0

for i in range(simulations):
    spin = ra.random()
    if spin < 1/3:
        third += 1
    elif spin < (1/3 + 1/4):
        fourth +=1
    elif spin < (1/3 + 1/4 + 1/5):
        fifth +=1
    elif spin < (1/3 + 1/4 + 1/5 + 1/6):
        sixth +=1
    else:
        twentieth += 1

x = ['third','fourth','fifth','sixth','twentieth']
widht = [1/3, 1/4,1/5, 1/6,1/20]
heights = [3*third/simulations, 4*fourth/simulations,5*fifth/simulations,6*sixth/simulations,
           20*twentieth/simulations]
plt.bar(np.arange(len(x)),heights, align='center', alpha=0.5, width=widht)
plt.xticks(np.arange(len(x)), x)
plt.show()
