from py4cst.CST import Interface, FarfieldPlot
from py4cst.results import ASCIIFarfieldExporter
from py4cst import farfield_utils

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
ffexp = ASCIIFarfieldExporter()

ffexp.set_plot_mode(FarfieldPlot.PLOT_MODE_EFIELD)

farfield_name = 'ff [1]'
ffexp.prepare(proj, farfield_name)
ff = ffexp.export_complex_theta_phi()

print(f'Num theta samples: {farfield_utils.get_num_theta_samples(ff)}')
print(f'Theta step (degrees): {farfield_utils.get_theta_step_deg(ff)}')
print(f'Theta step (radians): {farfield_utils.get_theta_step_rad(ff)}')
print(f'Theta vector (degrees): {farfield_utils.get_theta_vec_deg(ff)}')
print(f'Theta vector (radians): {farfield_utils.get_theta_vec_rad(ff)}')

print(f'Num phi samples: {farfield_utils.get_num_phi_samples(ff)}')
print(f'Phi step (degrees): {farfield_utils.get_phi_step_deg(ff)}')
print(f'Phi step (radians): {farfield_utils.get_phi_step_rad(ff)}')
print(f'Phi vector (degrees): {farfield_utils.get_phi_vec_deg(ff)}')
print(f'Phi vector (radians): {farfield_utils.get_phi_vec_rad(ff)}')

ip_total, ip_theta, ip_phi = farfield_utils.get_inner_product(ff, ff)
print('Inner product:')
print(f'- total: {ip_total}')
print(f'- theta component: {ip_theta}')
print(f'- phi component: {ip_phi}')

e_theta = ff[:,:,0]
ip_single_comp = farfield_utils.get_inner_product_single_comp(e_theta, e_theta)
print(f'Inner product (theta component only): {ip_single_comp}')