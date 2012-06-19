#!/usr/bin/python2
"""Dieses Script plottet die Funktion f(z) nach jedem Iterationsschritt des Steepest Descent Verfahrens
und speichert sie ab."""
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.io

def func(x, y, w, z):
	return 10 * np.exp( - ( (x-w)**2 + (y-z)**2 ) / 0.0025 )

input_file = 'results/z.txt'
dat = np.loadtxt(input_file)
z1 = dat[:,0]
z2 = dat[:,1]
normNablaJ = dat[:,2]

x = np.arange(0, 1+0.005, 0.005)
y = np.arange(0, 1+0.005, 0.005)
X,Y = np.meshgrid(x,y)

# Plotte f nach jedem Iterationsschritt und speichere die Plots ab:
for i in range(0, len(z1)):
	fig = plt.figure()
	ax = fig.add_subplot(111, aspect='equal')
	Z = func(X, Y, z1[i], z2[i])
	plt.contour(X, Y, Z, 10, cmap=cm.Reds)
	cs = plt.contourf(X, Y, Z, 10, cmap=cm.Reds)
	cbar = plt.colorbar()
	z1_str = "%.2f" %z1[i]
	z2_str = "%.2f" %z2[i]
	plt.title('Funktion f(x,z) mit z = (' + z1_str + ', ' + z2_str + ')')
	ind_str = "%.2d" %i
	plt.savefig('plots/f' + ind_str + '.png')
