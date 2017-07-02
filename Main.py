import Machine as m
import RandomWalk as rw
import Greedy as g
import UCB as ucb
import Print
from random import randint

nbiterations = []
gains = []

def creerManchots(nb):

    tabMachines = []


    for i in range(nb):
        esperance = randint(-10, 10)
        variance = randint(0, 10)

        machine = m.Implementation(esperance, variance)
        print("Machine "+str(i+1)+" :")
        print machine

        tabMachines.append(machine)

    return(tabMachines)



def runRandomWalk(tabMachines, iterations):

    for i in range(iterations):
        nbiterations.append(i+1)
        gains.append(rw.rechercheAleatoire(100, tabMachines))
    print(gains)
    return nbiterations, gains
    #Print.printGraph(nbiterations, gains)


def runGreedy(tabMachines, iterations):

    for i in range(iterations):
        nbiterations.append(i+1)
        gains.append(g.Greedy(10000, tabMachines))
    print(gains)
    return nbiterations, gains
    #Print.printGraph(nbiterations, gains)

def runUCB(tabMachines, iterations):

    for i in range(iterations):
        nbiterations.append(i+1)
        gains.append(ucb.UCB(10000, tabMachines))
    print(gains)
    return nbiterations, gains
    #Print.printGraph(nbiterations, gains)





if __name__ == '__main__':
    tabMachines = creerManchots(3)
    #nbiterations, gains = runRandomWalk(tabMachines,10)
    #Print.printGraph(nbiterations, gains)
    #nbiterations, gains = runGreedy(tabMachines, 10)
    #Print.printGraph(nbiterations, gains)
    nbiterations, gains = runUCB(tabMachines, 10)
    Print.printGraph(nbiterations, gains)
