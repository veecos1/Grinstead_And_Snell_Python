import random as ra
sample_size = 3000

simulations = 100
democrat_wins = 0
republican_wins = 0

for j in range(simulations):
    vote_republican = 0
    vote_democrat = 0
    for i in range(sample_size):
        toss = ra.random()
        if toss <= 0.48:
            vote_republican +=1
        else:
            vote_democrat += 1
    if vote_democrat > vote_republican:
        democrat_wins+=1
    if vote_republican > vote_democrat:
        republican_wins+=1

print("Democrat win % : {} Republican win % : {} tie % : {}".format(
    democrat_wins/simulations, republican_wins/simulations, (simulations-democrat_wins-republican_wins)/simulations))