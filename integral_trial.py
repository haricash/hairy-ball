import numpy as np

def func(r, t, p):
    return np.power(r, -1)

def integral(f, R, T, P, N_r, N_t, N_p):
    r = np.linspace(0,R,N_r)
    t = np.linspace(0,T,N_t)
    p = np.linspace(0,P,N_p)
    
    r_grid, t_grid, p_grid = np.meshgrid(r, t, p)

    integrand = f(r_grid, t_grid, p_grid) * np.power(r_grid, 2) * np.sin(t_grid)

    return np.sum(integrand) * R * T * P / (N_r * N_t * N_p)

print(integral(func, 5, np.pi, 2*np.pi, 100, 100, 100))
