import lib_test
from py4cst import matrix_conversions
import numpy as np

Z_REF_MIN = 1
Z_REF_MAX = 100
Z_REF_STEP = 1

s_mat = np.array([
    [10+1j, 2+0.3j],
    [2+0.3j,10+1j]
])

for z_ref in range(Z_REF_MIN, Z_REF_MAX+1, Z_REF_STEP):
    abcd_mat = matrix_conversions.convert_s_to_abcd(s_mat, z_ref)
    s_mat2 = matrix_conversions.convert_abcd_to_s(abcd_mat, z_ref)
    assert(np.allclose(s_mat, s_mat2))

for z_ref in range(Z_REF_MIN, Z_REF_MAX+1, Z_REF_STEP):
    z_mat = matrix_conversions.convert_s_to_z(s_mat, z_ref)
    s_mat2 = matrix_conversions.convert_z_to_s(z_mat, z_ref)
    assert(np.allclose(s_mat, s_mat2))

for z_ref in range(Z_REF_MIN, Z_REF_MAX+1, Z_REF_STEP):
    s_mat2a = matrix_conversions.convert_s_to_s(s_mat, z_ref, Z_REF_MAX)
    s_mat2 = matrix_conversions.convert_s_to_s(s_mat2a, Z_REF_MAX, z_ref)
    assert(np.allclose(s_mat, s_mat2))

for z_ref in range(Z_REF_MIN, Z_REF_MAX+1, Z_REF_STEP):
    y_mat = matrix_conversions.convert_s_to_y(s_mat, z_ref)
    s_mat2 = matrix_conversions.convert_y_to_s(y_mat, z_ref)
    assert(np.allclose(s_mat, s_mat2))

for z_ref in range(Z_REF_MIN, Z_REF_MAX+1, Z_REF_STEP):
    h_mat = matrix_conversions.convert_s_to_h(s_mat, z_ref)
    s_mat2 = matrix_conversions.convert_h_to_s(h_mat, z_ref)
    assert(np.allclose(s_mat, s_mat2))

lib_test.finalize()