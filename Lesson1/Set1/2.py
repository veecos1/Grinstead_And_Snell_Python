
import random as ra
simulations = 1000

n = 100
correct = 0

for i in range(n):
    heads = 0
    tails = 0
    for j in range(simulations):
         if ra.random() < 0.5:
             heads +=1
         else:
             tails += 1

    if  heads/simulations >=0.4 and heads/simulations <= 0.6:
        correct += 1

print("proportion is {}".format(correct/n))
