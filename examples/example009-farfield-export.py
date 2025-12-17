from py4cst.cst import Interface
from py4cst.cst.wrappers import FarfieldPlot
from py4cst.results import ASCIIFarfieldExporter
import numpy as np

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
ffexp = ASCIIFarfieldExporter()

ffexp.set_plot_mode(FarfieldPlot.PlotMode.EFIELD)

farfield_name = 'farfield (f=f0) [1]'
ffexp.prepare(proj, farfield_name)
ff = ffexp.get_complex_theta_phi() # array structure (num_theta_samples, num_phi_samples, 2)
print(f'Farfield (theta+phi) | shape: {ff.shape} | data type: {ff.dtype}')

# Extract only theta or phi components
ff_theta = ff[:,:,0]
ff_phi = ff[:,:,1]
print(f'Farfield (theta) | shape: {ff_theta.shape} | data type: {ff_theta.dtype}')
print(f'Farfield (phi) | shape: {ff_phi.shape} | data type: {ff_phi.dtype}')

# Or directly get the components (ffexp.prepare() still needs to be called first!)
ff_theta = ffexp.get_complex_theta()
ff_phi = ffexp.get_complex_phi()

# There is also a convenience method to get absolute values
ff_abs = ffexp.get_abs()
print(f'Farfield (abs) | shape: {ff_abs.shape} | data type: {ff_abs.dtype}')
# which is equivalent to
ff_abs = np.linalg.norm(ff, axis=2)

# !!!!!!! IMPORTANT NOTE !!!!!!!
# Normally, MWS exports data that contains duplicate values
#  (You obtain farfield values for phi angles: phi = 0° and phi = 360°)
# ASCIIFarfieldExporter takes care of these and removes them so you don't have to.
# But... there are still duplicate values in poles (theta = 0° and theta = 180°)
#  which is the limitation of the way the values are stored (polar coordinate system)
