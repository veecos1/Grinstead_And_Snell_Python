import numpy as np
import matplotlib.pyplot as plt
lab_array = [1,2,3,4]
winning_array = []
win = 0

while True:
    if len(lab_array) == 0:
        break
    bet = lab_array[-1] + lab_array[0]
    x = np.random.random_integers(38)
    if x > 2:
        if x % 2 == 1:
            if len(lab_array) ==1:
                win += bet
                winning_array.append(win)
                break
            del lab_array[-1]
            del lab_array[0]
            win += bet
            winning_array.append(win)
        else:
            lab_array.append(bet)
            win -= bet
            winning_array.append(win)
    else:
        lab_array.append(bet)
        win -= bet
        winning_array.append(win)

print("winnings is {}".format(win))
plt.plot(winning_array)
plt.show()