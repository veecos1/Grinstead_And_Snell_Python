#Polya is a stalker :P

import random as ra

simulations = 10000
total_steps = 0
"""
for i in range(simulations):
    count = 0
    steps = 0
    while True:
        if ra.random() < 0.5:
            count -= 1
            steps += 1
        else:
            count += 1
            steps += 1

        if count == 0:
            break

    total_steps += steps

print("Average number of steps in 1d : {}".format(total_steps/simulations))
#Indicates he will eventually return , hmm


#2d
simulations = 1
total_steps = 0

for j in range(simulations):
    count_x = 0
    count_y = 0
    steps = 0
    while True:

        if ra.random() < 0.5:
            count_x -= 1
            steps += 1
        else:
            count_x += 1
            steps += 1

        if ra.random() < 0.5:
            count_y -= 1
            steps += 1
        else:
            count_y += 1
            steps += 1

        if count_x == 0 and count_y == 0:
            break

    total_steps += steps

print("Average number of steps in 2d : {}".format(total_steps/simulations))
"""
#3d
simulations = 1
total_steps = 0

for j in range(simulations):
    count_x = 0
    count_y = 0
    count_z = 0
    steps = 0
    while True:

        if ra.random() < 0.5:
            count_x -= 1
            steps += 1
        else:
            count_x += 1
            steps += 1

        if ra.random() < 0.5:
            count_y -= 1
            steps += 1
        else:
            count_y += 1
            steps += 1

        if ra.random() < 0.5:
            count_z -= 1
            steps += 1
        else:
            count_z += 1
            steps += 1

        if count_x == 0 and count_y == 0 and count_z ==0:
            break

    total_steps += steps

print("Average number of steps in 3d : {}".format(total_steps/simulations))