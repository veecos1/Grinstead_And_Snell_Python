import random as ra
import numpy as np
simulations = 1000000
roll_9 = 0
roll_10 = 0

for i in range(simulations):
    roll1 = np.random.random_integers(6)
    roll2 = np.random.random_integers(6)
    roll3 = np.random.random_integers(6)
    if roll1 + roll2 + roll3 == 9:
        roll_9 += 1
    elif roll1 + roll2 + roll3 == 10:
        roll_10 += 1
    else:
        continue

print("roll 9 is {}".format(roll_9/simulations))
print("roll 10 is {}".format(roll_10/simulations))
#Roll of 9 is less likely than roll of 10 