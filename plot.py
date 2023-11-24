import constants
import conversions
import numpy as np
import matplotlib.pyplot as plt
# from mayavi import mlab

NLAT, NPHI = constants.nlat, constants.nphi
RADIUS, HEIGHT = constants.RADIUS, constants.HEIGHT

##########################################################
def _spherical_grid(RADIUS, NLAT, NPHI):
    theta = (np.arange(NLAT)+1) * np.pi/NLAT
    phi = (np.arange(NPHI)+1) * 2*np.pi/NPHI

    X = RADIUS * np.outer(np.sin(theta), np.cos(phi))
    Y = RADIUS * np.outer(np.sin(theta), np.sin(phi))
    Z = RADIUS * np.outer(np.cos(theta), np.ones(NPHI))

    return X, Y, Z
    
##############################################################

organism_grid = _spherical_grid(RADIUS, NLAT, NPHI)

# velocity_table = conversions.sph_to_cart(U_r, U_t, U_p, NLAT, NPHI)


def plotter(radius, velocities):
    grid = _spherical_grid(radius, NLAT, NPHI)
    ax = plt.figure().add_subplot(projection='3d')
    # ax.plot_surface(*organism_grid, color='white')
    ax.quiver(*grid, *velocities, cmap=plt.cm.jet)

    plt.show()


# def mayavi_plotter(radius, velocities):
    # mlab.flow(*_spherical_grid(radius, NLAT, NPHI), velocities)
    # mlab.show()