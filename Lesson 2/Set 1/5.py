import random as ra
import math

simulations = 10
area = []

for i in range(simulations):
    points = 0
    for j in range(10000):
        x = ra.random()
        y = ra.random()
        if y <= 1/(x+1):
            points += 1
    area.append(points/10000)

#value of integration is 2/pi
print("The area is {}".format(sum(area)/simulations))
print("the value should be {}".format(math.log(2, math.e)))