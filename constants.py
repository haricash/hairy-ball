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

# def tangent(theta):
#     return np.array([-np.sin(theta), np.cos(theta)])

# def normal(theta):
#     return np.array([np.cos(theta), np.sin(theta)])

# def a(theta):
#     return tangent(theta)/(b*Omega)

# def B(theta):
#     return np.outer(tangent(theta), normal(theta))/Omega

# def c(theta):
#     return b*Omega*tangent(theta)

# def D(theta):
#     return np.outer(normal(theta), normal(theta))

# def E(theta):
#     return b*Omega*np.outer(normal(theta), tangent(theta))

# def G(theta):
#     NORMAL = normal(theta)
#     return 2*np.outer(np.outer(NORMAL, NORMAL), NORMAL)


# # This currently will evaluate the FFT for each m
# # If we already know how many m we will be using, 
# # we can rewrite this to directly compute only so
# # many values and store them when the class is instantiated

# class FFT:
#     def __init__(self, phi):
#         """
#             This phi array has 3 spatial directions and along
#             a fourth direction it has how the phi varies
#         """
#         self.phi = phi

#     def a_tilde(self):
#         arr = np.fft.fft(a(self.phi), axis=-1)
#         return np.fft.fft(a(self.phi), axis=-1), np.fft.fftfreq(a(self.phi).shape[-1])
    
#     def B_tilde(self, m):
#         arr = np.fft.fft(B(self.phi), axis=-1)
#         return np.fft.fft(B(self.phi), axis=-1), np.fft.fftfreq(B(self.phi).shape[-1])
    
#     def c_tilde(self, m):
#         arr = np.fft.fft(c(self.phi), axis=-1)
#         return np.fft.fft(c(self.phi), axis=-1), np.fft.fftfreq(c(self.phi).shape[-1])
    
#     def D_tilde(self, m):
#         arr = np.fft.fft(D(self.phi), axis=-1)
#         return np.fft.fft(D(self.phi), axis=-1), np.fft.fftfreq(D(self.phi).shape[-1])
    
#     def E_tilde(self, m):
#         arr = np.fft.fft(E(self.phi), axis=-1)
#         return np.fft.fft(E(self.phi), axis=-1), np.fft.fftfreq(E(self.phi).shape[-1])
    
#     def G_tilde(self, m):
#         arr = np.fft.fft(G(self.phi), axis=-1)
#         return np.fft.fft(G(self.phi), axis=-1), np.fft.fftfreq(G(self.phi).shape[-1])