import numpy as np
import matplotlib.pyplot as plt
import random
import math


# This function generates random numbers between 0 and 1 by using LCM.
def LCM(a, c, M, r, size):

    pesudo_rn = []
    for i in range(size):

        r = (a * r + c) % M
        # k = r / M # This part generate random numbers between [0,1]
        # pesudo_rn.append(k)
        pesudo_rn.append(r)

    return pesudo_rn

# LCM_01 generate scaled random numbers in range [0,1]
def LCM_01(a, c, M, r, size):

    pesudo_rn = []
    for i in range(size):
        r = (a * r + c) % M
        k = r / M  # This part generate random numbers between [0,1]
        pesudo_rn.append(k)

    return pesudo_rn

ran = LCM(57, 1, 256, 10, 500)
ran_01 = LCM_01(57, 1, 256, 10, 10000)



# THis function is implement Lagrange interpolation for fitting.

def Lagrange(x, y, x_val):
    data_len = len(x)
    order = data_len - 1
    g = 0

    for i in range(data_len):

        p_j = 1
        for j in range(order + 1):
            if i != j:
                p_j = p_j * (x_val - x[j]) / (x[i] - x[j])

        g = g + p_j * y[i]

    return g

# This function implement linear regression.

def LinearRegression(x,y):

    X = np.array(x)
    y = np.array(y)

    design_1 = np.c_[np.ones((np.shape(x)[0], 1)), x]
    betha = np.dot(np.dot(np.linalg.inv(np.dot(design_1.T, design_1)), design_1.T), y)

    return betha, X*betha[1]+ betha[0]

