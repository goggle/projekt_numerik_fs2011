#!/usr/bin/python2
"""Dieses Script plottet die numerische Loesung u fuer die gefundene Position z* der Quelle f"""
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import scipy.io

def func(x, y):
	return 10 * np.exp( - ( (x-0.5)**2 + (y-0.5)**2 ) / 0.0025 )

t = scipy.io.loadmat('../data/t.mat')['t']# - 1
p = scipy.io.loadmat('../data/p.mat')['p']
b = scipy.io.loadmat('../data/b.mat')['b']# - 1

input_file = 'results/u.txt'
u = np.loadtxt(input_file)


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

x = p[:,0]
y = p[:,1]
plt.tricontourf(x, y, t-1, u, 250, antialiased=False)
#plt.tripcolor(x, y, t-1, u)



plt.colorbar(ticks=[-0.008, -0.006, -0.004, -0.002, 0, 0.002, 0.004, 0.006, 0.008])

#plt.savefig('plots/u.png')
plt.show()
