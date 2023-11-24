import numpy as np

DELTA_WIDTH = None # How big the neighbourhood is

def Z(phi, n):
    """
        Input : 
            phi : 2D array of phase values on the surface of a sphere
            n : order of the synchronization parameter
        Output : Order parameter field
    """
    