import numpy as np
import constants
import conversions

class Forces():        

    def neutral(self):
        """
            All the forces point in the same theta direction,
            towards one of the poles.
        """
        f_r = np.zeros((constants.array_shape))
        f_t = np.ones((constants.array_shape))
        f_p = np.zeros((constants.array_shape))

        return np.array([f_r, f_t, f_p])
    
    def rotation(self):
        """
            All the forces point in the azimuthal direction
        """
        f_r = np.zeros(constants.array_shape)
        f_t = np.zeros(constants.array_shape)
        f_p = np.ones(constants.array_shape)

        return np.array([f_r, f_t, f_p])
    

