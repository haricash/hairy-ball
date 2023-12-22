"""
    To be continued - the correctv divergence operator
"""
import numpy as np
import tildes

# When dealing with vector fields, write it down as (Vr, Vt, Vp)
# This will be easy when we want to calculate derivatives as well!

RHO_C = 1
ZETA = 1
phi_array = np.linspace(0,2*np.pi,100)

def m_extractor(f,m):
    """
        Gives the phase parameters for given m value
    """
    fun = tildes.tilde(f,tildes.phi_array)
    m_size = fun.shape[0]
    m_array = np.fft.fftfreq(m_size)
    m_array = m_array/m_array[1]
    idx, = np.where(m_array == m)
    return fun[idx]

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
    _c = m_extractor(tildes.c,m)
    _D = m_extractor(tildes.D,m)

    force_term = (_c.reshape(2) - np.matmul(_D , v.reshape(2,-1)).reshape(-1,2)).reshape(2,100,100) * Z
    stress = (m_extractor(tildes.E,m).reshape(2,2) - (np.tensordot(m_extractor(tildes.G,m).reshape(2,2,2), v, axes=1)).reshape(-1,2,2)).reshape(2,2,100,100) * Z
    stress_term = np.sum(np.gradient(stress))

    return RHO_C * ZETA * (force_term + stress_term)

trial_Z = np.random.rand(100,100)
vel = np.zeros((3,100,100))
m = 2.

F = Z_to_traction_force(trial_Z, vel, m)