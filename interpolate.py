import constants
import conversions
import numpy as np
from scipy.ndimage import map_coordinates
from scipy.special import sph_harm
import matplotlib.pyplot as plt
from tqdm import tqdm

NLAT, NPHI = constants.nlat, constants.nphi
RADIUS, HEIGHT = constants.RADIUS, constants.HEIGHT
L,M = constants.el, constants.em

folder = 'data/'
files = ['output_r3.npy', 
         'output_2r3.npy', 
         'output_r.npy', 
         'output_4r3.npy', 
         'output_5r3.npy', 
         'output_6r3.npy']

