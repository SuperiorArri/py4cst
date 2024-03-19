from py4cst.CST import Interface, ProjectUnits
from py4cst import CST

interface = Interface()
proj = interface.new_microwave_studio_project()
units = ProjectUnits(proj)

units.set_frequency_unit(CST.units.FREQUENCY_GIGAHERTZ)
units.set_time_unit(CST.units.TIME_SECOND)
units.set_temperature_unit(CST.units.TEMPERATURE_KELVIN)
units.set_geometry_unit(CST.units.GEOMETRY_MILLIMETER)