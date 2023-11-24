import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import constants

RADIUS = constants.RADIUS
HEIGHT = constants.HEIGHT

MU = constants.MU

LMAX = constants.lmax

class MatrixDataset:
    def __init__(self, r, R, lmax):
        self.r = r
        self.R = R
        self.lmax = lmax

    # Not converging as r-->R
    def single_layer(self, l):
        """
            Computes the single layer operator
            Input : 
                    r = Radius of measurement
                    l = Value of l
                    R = Radius of reference
                    outside(bool) : if r > R 
        """

        matrix = np.zeros((3,3))
        r = self.r
        R = self.R


        if r >= R :
            matrix[0][0] = r**(-2-l) * R**(1+l) * l*(l+1) * (
                           (2*l+3)*r**2
                           +
                           (2*l-1)*R**2
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))
        
            matrix[0][1] = r**(-2-l) * R**(1+l) * l*(l+1) * (
                           ((2*l+3)*(l+1)*r**2)
                           -
                           ((l+3)*(2*l-1)*R**2)
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))
        
            matrix[1][0] = r**(-2-l) * R**(1+l) * (
                           (6+l-2*l**2)*r**2
                           +
                           l*(2*l-1)*R**2
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))
        
            matrix[1][1] = r**(-2-l) * R**(1+l) * (l+1) * (
                           (2-l)*(1+l)*(2*l+3)*r**2
                           +
                           l*(l+3)*(2*l-1)*R**2
                           )/(
                           (2*l+1)*(2*l + 8*l**2*(l+2) - 6))
        
            matrix[2][2] = (R**(l+2))/((2*l+1)*(r**(l+1)))

        else:
            matrix[0][0] = r**(l-1) * R**(-l) * l*(l+1) * (
                           (2*l+3)*R**2
                           -
                           (2*l-1)*r**2
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))
        
            matrix[0][1] = r**(l-1) * R**(-l) * l*(l+1)*(
                           (6 * R**2)
                           +
                           (l*(2*l-1)*(r-R)*(r+R))
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))

            matrix[1][0] = r**(l-1) * R**(-l) * (
                           (1+l)*(2*l+3)*R**2
                           -
                           (l+3)*(2*l-1)*r**2
                           )/(
                           (2*l+1) * (8*l*(l+1)-6))
        
            matrix[1][1] = r**(l-1) * R**(-l) * (l+1) * (
                           l*(l+3)*(2*l-1)*r**2
                           -
                           (l-2)*(l+1)*(2*l+3)*R**2
                           )/(
                           (2*l+1)*(2*l + 8*l**2*(l+2) - 6))
        
            matrix[2][2] = r**l/((2*l+1)*R**(l-1))

        return matrix
    
    def matrix_dict(self):
        """
            Constructs a dictionary of matrices for each corresponding
            value of l. This saves a lot of computing time as we don't have
            to spend calculating the matrix for each instance
        """
        matrix_dict = dict(zip(map(str,np.arange(self.lmax+1)), np.arange(self.lmax+1)))
        matrix_dict = {k:self.single_layer(v) for k,v in matrix_dict.items()}
        
        return matrix_dict

####################################################################################

# Internal use functions
def _special_operator_action(inverse, direct, force, l):
    return -np.array([np.matmul(inverse.get(str(L)), direct.get(str(L))).dot(f) for L,f in tqdm(zip(l,force))])

def _flow_field(operators, surface_force, l):
    return 1/MU * np.array([np.matmul(operators.get(str(L)), force) for L,force in tqdm(zip(l,surface_force))])

def _custom_inverse(matrix):
    try :
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError :
        print("Singular matrix encountered")
        return np.zeros((3,3))

#####################################################################################


# Compute the wall force
def f_w(f_l, l):
    """
        Computes the wall force given the layer force. Since the flow field is zero
        on the surface of the sphere we will evaluate the integral on that surface and
        we see that we only need to perform a simple calculation.
        Input :
            f_l : The layer force coeffecients in VSH basis
            l   : The array of l coefficients
            m   : The array of m coefficients
    """
    f_l = np.array(f_l).T
    print(f_l.shape)

    layer_operators = MatrixDataset(RADIUS+HEIGHT, RADIUS, LMAX).matrix_dict()

    print("Inverting Operators")
    inv_wall_operators = {k:_custom_inverse(v) for k,v in tqdm(MatrixDataset(RADIUS, RADIUS, LMAX).matrix_dict().items())}
    print("Inverting finished!")
    
    print("Computing wall force")
    wall_force = _special_operator_action(inv_wall_operators, layer_operators, f_l, l)
    print("Wall force computation done!")

    return wall_force.T
    


# Calculating the velocity field
def velocity_field(l, wall_force, layer_force):
    """
        Given the wall force and force from the ciliary layer,
        this function computes the velocity field. The output 
        should be three scalar fields, each corresponding to one
        component of the vector spherical harmonic.

        The Green's function is just that of the free space impulse response
    """
    wall_force = wall_force.T
    layer_force = layer_force.T

    wall_operators = MatrixDataset(RADIUS+HEIGHT, RADIUS, LMAX).matrix_dict()
    layer_operators = MatrixDataset(RADIUS+HEIGHT, RADIUS+HEIGHT, LMAX).matrix_dict()

    print("Computing Flow Field")
    wall_contribution = _flow_field(wall_operators, wall_force, l)
    layer_contribution = _flow_field(layer_operators, layer_force, l)
    print("Flow Field Computation Done!")

    
    return (wall_contribution + layer_contribution).T