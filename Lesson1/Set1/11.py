import random as ra
import matplotlib.pyplot as plt
import numpy as np

overall_max = []
overall_prop = []

for k in range(10000):
    peter = []
    paul = []
    max_peter = 0
    prop_count = 0
    for i in range(40):
        roll = ra.random()
        if roll < 0.5:
            peter.append(-1)
            paul.append(1)
        else:
            peter.append(1)
            paul.append(-1)

        if sum(peter) > max_peter:
            max_peter = sum(peter)
        if max_peter % 2 == 0:
            prop_count += 1

    overall_max.append(max_peter)
    overall_prop.append(prop_count)

#plt.plot(overall_max)
#plt.plot(overall_prop)
#plt.show()
print("average of max is ", np.mean(overall_max))
print("averagge of prop is", np.mean(overall_prop))