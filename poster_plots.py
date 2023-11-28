import constants
import conversions
import numpy as np
from scipy.ndimage import map_coordinates
from scipy.special import sph_harm
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys

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

file = files[2]

l = np.linspace(-RADIUS-3*HEIGHT, RADIUS+3*HEIGHT, 21)

X, Y, Z = np.meshgrid(l,l,l)


R = np.sqrt(X**2 + Y**2 + Z**2)
THETA = np.arccos(np.nan_to_num(Z/R))
PHI = -np.arctan2(Y,X) + 3*np.pi/2

l,m = constants.el, constants.em


Ax = Ay = Az = np.zeros_like(THETA, dtype=np.complex128)



def cot(x):
    return -np.tan(x + np.pi/2)

length = len(L)

def one_iter(file):

    data = np.load(file)

    A_r = A_t = A_p = np.zeros_like(THETA, dtype=np.complex128)

    for idx in range(length):
    
        alm = data[0][idx]
        blm = data[1][idx]
        clm = data[2][idx]
    
        l = L[idx]
        m = M[idx]
    
        idhu = np.nan_to_num(1j*m*sph_harm(m,l,PHI, THETA)/np.sin(THETA))
        adhu = np.nan_to_num(m*cot(THETA)*sph_harm(m,l,PHI, THETA)+np.sqrt((l-m)*(l+m+1))*np.exp(-1j*PHI)*sph_harm(m+1,l,PHI, THETA))
    
        A_r += np.nan_to_num(alm*sph_harm(m,l, PHI, THETA))
        A_t += np.nan_to_num(blm*adhu - clm*idhu/R)
        A_p += np.nan_to_num(blm*idhu + clm*adhu/R)

    A_x = A_r * np.sin(THETA)*np.cos(PHI) + A_t*np.cos(THETA)*np.cos(PHI) - A_p*np.sin(PHI)
    A_y = A_r * np.sin(THETA)*np.sin(PHI) + A_t*np.cos(THETA)*np.sin(PHI) + A_p*np.cos(PHI)
    A_z = A_r * np.cos(THETA) - A_t * np.sin(THETA)

    return A_x, A_y, A_z

A_x, A_y, A_z = one_iter(folder+file)
# Ax = Ax + A_x
# Ay = Ay + A_y
# Az = Az + A_z

plt.quiver(Z[11,:,:], X[11,:,:], A_z[:,:,11].real, A_x[:,:,11].real)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.quiver(X,Y,Z,A_x,A_y,A_z)

plt.show()

np.save('temp.npy', np.array([Ax, Ay, Az]))