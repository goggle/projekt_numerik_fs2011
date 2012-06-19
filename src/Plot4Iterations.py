#!/usr/bin/python2
"""Dieses Script plottet die Funktion f(x,z) nach vier verschiedenen Iterationsschritten."""
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

fig = plt.figure()
#ax = fig.add_subplot(111, aspect='equal')
plt.subplots_adjust(hspace=0.4)
plt.subplot(2,2,1)
i = 0
Z = func(X, Y, z1[i], z2[i])
plt.contour(X, Y, Z, 10, cmap=cm.Reds)
#plt.plot(z1[i], z2[i], 'o', color='black')
cs = plt.contourf(X, Y, Z, 10, cmap=cm.Reds)
cbar = plt.colorbar()
plt.title('f(x,z) nach ' + str(i) + ' Iterationen')
z1_str = "%.2f" %z1[i]
z2_str = "%.2f" %z2[i]
plt.text(0.25, 0.35, 'z = (' + z1_str + ', ' + z2_str + ')')

plt.subplot(2,2,2)
i = 5
Z = func(X, Y, z1[i], z2[i])
plt.contour(X, Y, Z, 10, cmap=cm.Reds)
cs = plt.contourf(X, Y, Z, 10, cmap=cm.Reds)
cbar = plt.colorbar()
plt.title('f(x,z) nach ' + str(i) + ' Iterationen')
z1_str = "%.2f" %z1[i]
z2_str = "%.2f" %z2[i]
plt.text(0.25, 0.35, 'z = (' + z1_str + ', ' + z2_str + ')')

plt.subplot(2,2,3)
i = 8
Z = func(X, Y, z1[i], z2[i])
plt.contour(X, Y, Z, 10, cmap=cm.Reds)
cs = plt.contourf(X, Y, Z, 10, cmap=cm.Reds)
cbar = plt.colorbar()
plt.title('f(x,z) nach ' + str(i) + ' Iterationen')
z1_str = "%.2f" %z1[i]
z2_str = "%.2f" %z2[i]
plt.text(0.25, 0.50, 'z = (' + z1_str + ', ' + z2_str + ')')

plt.subplot(2,2,4)
i = 16
Z = func(X, Y, z1[i], z2[i])
plt.contour(X, Y, Z, 10, cmap=cm.Reds)
cs = plt.contourf(X, Y, Z, 10, cmap=cm.Reds)
cbar = plt.colorbar()
plt.title('f(x,z) nach ' + str(i) + ' Iterationen')
z1_str = "%.2f" %z1[i]
z2_str = "%.2f" %z2[i]
plt.text(0.25, 0.60, 'z = (' + z1_str + ', ' + z2_str + ')')

plt.savefig('plots/f.pdf')
plt.show()
