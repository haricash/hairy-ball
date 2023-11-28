import constants
import numpy as np
import force_u
import conversions
from tests.test import Forces


l = constants.el
RADIUS, HEIGHT = constants.RADIUS, constants.HEIGHT


force_layer_sph = Forces().neutral()
force_layer_vsh = conversions.f_to_VSH(*force_layer_sph)

def main():
    # Compute the wall force
    wall_force = force_u.f_w(force_layer_vsh, l)
    
    # Computing the flow field from the wall force and force layer
    flow_field = force_u.velocity_field(l, wall_force, force_layer_vsh)

    # Converting the flow field to different basis for use
    flow_field_sph = conversions.VSH_to_spat(*flow_field)
    flow_field_cart = conversions.sph_to_cart(*flow_field_sph)

    # Saves the flow field in VSH basis
    np.save("output.npy", flow_field)
    print("Program Finished")

    force_layer_cart = conversions.sph_to_cart(*force_layer_sph)

    wall_force_sph = conversions.VSH_to_spat(*wall_force)
    wall_force_cart = conversions.sph_to_cart(*wall_force_sph)

    # The plotting step
    import plot
    plot.plotter(RADIUS+HEIGHT, force_layer_cart)
    plot.plotter(RADIUS, wall_force_cart)
    plot.plotter(RADIUS+HEIGHT, flow_field_cart)

if __name__ == "__main__":
    main()