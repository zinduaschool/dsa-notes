import numpy as np
import matplotlib.pyplot as plt

def randomcoordinates(n):
    '''Generate n random x-y coordinates;
    Use this for pi estimation and visualisation'''
    x  = np.random.rand(n)
    y = np.random.rand(n)
    return x, y

def estimatepi(x,y):
    '''Using n random points distributed across a square of side 1,
      and a circle of radius 1, estimate pi using the monte carlo method'''
    dist = np.sqrt(x**2 + y**2) #Find point distance from origin
    c = len(np.where(dist<= 1)[0]) #Count points within circle
    pi = 4 * c/len(x)
    return pi
    
def circlecoordinates(n=100, start=0,stop=1):
    '''Find coordinates for cirlce edge,
    This is code is purely for visualisation'''
    x = np.linspace(start,stop,n)
    y = np.sqrt(1-x**2)
    return x,y


if __name__ == '__main__':
    x,y = randomcoordinates(1000)
    print(estimatepi(x,y))
    
    ## Uncomment the code below to visualise the points and those within the circle
    # circle_x, circle_y = circlecoordinates() 
    # plt.scatter(x,y) #Visualise randomly generated points
    # plt.plot(circle_x, circle_y, 'r') #Plot the circle coordinates
    # plt.show()