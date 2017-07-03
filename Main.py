import sys

import Machine as m
import RandomWalk as rw
import Greedy as g
import UCB as ucb
import Print
from random import randint

nbiterations1 = []
gains1 = []

nbiterations2 = []
gains2 = []

nbiterations3 = []
gains3 = []


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



def runRandomWalk(nbmanchots, run, iterations):

    for i in range(run):
        tabMachines = creerManchots(nbmanchots)
        nbiterations1.append(i+1)
        gains1.append(rw.rechercheAleatoire(iterations, tabMachines))
    print(gains1)
    return nbiterations1, gains1
    #Print.printGraph(nbiterations, gains)


def runGreedy(nbmanchots, run, iterations):

    for i in range(run):
        tabMachines = creerManchots(nbmanchots)
        nbiterations2.append(i+1)
        gains2.append(g.Greedy(iterations, tabMachines))
    print(gains2)
    return nbiterations2, gains2
    #Print.printGraph(nbiterations, gains)

def runUCB(nbmanchots, run, iterations, k):

    for i in range(run):
        tabMachines = creerManchots(nbmanchots)
        nbiterations3.append(i+1)
        gains3.append(ucb.UCB(iterations, tabMachines, k))
    print(gains3)
    return nbiterations3, gains3
    #Print.printGraph(nbiterations, gains)





if __name__ == '__main__':

    manchots = int(sys.argv[1])
    run = int(sys.argv[2])
    iterations = int(sys.argv[3])
    k = int(sys.argv[4])

    nbiterations1, gains1 = runRandomWalk(nbmanchots = manchots, run=run, iterations=iterations)
    #Print.printGraph(nbiterations, gains)
    nbiterations2, gains2 = runGreedy(nbmanchots = manchots, run=run, iterations=iterations)
    #Print.printGraph(nbiterations, gains)
    nbiterations3, gains3 = runUCB(nbmanchots = manchots, run=run, iterations=iterations, k=k)
    Print.printGraph(nbiterations1, gains1, nbiterations2, gains2, nbiterations3, gains3)
