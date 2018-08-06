import random as ra
import numpy as np
import math

simulations = 10000
runs = 10
final_counts = []


for j in range(runs):
    count = 0
    for i in range(simulations):

        d = (ra.random()*0.5)
        tita = (ra.random() * math.pi *0.5)

        if d < 0.5 * math.sin(tita):
            count += 1

    final_counts.append(count/10000)

print(" The value of pi is ", 2 / np.mean(final_counts))
