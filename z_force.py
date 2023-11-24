import numpy as np
import constants

# When dealing with vector fields, write it down as (Vr, Vt, Vp)
# This will be easy when we want to calculate derivatives as well!

RHO_C = None
ZETA = None
phi_array = None # This would be the array of phi values at a given instant


const = constants.FFT(phi_array)


def Z_to_traction_force(Z, v, m):
    """
        This function will compute the force given the value of the order parameter
    """
    force = RHO_C * ZETA * (const.c_tilde(m) - const.D_tilde(m)) * Z
    stress = (const.E_tilde - np.dot(const.G_tilde, v)) * Z
    stress_term = np.sum(np.gradient(stress))

    # Then sum each over all m

    pass
