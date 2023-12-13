import shtns
import numpy as np

lmax = 20
mmax = -1

sh = shtns.sht(lmax, mmax)

nlat, nphi = sh.set_grid()


array_shape = np.array(sh.spat_array()).shape
vsh_array_shape = np.array(sh.spec_array()).shape

el = sh.l
em = sh.m

RADIUS = 20.
HEIGHT = 5.

MU = 10

b = 1
Omega = 1
m = None

def _tangent(theta):
    return np.array([-np.sin(theta), np.cos(theta)])

def _normal(theta):
    return np.array([np.cos(theta), np.sin(theta)])

def _a(theta):
    return _tangent(theta)/(b*Omega)

def _B(theta):
    return np.tensordot(_tangent(theta), _normal(theta), axes=0)/Omega

def _c(theta):
    return b*Omega*_tangent(theta)

def _D(theta):
    return np.eye(2) - np.tensordot(_tangent(theta), _tangent(theta), axes=0)

def _E(theta):
    return b*Omega*np.tensordot(_normal(theta), _tangent(theta), axes=0)

def _G(theta):
    return np.tensordot(_normal(theta), np.eye(2) - np.tensordot(_tangent(theta), _tangent(theta), axes=0), axes=0)

# # This currently will evaluate the FFT for each m
# # If we already know how many m we will be using, 
# # we can rewrite this to directly compute only so
# # many values and store them when the class is instantiated

# Rewrite to make it less clunky, use one function and write them all

class FFT:
    def __init__(self, phi):
        """
            An array for how phi varies
        """
        self.phi = phi

    def array_iter(self,f):
        ret_list = []
        for phi in self.phi:
            ret_list.append(f(phi))
        
        return np.array(ret_list)

    def a_tilde(self):
        a = self.array_iter(_a)
        ms = np.fft.fftfreq(a(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(a(self.phi), axis=0), ms
    
    def B_tilde(self):
        B = self.array_iter(_B)
        ms = np.fft.fftfreq(B(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(B(self.phi), axis=0), ms
    
    def c_tilde(self):
        c = self.array_iter(_c)
        ms = np.fft.fftfreq(c(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(c(self.phi), axis=0), ms

    def D_tilde(self):
        D = self.array_iter(_D)
        ms = np.fft.fftfreq(D(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(D(self.phi), axis=0), ms
    
    def E_tilde(self):
        E = self.array_iter(_E)
        ms = np.fft.fftfreq(E(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(E(self.phi), axis=0), ms
    
    def G_tilde(self):
        G = self.array_iter(_G)
        ms = np.fft.fftfreq(G(self.phi).shape[0])
        ms = ms/ms[1]
        return np.fft.fft(G(self.phi), axis=0), ms