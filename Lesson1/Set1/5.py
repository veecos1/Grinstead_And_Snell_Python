import random as ra
import numpy as np
simulations = 10000
sum_rolls = 0

for i in range(simulations):
    total_rolls = 0
    while True:
        roll1 = np.random.random_integers(6)
        roll2 = np.random.random_integers(6)
        roll3 = np.random.random_integers(6)
        total_rolls +=1
        if roll1 ==6 and roll2 ==6 and roll3 == 6:
            sum_rolls += total_rolls
            break
        else:
            continue

print("Number or rolls required is {}".format(sum_rolls/simulations))

#Roll of 9 is less likely than roll of 10 