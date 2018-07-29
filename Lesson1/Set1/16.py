import random as ra

simulations = 100000
children = 0

# one boy
for i in range(simulations):
    while True:
        #Get a boy here
        if ra.random() < 0.5:
            children += 1
            break
        else:
            children +=1

print("Number of children per family is : {}".format(children/simulations))

children_2 = 0
#one boy and one girl
for j in range(simulations):
    boy = 0
    girl = 0
    while True:
        if boy >= 1 and girl >=1:
            break
        #get a boy here
        if ra.random()< 0.5:
            children_2 += 1
            boy += 1
        else:
            children_2 += 1
            girl += 1

print("Number of children per family is : {}".format(children_2/simulations))

#you will find one more child on average