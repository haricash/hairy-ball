### This file is just me fooling around with the package to understand how it works


import numpy as np
import shtns
import matplotlib.pyplot as plt
# import time

# start_time = time.time()

lmax = 2000
mmax = -1

sh = shtns.sht(lmax, mmax)

nlat, nphi = sh.set_grid()
# print("Number of latitudes is", sh.nlat, " and number of longitudes is ", sh.nphi)
el = sh.l
em = sh.m
l2 = el*(el+1)
# l2 = el*(el+1)
# print("The l values are", el, " and the l2 values are", l2)
# print(el.shape, em.shape)
# print(el)

ylm = sh.spec_array() # This is the corresponding sph array. It is a 1D array where each entry
# corresponds to an l value in the el array (I think)
vr = sh.spat_array() # And this is the corresponding spatial array

Vr = np.ones(vr.shape)
Vt = np.ones(vr.shape)
Vp = np.ones(vr.shape)

Qlm = sh.spec_array()  
Slm = sh.spec_array()  
Tlm = sh.spec_array()  

# Qlm, Slm, Tlm

vsh_arr = np.array(sh.analys(Vr, Vt, Vp))

print(vsh_arr.T)

# Vr1, Vt1, Vp1 = sh.synth(Qlm, Slm, Tlm)

# print(Vr1)
# print(Vt1)
# print(Vp1)


# print(Qlm.shape)

# sh.spat_to_SHqst(Vr, Vt, Vp, Qlm, Slm, Tlm)

# print(time.time()-start_time)

# print("Slm is", Slm)
# print("Qlm is", Qlm)
# print("Tlm is", Tlm)

###################################33

# x = np.arange(vr.shape[0])

# X, Y, Z = np.meshgrid(x,
#                       x,
#                       x)

# ax = plt.figure().add_subplot(projection='3d')
# ax.quiver(X, Y, Z, Vr, Vt, Vp)

# def sphere(radius):
#     """This needs to be an object. Include the plotting
#         as a function in here"""
#     r = radius
#     pi = np.pi
#     cos = np.cos
#     sin = np.sin
#     phi, theta = np.mgrid[0.0:pi:200j, 0.0:2.0*pi:200j]
#     x = r*sin(phi)*cos(theta)
#     y = r*sin(phi)*sin(theta)
#     z = r*cos(phi)
#     return x, y, z

# x,y,z = sphere(1)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.plot_surface(
#     x, y, z, rstride=1, cstride=1, color='c', alpha=0.6, linewidth=0)

# plt.show()