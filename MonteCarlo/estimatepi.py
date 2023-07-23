import numpy as np


def estimatepi(n):
    '''Using n random points distributed across a square of side 1,
      and a circle of radius 1, estimate pi using the monte carlo method'''
    
    x  = np.random.rand(n) #Generate x-coordinates
    y = np.random.rand(n) #Generate y-coordinates

    dist = np.sqrt(x**2 + y**2) #Find point distance from origin
    c = len(np.where(dist<= 1)[0]) #Count points within circle

    pi = 4 * c/n
    return pi


if __name__ == '__main__':
    print(estimatepi(1000000))