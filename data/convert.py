import conversions
import numpy as np

files = ['output_r3.npy', 
         'output_2r3.npy', 
         'output_r.npy', 
         'output_4r3.npy', 
         'output_5r3.npy', 
         'output_6r3.npy']

for file in files:
	data = np.load(file)
	data = conversions.VSH_to_spat(*data)
	data = conversions.sph_to_cart(*data)
	data = np.array(data)
	data.astype('float32').tofile(file[:-4]+'.dat')


