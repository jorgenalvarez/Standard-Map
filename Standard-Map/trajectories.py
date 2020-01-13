from ctypes import *
import numpy as np
from matplotlib import pyplot as plt
from propagation import *

# ---------- Dynamical parameter
mu = 0.5
init_mu(mu)
		
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
