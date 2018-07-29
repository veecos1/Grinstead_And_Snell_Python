import numpy as np
import matplotlib.pyplot as plt

winning_array = []
win = 0
simulations =1000

for i in range(simulations):
    bet = 1
    win = 0
    while True:
        if win >=5 or win<=-100:
            break
        x = np.random.random_integers(38)
        if x > 2:
            if x % 2 == 1:
                win += bet

                bet = 1
            else:
                win -= bet
                winning_array.append(win)
                bet *= 2
        else:
            win -= bet
            winning_array.append(win)
            bet *= 2
    winning_array.append(win)

print("winnings is {}".format(np.mean(winning_array)))
#Good advice to avoid