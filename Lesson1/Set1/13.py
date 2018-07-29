import random as ra
simmulations = 100

count_big = 0
count_small = 0

for j in range(simmulations):

    for i in range(365):
        boy_big = 0
        boy_small = 0
        for child_big in range(45):
            if ra.random() < 0.5:
                boy_big += 1

        for child_small in range(15):
            if ra.random() < 0.5:
                boy_small += 1

        if float(boy_big) > (45*0.6):
            count_big += 1

        if boy_small > 9:
            count_small += 1

print("big hospital count : {}".format(count_big/simmulations))
print("small hospital count : {}".format(count_small/simmulations))
