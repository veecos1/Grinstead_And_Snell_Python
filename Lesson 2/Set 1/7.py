import random as ra
import numpy as np
import math

simulations = 10000
runs = 10
final_counts = []


for j in range(runs):
    count = 0
    for i in range(simulations):

        d1 = (ra.random()*0.5)
        d2 = (ra.random()*0.5)
        tita = (ra.random() * math.pi *0.5)

        if d1 <= 0.5 * math.sin(tita) or d2<= 0.5* math.cos(tita):
            count += 1

    final_counts.append(count/10000)

print(" The value of pi is ", 3 / np.mean(final_counts))
