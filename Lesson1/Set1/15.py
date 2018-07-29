import random as ra
simulations = 1000

prop = 0
for i in range(simulations):
    hits = []
    for j in range(20):
        if ra.random() < 0.5:
            hits.append(1)
        else:
            hits.append(0)

    cur_count = 0
    max_count = 0
    for k in hits:
        if k == 1:
            cur_count += 1
            if cur_count > 5:
                prop += 1
                break
        else:
            cur_count = 0

print("The proportion is {}".format(prop/simulations))