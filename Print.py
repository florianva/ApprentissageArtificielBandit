import matplotlib.pyplot as plt

def printGraph(iterations1, gains1, iterations2, gains2, iterations3, gains3):

    plt.plot(iterations1, gains1)
    plt.plot(iterations2, gains2)
    plt.plot(iterations3, gains3)
    plt.xlabel('iterations')
    plt.ylabel('gains')

    plt.legend(['Random Walk', 'Greedy', 'UCB'], loc='lower right')




    plt.show()