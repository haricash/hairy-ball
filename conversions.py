import numpy as np
import constants
import conversions

NLAT, NPHI = constants.nlat, constants.nphi


def spat_to_VSH(Ar, At, Ap):
    """
        This function transforms the input scalar fields that correspond
        to a spherical coordinate system's vector components into their 
        vector spherical harmonic component scalar fields.

        Note that the input args have to be of the form sh.spat_array()
        
        Input :
            Ar : Radial component field
            At : Component field along theta direction (latitude)
            Ap : Component field along phi direction (logitude)
        Output :
            Qlm, Slm, Tlm
    """
    return constants.sh.analys(Ar, At, Ap)

def VSH_to_spat(Qlm, Slm, Tlm):
    """
        This function transforms the input vector spherical harmonic components
        into spherical coordinate component fields.

        Note that the input array must be of the form sh.spec_array()

        Input :
            Qlm, Slm, Tlm
        Output :
            Ar, At, Ap
    """
    return constants.sh.synth(Qlm, Slm, Tlm)

def sph_to_cart(u_r, u_t, u_p, NLAT=NLAT, NPHI=NPHI):
    """
        Converts vector fields from spherical basis to cartesian
        basis on the surface of the sphere
    """
    theta = np.arange(NLAT) * np.pi/NLAT
    phi = np.arange(NPHI) * 2*np.pi/NPHI

    u_x =   (u_r * np.outer(np.sin(theta), np.cos(phi))
            +
            u_t * np.outer(np.cos(theta), np.cos(phi))
            -
            u_p * np.outer(np.ones(NLAT), np.sin(phi)))

    u_y =   (u_r * np.outer(np.sin(theta), np.sin(phi))
            +
            u_t * np.outer(np.cos(theta), np.sin(phi))
            +
            u_p * np.outer(np.ones(NLAT), np.cos(phi)))

    u_z =   (u_r * np.outer(np.cos(theta), np.ones(NPHI))
            -
            u_t * np.outer(np.sin(theta), np.ones(NPHI)))

    return u_x, u_y, u_z

def f_to_VSH(f_r, f_t, f_p):
    f = np.array([f_r, f_t, f_p])
    f_vsh = conversions.spat_to_VSH(*f)
    return np.array(f_vsh)

def sph_divergence(field):
    """
        Computes the divergence of the input spherical coordinate vector field
    """
    Ax, Ay, Az = sph_to_cart(*field)
    ### sp is the difference in the coordinate position
    return np.sum(np.sum(np.array([np.gradient(f[i],sp) for i in range(3)]), axis=0),axis=0)

