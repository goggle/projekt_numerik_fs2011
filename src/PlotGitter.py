#!/usr/bin/python2
"""Dieses Script plottet das vorgegebene Gitter und markiert die Punkte auf dem Rand."""
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import scipy.io

t = scipy.io.loadmat('../data/t.mat')['t']# - 1
p = scipy.io.loadmat('../data/p.mat')['p']
b = scipy.io.loadmat('../data/b.mat')['b']# - 1
uh_b_nr = scipy.io.loadmat('../data/uh_b.mat')['uh_b'][:,0]
uh_b_nr = np.uint16(uh_b_nr) - 1

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

x = p[:,0]
y = p[:,1]
plt.triplot(x, y, t-1, lw=0.6)
ax.plot(x[uh_b_nr], y[uh_b_nr], 'r.')

ax.set_xlim(-0.05,1.05)
ax.set_ylim(-0.05,1.05)

plt.savefig('plots/grid.pdf')
plt.show()
