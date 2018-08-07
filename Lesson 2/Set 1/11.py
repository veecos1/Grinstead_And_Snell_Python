import random as ra
import numpy as np
import math

simulations = 10000
runs = 10
final_counts = []

#Lenght of the line segment is 2 *sqrt( radius^2 - distance^2 )

for j in range(runs):
    count = 0
    actual_count = 0
    for i in range(simulations):

        x_0 = (ra.random()*100) - 50
        y_0 = (ra.random()*100) - 50
        tita = (ra.random() * math.pi) - (math.pi/2)
        m = math.tan(tita)
        distance = abs((y_0 - m * x_0) / (math.sqrt(m**2 + 1)))

        if distance < 1:
            actual_count += 1
            length = 2 * math.sqrt(1 - distance**2)
            if length > math.sqrt(3):
                count += 1
    final_counts.append(count/actual_count)

print(" The probability is ", np.mean(final_counts))
