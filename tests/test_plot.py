import numpy as np
import shtns
from vsh import *
import matplotlib.pyplot as plt

def sinusoidal_array(m,n):
    m_arr, n_arr = (np.arange(m)+1)/10, (np.arange(n)+1)/10
    return np.cos(np.outer(2*np.pi*m_arr, 2*np.pi*n_arr))

# y = sinusoidal_array(*vr.shape)
y = np.ones(vr.shape)
zlm = sh.analys(y)
y_dash = sh.synth(zlm)
# y_dash = np.roll(y_dash, -2, axis=0)

# print(np.abs(y - y_dash/y))

plt.imshow(y-y_dash)
plt.colorbar()
plt.show()

# plt.imshow(y_dash)
# plt.colorbar()
# plt.show()

plt.plot(zlm)
plt.show()
