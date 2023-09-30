import numpy as np

DEFAULT_Z_REF = 50

def convert_s_to_s(s_mat, z_ref: complex, z_ref_new: complex):
    E = np.eye(s_mat.shape[0])
    r = (z_ref_new - z_ref)/(z_ref_new + z_ref)
    r_mat = E*r
    a = np.sqrt(1-np.abs(r)**2)*np.sign(1-r)
    a_mat = E*a
    a_mat_inv = E/a
    return a_mat_inv@(s_mat - r_mat)@np.linalg.inv((E - r_mat@s_mat))@a_mat

def convert_s_to_z(s_mat, z_ref: complex = DEFAULT_Z_REF):
    E = np.eye(s_mat.shape[0])
    sqrt_z_ref_mat = E*np.sqrt(z_ref)
    return sqrt_z_ref_mat@np.linalg.solve(E-s_mat, E+s_mat)@sqrt_z_ref_mat

def convert_z_to_s(z_mat, z_ref: complex = DEFAULT_Z_REF):
    E = np.eye(z_mat.shape[0])
    z_ref_mat = z_ref*E
    return np.linalg.solve(z_mat + z_ref_mat, z_mat - z_ref_mat)

def convert_s_to_y(s_mat, z_ref: complex = DEFAULT_Z_REF):
    E = np.eye(s_mat.shape[0])
    return (E - s_mat) @ np.linalg.inv(z_ref * (E + s_mat))

def convert_y_to_s(y_mat, z_ref: complex = DEFAULT_Z_REF):
    E = np.eye(y_mat.shape[0])
    return np.linalg.solve(E + z_ref*y_mat, E - z_ref*y_mat)

def convert_s_to_abcd(s_mat, z_ref: complex = DEFAULT_Z_REF):
    s11, s12, s21, s22 = s_mat[0][0], s_mat[0][1], s_mat[1][0], s_mat[1][1]
    k = 2*s21
    l = s12*s21
    a = ((1 + s11)*(1 - s22) + l)/k
    b = ((1 + s11)*(1 + s22) - l)/k*z_ref
    c = ((1 - s11)*(1 - s22) - l)/k/z_ref
    d = ((1 - s11)*(1 + s22) + l)/k
    return np.array([[a, b], [c, d]])

def convert_abcd_to_s(abcd_mat, z_ref: complex = DEFAULT_Z_REF):
    a, b, c, d = abcd_mat[0][0], abcd_mat[0][1], abcd_mat[1][0], abcd_mat[1][1]
    k = a + b/z_ref + c*z_ref + d
    s11 = (a + b/z_ref - c*z_ref - d)/k
    s12 = 2*(a*d - b*c)/k
    s21 = 2/k
    s22 = (-a + b/z_ref - c*z_ref + d)/k
    return np.array([[s11, s12], [s21, s22]])

def convert_s_to_h(s_mat, z_ref: complex = DEFAULT_Z_REF):
    s11, s12, s21, s22 = s_mat[0][0], s_mat[0][1], s_mat[1][0], s_mat[1][1]
    delta = (1 - s11)*(1 + s22) + s12*s21
    h11 = ((1 + s11)*(1 + s22) - s12*s21)*z_ref/delta
    h12 = 2*s12/delta
    h21 = -2*s21/delta
    h22 = (((1 - s11)*(1 - s22) - s12*s21))/z_ref/delta
    return np.array([[h11, h12], [h21, h22]])

def convert_h_to_s(h_mat, z_ref: complex = DEFAULT_Z_REF):
    h11, h12, h21, h22 = h_mat[0][0]/z_ref, h_mat[0][1], h_mat[1][0], h_mat[1][1]*z_ref
    delta = (h11 + 1)*(h22 + 1) - h12*h21
    s11 = ((h11 - 1)*(h22 + 1) - h12*h21)/delta
    s12 = 2*h12/delta
    s21 = -2*h21/delta
    s22 = ((1 + h11)*(1 - h22) + h12*h21)/delta
    return np.array([[s11, s12], [s21, s22]])