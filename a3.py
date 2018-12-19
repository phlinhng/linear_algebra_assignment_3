# Linear Algebra 2018 Assignment 3

import numpy as np
import matplotlib.pyplot as plt
import math as m

# 8 points of a cube
points = np.array([[ 0, 0, 0, 0, 1, 1, 1, 1],
                   [ 0, 0, 2, 1, 0, 0, 1, 1],
                   [ 0, 1, 0, 1, 0, 1, 0, 1]])


def plotcube(pt):
    """plot a cube described by pt. 
       T is the transition matrix that maps objects from a 3D space to a 2D screen.
       The viewport is at [1/2, 1/2, sqrt(2)/2]"""
    T = np.array([[m.sqrt(2)/m.sqrt(3), 0, -1/m.sqrt(3)],
                  [-1/m.sqrt(12),  m.sqrt(3)/2, -1/m.sqrt(6)]])
    
    def drawAxis():
        """ draw the axes of the 3D space"""
        X = np.dot(T, [[0,1.5],[0,0],[0,0]])
        Y = np.dot(T, [[0,0],[0,1.5],[0,0]])
        Z = np.dot(T, [[0,0],[0,0],[0,1.5]])
        plt.plot(X[0,:], X[1,:], 'b:')
        plt.plot(Y[0,:], Y[1,:], 'b:')
        plt.plot(Z[0,:], Z[1,:], 'b:')
        plt.text(X[0,1], X[1,1], r'x', fontsize=20)
        plt.text(Y[0,1], Y[1,1], r'y', fontsize=20)
        plt.text(Z[0,1]-0.1, Z[1,1], r'z', fontsize=20)

    def visible(p1, p2, p3):
        """output if the face is visible."""
        # write your code here...
        return True
        
    def mapRectangle(p1, p2, p3, p4):
        """return two 1D arrays: X list and Y list from
           points[:, p1], points[:,p2], points[:, p3], points[:, p4]"""
        A = np.dot(T, points[:, [p1,p2,p3,p4,p1]])
        return A[0,:], A[1,:]
        
        
    # plot face 1
    X1, Y1 = mapRectangle(0, 1, 3, 2)
    print(X1, Y1)
    if(visible(0, 1, 3)):
        plt.plot(X1,Y1)

    # plot face 2
    X2, Y2 = mapRectangle(4, 6, 7, 5)
    if(visible(4, 6, 7)):
        plt.plot(X2,Y2)

    # plot face 3
    X3, Y3 = mapRectangle(0, 2, 6, 4)
    if (visible(0, 2, 6)):
        plt.plot(X3,Y3)

    # plot face 4
    X4, Y4 = mapRectangle(1, 5, 7, 3)
    if(visible(1, 5, 7)):
        plt.plot(X4,Y4)

    # plot face 5
    X5, Y5 = mapRectangle(0, 4, 5, 1)
    if(visible(0, 4, 5)):
        plt.plot(X5,Y5)

    # plot face 6
    X6, Y6 = mapRectangle(2, 3, 7, 6)
    if(visible(2, 3, 7)):
        plt.plot(X6,Y6)

    plt.axis('equal')
    drawAxis()
    plt.show()

# ----------- the main body ----------------------
r1 = np.array([[m.sqrt(3)/2, 1/2, 0],
                   [-1/2, m.sqrt(3)/2, 0],
                   [0, 0, 1]])

#points = np.dot(r1, points)

r2 = np.array([[1, 0, 0],
               [0, 3, 0],
               [0, 0, 1]])

#points = np.dot(r2, points)

plotcube(points)
