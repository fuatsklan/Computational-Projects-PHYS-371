import numpy as np
import matplotlib.pyplot as plt
import random
import math
from FromScratch import ran_01


"""""
A random walk in two dimensions
Write a program that simulate a random 2D walk with the same step size . Four directions are possible (N, E, S, W). 
Your program will involve two large integers, K = the number of
random walks to be taken and N = the maximum number of steps in a single walk. Run your program with at least K >= 1000.
1. Find the average distance R to be from the origin point after N steps
Assume that R has the asymptotic N dependence R~Na and estimate the exponent a.
2. Randomly place the "random walker" on a two-dimension lattice of L sites in a row
(like a city with L+1 blocks in a row). Find the average distance D (or the average number of steps) to go to be out of the city limit. 
Is there a connection between D and L? Consider the problem as an unrestricted random walk when all directions have equal probability.
3. Consider the "random walker in a city" as a persistent random walk, i.e. on each step the walker cannot step back but forward, left or right.
 What is different in this case comparing to the unrestricted random walk?

"""

# Declare number of steps in single walk and number of walks.

N = 1000
K = 1000

# Single Random Walk in 2-D

def RW(N):

    x_list = []
    y_list = []

    y = 0
    x = 0

    for i in range(N):
        x_list.append(x)
        y_list.append(y)
        #random_num = random.choice(ran_01)
        num = random.random() # random_num
        if num > 0.75:
            y = y + 1
        elif 0.5 < num < 0.75:
            y = y - 1
        elif 0.25 < num < 0.5:
            x = x + 1
        else:
            x = x - 1


    avg_dist = np.sqrt(x**2 + y**2)

    return x_list, y_list, avg_dist

Single_Walk = RW(N)

#Plots
#fig, ax = plt.subplots()
#plt.plot(Single_Walk[0], Single_Walk[1])
#plt.plot(Single_Walk[0][-1], Single_Walk[1][-1],'r*', label='Final Position')
#plt.plot(Single_Walk[0][0], Single_Walk[1][0],'k*',label='Initial Position')
#ax.set_title('Single 2-D Random Walk (N = 1000)')
#ax.set_xlabel('X-position')
#ax.set_ylabel('Y-position')
#ax.legend(shadow=True, fancybox=True)
#plt.show()

# This function calculates the avarage distance and final position of each single walk.
# Hence, we can find probability distrubition and asymptotic relation between N and <R>.
def Dependency(K, N):

    avarage_distances = []
    avarage = []
    N_list = []
    x_list = []
    y_list = []

    for j in range(N, 50*N, 100):
        for i in range(K):

            singlwalk_avarage_distance = RW(j)[2]
            avarage_distances.append(singlwalk_avarage_distance)
            if j == N*10:
                x_list.append(RW(j)[0][-1])
                y_list.append(RW(j)[1][-1])

        avarage.append(np.mean(avarage_distances))
        N_list.append(j)

    return N_list, avarage, x_list, y_list

dep = Dependency(K, N)

# Calculating asymptotic N^a dependency.
def calc_dep(x, y):
    dep_list = []
    for i, j in enumerate(x):
        dep = math.log(j, y[i])
        dep_list.append(dep)

    return np.mean(dep_list)

a = calc_dep(dep[1], dep[0])
N_a = (dep[0])**a

# PLots

fig, ax = plt.subplots()
plt.plot(dep[0], dep[1], label='$< R >$')
plt.plot(dep[0], N_a, label='$N^a, $ a = {}'.format(a))
ax.set_title('N vs Avarage Distance (N = 100-5000, K = 1000), LCM Method')
ax.set_xlabel('N')
ax.set_ylabel('Avarage Distance From Origin < R >')
ax.legend(shadow=True, fancybox=True)
plt.show()


#fig, ax = plt.subplots()
#plt.scatter(dep[2], dep[3])
#ax.set_title('P(x,y) after K walk(N = 1000, K = 1000)')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#plt.show()







