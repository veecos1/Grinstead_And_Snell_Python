import random as ra
import matplotlib.pyplot as plt

overall_leads = []

for k in range(10000):
    peter = []
    paul = []
    leads = 0
    for i in range(40):
        roll = ra.random()
        if roll < 0.5:
            peter.append(-1)
            paul.append(1)
        else:
            peter.append(1)
            paul.append(-1)

        if len(paul) == 1:
            if paul[0] == 1:
                leads += 1
        else:
            if sum(peter) > 0:
                leads += 1
            elif sum(peter) == 0:
                if sum(peter[:-1]) > 0:
                    leads += 1

    overall_leads.append(leads)

plt.hist(overall_leads)
plt.show()