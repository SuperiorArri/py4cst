from py4cst.CST import Interface
from py4cst.results import ASCIIFarfieldExporter

ifc = Interface(start_mode=Interface.StartMode.Existing)
proj = ifc.get_active_project()

ffexp = ASCIIFarfieldExporter()
ffexp.prepare(proj, 'farfield (f=3) [1]')
print(ffexp.export_complex_theta()[:4])
print(ffexp.export_complex_phi()[:4])