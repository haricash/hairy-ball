"""
Module that computes the Fourier transform of the 
various cilia phase distribution parameters
"""
import numpy as np

b = 1
Omega = 1
m = None

phi_array = np.linspace(0,2*np.pi,100)

def tangent(theta):
    return np.array([-np.sin(theta), np.cos(theta)])

def normal(theta):
    return np.array([np.cos(theta), np.sin(theta)])

def a(theta):
    return (tangent(theta)/(b*Omega)).T

def B(theta):
    temp_list = list(np.zeros_like(theta))
    for idx,phi in enumerate(theta):
        temp_list[idx] = np.tensordot(tangent(phi), normal(phi), axes=0)/Omega
    return np.array(temp_list)

def c(theta):
    return b*Omega*tangent(theta).T

def D(theta):
    temp_list = list(np.zeros_like(theta))
    for idx,phi in enumerate(theta):
        temp_list[idx] = np.eye(2) - np.tensordot(tangent(phi), tangent(phi), axes=0)
    return np.array(temp_list)

def E(theta):
    temp_list = list(np.zeros_like(theta))
    for idx,phi in enumerate(theta):
        temp_list[idx] = b*Omega*np.tensordot(normal(phi), tangent(phi), axes=0)
    return np.array(temp_list)

def G(theta):
    temp_list = list(np.zeros_like(theta))
    for idx,phi in enumerate(theta):
        temp_list[idx] = np.tensordot(normal(phi), np.eye(2) - np.tensordot(tangent(phi), tangent(phi), axes=0), axes=0)
    return np.array(temp_list)
    
def tilde(f,phi_values):
    """
    Returns the Fourier transform of the ciliary parameter
    """
    evaluated_function = f(phi_values)
    return np.fft.fft(evaluated_function,axis=-1)