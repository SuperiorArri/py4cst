from py4cst.CST import Interface, FarfieldPlot
from py4cst.results import ASCIIFarfieldExporter

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
ffexp = ASCIIFarfieldExporter()

ffexp.set_plot_mode(FarfieldPlot.PLOT_MODE_EFIELD)

farfield_name = 'ff [1]'
ffexp.prepare(proj, farfield_name)
ff = ffexp.export_complex_theta_phi() # array structure (num_theta_samples, num_phi_samples, 2)
print(f'Farfield (theta+phi) | shape: {ff.shape} | data type: {ff.dtype}')

# Extract only theta or phi components
ff_theta = ff[:,:,0]
ff_phi = ff[:,:,1]
print(f'Farfield (theta) | shape: {ff_theta.shape} | data type: {ff_theta.dtype}')
print(f'Farfield (phi) | shape: {ff_phi.shape} | data type: {ff_phi.dtype}')

# Or directly get the components (ffexp.prepare() still needs to be called first!)
ff_theta = ffexp.export_complex_theta()
ff_phi = ffexp.export_complex_phi()

# !!!!!!! IMPORTANT NOTE !!!!!!!
# Exported data contains duplicit values
#  (You obtain farfield values for theta angles: theta = 0° and theta = 180°,
#  and similarly for phi angles: phi = 0° and phi = 360°)
# Tools like farield_utils.get_inner_product() or ffplot always take the redundant samples
#  into account. If you need to remove them manually, you can do it like this:
ff_trun = ff[0:-1,0:-1,:]
print(f'Farfield (theta+phi truncated) | shape: {ff_trun.shape} | data type: {ff_trun.dtype}')
