from ctypes import *
import numpy as np
from matplotlib import pyplot as plt
from propagation import *

# Dynamical parameter
mu = 0.5
init_mu(mu)

# ---------- Number of iterations
k = 500

# ---------- Initial state
state = np.zeros(2)
state[0] = 3
state[1] = 0
# ---------- Standard deviation of the observations
sigma = 1.e-3
# ---------- Call propagation function
obslist = sm_observations(state, k, sigma)
# ---------- Plot trajectory
plt.scatter(obslist[:,0], obslist[:,1], s=1)

plt.title(r'Standard map ($\mu$ = {}, $\sigma$ = {:.1E})'.format(mu, sigma))
plt.xlabel('x')
plt.ylabel('y')
plt.show()



