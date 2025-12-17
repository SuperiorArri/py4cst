from py4cst.cst import Interface
from py4cst.cst.wrappers import FarfieldPlot
from py4cst.results import ASCIIFarfieldExporter
from py4cst import ffplot, farfield_utils
import numpy as np

def draw_farfield(ff: np.ndarray):
    theta = farfield_utils.get_theta_vec_deg(ff)
    phi = farfield_utils.get_phi_vec_deg(ff)
    ffplot.plot_farfield_log(ff, theta, phi, dyn_range=40.0, units='dB(V/m)')

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
ffexp = ASCIIFarfieldExporter()

ffexp.set_plot_mode(FarfieldPlot.PlotMode.EFIELD)

farfield_name = 'farfield (f=f0) [1]'
ffexp.prepare(proj, farfield_name)
ff = ffexp.get_abs()

ffplot.new_figure()
draw_farfield(ff)
ffplot.show()
