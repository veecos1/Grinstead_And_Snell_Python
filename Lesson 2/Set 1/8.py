import random as ra
import numpy as np
import math

simulations = 10000
runs = 10
final_counts = []


for j in range(runs):
    count = 0
    for i in range(simulations):

        tita = (ra.random() * math.pi * 0.5)

        count += 100 * math.cos(tita) + 100 * math.sin(tita)

    final_counts.append(count/simulations)

print(" The value of pi is ", 400 / np.mean(final_counts))
