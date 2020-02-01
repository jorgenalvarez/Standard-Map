from ctypes import *
import numpy as np

# ---------- Import C library
clib = np.ctypeslib.load_library('clib.so', '/home/jorge/ownCloud/PhD/Chaos/Standard Map/Standard-Map/C Library')

# ---------- Initialize dynamical parameter
def init_mu(mu):
	clib.init_mu(c_double(mu))

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

# ---------- Standard map observations function  
def sm_propagation_noisy (x, k, sigma):
        xlist = x
        for i in range(k):
                x = sm_iteration(x)
                obs = np.random.normal(x, sigma)
                xlist = np.vstack((xlist, obs))

        return xlist

