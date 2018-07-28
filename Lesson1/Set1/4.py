import random as ra
simulations = 10000
wins = 0

for i in range(simulations):
    point_mine = 0
    point_other = 0

    while point_mine <21 and point_other<21:
        server = "me"
        if server == "me":
            my_serve = ra.random()
            if my_serve <0.6:
                point_mine += 1
                server = "me"
            else:
                server = "her"
        if server == "her":
            her_serve = ra.random()
            if her_serve <0.5:
                point_other += 1
                server = "her"
            else:
                server = "me"

    if point_mine ==21:
        wins +=1

print("total win percent : {}".format(wins/float(simulations)*100.0))
