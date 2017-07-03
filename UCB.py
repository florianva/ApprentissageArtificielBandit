import math as m


def UCB(iterations, tabMachines, k):

    nbTirages = []
    SommeGains = []
    #Plus K est grand plus on explore, plus il est petit plus on exploite
    K = k
    gainTotal = 0

    for i in range(len(tabMachines)):
        scoreMachine = tabMachines[i].tirerBras()
        SommeGains.append(scoreMachine)
        nbTirages.append(1)
        gainTotal += scoreMachine

    for i in range(len(tabMachines), iterations - len(tabMachines)):
        bestUCB = None
        for j in range(len(tabMachines)):
            esperance = SommeGains[j] / nbTirages[j]
            coefficient = m.sqrt(m.log(i) / nbTirages[j])

            scoreUCB = esperance + K * coefficient

            if bestUCB is None:
                bestUCB = scoreUCB
                bestMachine = j
            elif scoreUCB > bestUCB:
                bestUCB = scoreUCB
                bestMachine = j

        gain = tabMachines[bestMachine].tirerBras()
        SommeGains[bestMachine] += gain
        gainTotal += gain
        nbTirages[bestMachine] += 1
    print(nbTirages)
    print("UCB -> " + str(gainTotal))
    return gainTotal