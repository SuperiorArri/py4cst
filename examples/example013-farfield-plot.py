from py4cst.CST import Interface, FarfieldPlot
from py4cst.results import ASCIIFarfieldExporter
from py4cst import ffplot
import numpy as np

def draw_farfield(ff: np.array):
    e_tot = np.sqrt(np.sum(np.abs(ff)**2, 2))
    theta = np.linspace(0, 180, ff.shape[0])
    phi = np.linspace(0, 360, ff.shape[1])
    ffplot.plot_farfield_log(e_tot, theta, phi, dyn_range=40.0, units='V/m')

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
ffexp = ASCIIFarfieldExporter()

ffexp.set_plot_mode(FarfieldPlot.PLOT_MODE_EFIELD)

farfield_name = 'ff [1]'
ffexp.prepare(proj, farfield_name)
ff = ffexp.export_complex_theta_phi()

ffplot.new_figure()
draw_farfield(ff)
ffplot.show()