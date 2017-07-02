import matplotlib.pyplot as plt

def printGraph(iterations, gains):

    plt.plot(iterations, gains, label='Gain en fonction du nombre des iterations')
    plt.xlabel('iterations')
    plt.ylabel('gains')
    plt.show()