import constants
import numpy as np
import force_u
import conversions
import plot

l = constants.el
m = constants.em
RADIUS, HEIGHT = constants.RADIUS, constants.HEIGHT

index = constants.sh.idx(2,1)

Qlm = Slm = Tlm = np.zeros(constants.vsh_array_shape, dtype=np.complex128)

Tlm[index] = 2.0 + 0j

# print(Qlm)

force_layer_vsh = np.array([Qlm, Slm, Tlm])

force_layer_sph = conversions.VSH_to_spat(*force_layer_vsh)
force_layer_cart = conversions.sph_to_cart(*force_layer_sph)

# plot.plotter(RADIUS+HEIGHT, force_layer_cart)

def test():
    # Compute the wall force
    wall_force = force_u.f_w(force_layer_vsh, l)
    
    # Computing the flow field from the wall force and force layer
    flow_field = force_u.velocity_field(l, wall_force, force_layer_vsh)

    # print(l)
    # print(m)
    # print(np.shape(flow_field))
    print(flow_field[0][index],flow_field[1][index],flow_field[2][index])

if __name__ == "__main__":
    test()