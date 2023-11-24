import constants
import conversions
import numpy as np
import matplotlib.pyplot as plt

RADIUS, HEIGHT = constants.RADIUS, constants.HEIGHT

folder = 'data/'
files = ['output_r3.npy', 
         'output_2r3.npy', 
         'output_r.npy', 
         'output_4r3.npy', 
         'output_5r3.npy', 
         'output_6r3.npy']

files = folder+files

for idx, file in enumerate(files):
    data = np.load(file)
    data = conversions.VSH_to_spat(*data)
    data = conversions.sph_to_cart(*data)
    u,v = data[0], data[1]
    U += u
    V += v

x = np.linspace(-RADIUS-2*HEIGHT, RADIUS+2*HEIGHT, 231)
y = np.linspace(-RADIUS-2*HEIGHT, RADIUS+2*HEIGHT, 231)

X, Y = np.meshgrid(x, y)

plt.imshow(X)
plt.imshow(Y)
plt.imshow(U)
plt.imshow(V)

# plt.streamplot(X, Y, U, V)
plt.show()