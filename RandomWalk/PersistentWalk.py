import numpy as np
import matplotlib.pyplot as plt
import random
import math
from FromScratch import LinearRegression, ran_01

"""""
This code is implamentation of Persistent Random Walk. 
On each step the walker cannot step back but forward, left or right. 
Again we will randomly place the walker in city. Than we will find avarage number of steps to be taken
by walker to be out of city.
"""""

# This function implements presistent restricted random walk. We initialize the position randomly,
# then find the number of steps to be taken to reach to the boundry of the city. As this is persistet,
# we have only three directions: S, N, E. Each of them has equal probability.

def PRRw(K, N, L):
    avg_steps_list = []
    num_step_list = []
    for j in range(K):
        y = random.randint(-L/2, L / 2)
        x = random.randint(-L/2, L / 2)
        num_steps = 0
        while abs(x) <= L / 2 and abs(y) <= L / 2 and num_steps < N:
            num = random.random() #random_num = random.choice(ran_01)
            # num = random_num
            if num > 0.66:
                y = y + 1
            elif 0.33 < num < 0.66:
                y = y - 1
            elif 0 < num < 0.33:
                x = x + 1
            num_steps = num_steps + 1
        num_step_list.append(num_steps)
    avg_step = np.mean(num_step_list)
    return avg_step


# Declare L array to relate L(row number of the cit) and D(avarage distance to be walker leave the region.

L = np.array([i for i in range(8,40, 2)])

# This function calculates the avarage distance for different size lattices. Also check the asymptotic dependency
# N^b.
def L_numstep_dep(K, N, L):
        avg_step_list = []
        b_list = []
        for i in L:
                avg_step = PRRw(K, N, i)
                avg_step_list.append(avg_step)
                b = math.log(avg_step, i)
                b_list.append(b)
        return avg_step_list, np.mean(b_list)

sol = L_numstep_dep(1000,4000,L)
b = sol[1]

# Calculate optimum solution with Linear Regression

curve_fit_lr = LinearRegression(L, sol[0])

# Plots

fig, ax = plt.subplots()
plt.plot(L, sol[0], 'k-', label=' < D >')
plt.plot(L, L**sol[1], 'b*', label='$< D > = L^b$, b = {}'.format(b))
plt.plot(L, curve_fit_lr[1], 'c-', label='y = ax + b, a = {:.2f}, b = {:.2f}'.format(curve_fit_lr[0][1],curve_fit_lr[0][0]))
ax.set_title('Persistent Walk, D vs L(N = 4000, K = 1000, L = 1-40)')
ax.set_xlabel('Number of sites L')
ax.set_ylabel('Avg # of steps for leaving site D')
ax.legend(shadow=True, fancybox=True)
plt.show()