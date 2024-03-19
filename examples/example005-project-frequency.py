from py4cst.CST import Interface, HFSolver, ProjectUnits
from py4cst import CST

interface = Interface()
proj = interface.new_microwave_studio_project()
units = ProjectUnits(proj)
hf_solver = HFSolver(proj)

units.set_frequency_unit(CST.units.FREQUENCY_GIGAHERTZ)
hf_solver.set_frequency_range(5.15, 5.85)