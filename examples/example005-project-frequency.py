from py4cst.cst import Interface
from py4cst.cst.wrappers import Solver, Units
from py4cst import cst

interface = Interface()
proj = interface.new_microwave_studio_project()
units = Units(proj)
hf_solver = Solver(proj)

units.set_frequency_unit(cst.units.FREQUENCY_GIGAHERTZ)
hf_solver.set_frequency_range(5.15, 5.85)
