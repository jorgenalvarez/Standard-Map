from ctypes import *
import numpy as np
from matplotlib import pyplot as plt

# ---------- Import C library
clib = np.ctypeslib.load_library('clib.so', '/home/jorge/ownCloud/PhD/Chaos/Standard Map/Standard-Map/C Library')

# ---------- Call C functions
def sm_iteration (x):
	# Convert parameters to ctype
	xc = (c_double * 2)(*x)
	# Call C function
	clib.standard_map(byref(xc))
	# Modify python parametrs
	for i in range(2): x[i] = xc[i]

	return x

# ---------- Standard map propagation function
def sm_propagation (x, k):
	xlist = x 
	for i in range(k):
		x = sm_iteration(x)
		xlist = np.vstack((xlist, x))
	
	return xlist

# ---------- Dynamical parameter
mu = 0.5
clib.init_mu(c_double(mu))
		
# ---------- Number of iterations
k = 500

# ---------- Initial state
x = np.arange(2.7, 3.7, 0.05)
y = np.arange(-0.7, 0.3, 0.05)
for xi in x:
	for yi in y: 
		state = [xi, yi]

# ---------- Call propagation function
		statelist = sm_propagation(state, k)
# ---------- Plot trajectory
		plt.scatter(statelist[:,0], statelist[:,1], s=1)

plt.title(r'Standard map ($\mu$ = 0.5)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
