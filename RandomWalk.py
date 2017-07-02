from random import randint

def rechercheAleatoire(nbIterations, tabMachines):

    gain = 0

    for i in range(nbIterations):

        gain += tabMachines[randint(0,len(tabMachines)-1)].tirerBras()
    print("RandomWalk -> " + str(gain))
    return gain

