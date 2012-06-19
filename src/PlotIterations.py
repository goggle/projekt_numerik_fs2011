#!/usr/bin/python2
"""Dieses Script plottet die Funktion f(x,z) nach vier verschiedenen Iterationsschritten."""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.io

input_file = 'results/z.txt'
dat = np.loadtxt(input_file)
z1 = dat[:,0]
z2 = dat[:,1]
normNablaJ = dat[:,2]

x = np.arange(0, 1+0.005, 0.005)
y = np.arange(0, 1+0.005, 0.005)
X,Y = np.meshgrid(x,y)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
plt.plot(z1, z2, 'ko')
plt.plot(z1[0], z2[0], 'bo')
plt.plot(z1[len(z1)-1], z2[len(z2)-1], 'ro')



ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.savefig('plots/iterations.pdf')
plt.show()
