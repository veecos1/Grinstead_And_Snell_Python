import random as ra
import numpy as np
simulations = 10000
winnings = []
counts = []

for i in range(simulations):
    count = 1
    while True:
        if ra.random() < 0.5:
            count+=1
        else:
            winnings.append(2**(count))
            counts.append(count)
            break

print("mean winnings is {} count is {}".format(np.mean(winnings), max(counts)))