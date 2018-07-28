import numpy as np

winnings = 0
for i in range(500):
    x = np.random.random_integers(38)
    if x > 2:
        if x % 2 == 1:
            winnings += 1
        else:
            winnings -= 1
    else:
        winnings -= 1

print("winnings is {}".format(winnings))
