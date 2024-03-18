import numpy as np

def get_num_theta_samples(ff: np.array) -> int:
    return ff.shape[0]

def get_theta_step_deg(ff: np.array) -> float:
    return 180/(get_num_theta_samples(ff) - 1)

def get_theta_step_rad(ff: np.array) -> float:
    return np.pi/(get_num_theta_samples(ff) - 1)

def get_theta_vec_deg(ff: np.array) -> float:
    return np.arange(get_num_theta_samples(ff))*get_theta_step_deg(ff)

def get_theta_vec_rad(ff: np.array) -> float:
    return np.arange(get_num_theta_samples(ff))*get_theta_step_rad(ff)

def get_num_phi_samples(ff: np.array) -> int:
    return ff.shape[1]

def get_phi_step_deg(ff: np.array) -> float:
    return 360/(get_num_phi_samples(ff) - 1)

def get_phi_step_rad(ff: np.array) -> float:
    return 2*np.pi/(get_num_phi_samples(ff) - 1)

def get_phi_vec_deg(ff: np.array) -> float:
    return np.arange(get_num_phi_samples(ff))*get_phi_step_deg(ff)

def get_phi_vec_rad(ff: np.array) -> float:
    return np.arange(get_num_phi_samples(ff))*get_phi_step_rad(ff)

def get_inner_product(ff1: np.array, ff2: np.array):
    sin_theta_vec = np.array([np.sin(get_theta_vec_rad(ff1))]).T
    theta_grid = np.tile(sin_theta_vec, [1, get_num_phi_samples(ff1)])
    ds = 2*theta_grid*np.sin(get_theta_step_rad(ff1)/2)*get_phi_step_rad(ff1)
    integrand_theta = np.conj(ff1[0:-2,0:-2,0]) * ff2[0:-2,0:-2,0] * ds[0:-2,0:-2]
    integrand_phi = np.conj(ff1[0:-2,0:-2,1]) * ff2[0:-2,0:-2,1] * ds[0:-2,0:-2]
    integral_theta = np.sum(np.sum(integrand_theta))
    integral_phi = np.sum(np.sum(integrand_phi))
    return (integral_theta+integral_phi, integral_theta, integral_phi)

def get_inner_product_single_comp(ff1: np.array, ff2: np.array):
    sin_theta_vec = np.array([np.sin(get_theta_vec_rad(ff1))]).T
    theta_grid = np.tile(sin_theta_vec, [1, get_num_phi_samples(ff1)])
    ds = 2*theta_grid*np.sin(get_theta_step_rad(ff1)/2)*get_phi_step_rad(ff1)
    integrand = np.conj(ff1[0:-2,0:-2]) * ff2[0:-2,0:-2] * ds[0:-2,0:-2]
    integral = np.sum(np.sum(integrand))
    return integral