import random as ra
import math

simulations = 10
area = []

for i in range(simulations):
    points = 0
    for j in range(10000):
        x = ra.random()
        y = ra.random()
        if (x-0.5)**2 + (y-0.5)**2 <= 0.25:
            points += 1
    area.append(points/10000)

print("The area is {}".format(sum(area)/simulations))
print("the value should be {}".format(math.pi/4))