
def Greedy(iterations, tabMachines):

    gain = 0
    bestScoreMachine = None

    for i in range(len(tabMachines)):
        scoreMachine = tabMachines[i].tirerBras()
        gain += scoreMachine
        if bestScoreMachine is None:
            bestScoreMachine = scoreMachine
            bestMachine = i
        elif scoreMachine > bestScoreMachine:
            bestScoreMachine = scoreMachine
            bestMachine = i



    for i in range(iterations-len(tabMachines)):
        gain += tabMachines[bestMachine].tirerBras()

    print("Greedy -> "+str(gain))
    return gain
