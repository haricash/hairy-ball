import numpy as np
import constants

# When dealing with vector fields, write it down as (Vr, Vt, Vp)
# This will be easy when we want to calculate derivatives as well!

RHO_C = 1
ZETA = 1
phi_array = np.linspace(0,2*np.pi,100)


const = constants.FFT(phi_array)

def evaluate_m(f, m):
    idx = list(f[1]).index(m)
    return f[0][idx]

def handy_mul(A, B):
    """
        Given a matrix A that is to be multiplied
        everywhere throughout B, this does it for us
    """
    len1,len2 = B.shape[1:]
    C = np.zeros((2,len1, len2))
    for i in range(len1):
        for j in range(len2):
            C[:][i][j] = np.matmul(A,B[:,i,j])
            
    return np.array(C)

# This needs to be made sure that it works over an array where we have our Z values


def Z_to_traction_force(Z, v, m):
    """
        This function will compute the force given the value of the order parameter
        for some order m, which is also the order of the Fourier series

        The velocity is presented with three coordinates on a 2d spherical surface, 
        so we slice it accordingly
    """
    v = v[1:,:,:]

    force_term = (evaluate_m(const.c_tilde(),m) - handy_mul(evaluate_m(const.D_tilde(),m), v)) * Z
    stress = (evaluate_m(const.E_tilde(),m) - np.dot(evaluate_m(const.G_tilde(),m), v)) * Z
    stress_term = np.sum(np.gradient(stress))

    return RHO_C * ZETA * (force_term + stress_term)

trial_Z = np.random.rand(100,100)
vel = np.zeros((3,100,100))
m = 2.

Z_to_traction_force(trial_Z, vel, m)