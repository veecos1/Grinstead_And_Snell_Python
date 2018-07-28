import numpy as np
import matplotlib.pyplot as plt

winnings = 0
win_17 = 0
winning_array = []
win_17_array = []
for i in range(500):
    x = np.random.random_integers(38)
    if x > 2:
        if x % 2 == 1:
            winnings += 1
            if x == 17:
                win_17 += 35
            else:
                win_17 -= 1
            win_17_array.append(win_17)
            winning_array.append(winnings)
        else:
            winnings -= 1
            win_17 -=1
            winning_array.append(winnings)
            win_17_array.append(win_17)
    else:
        winnings -= 1
        win_17 -= 1
        winning_array.append(winnings)
        win_17_array.append(win_17)

print("winnings is {}".format(winnings))
plt.plot(winning_array)
plt.plot(win_17_array)
plt.show()