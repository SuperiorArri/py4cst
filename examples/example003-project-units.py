from py4cst.cst import Interface
from py4cst.cst.wrappers import Units
from py4cst import cst

interface = Interface()
proj = interface.new_microwave_studio_project()
units = Units(proj)

units.set_frequency_unit(cst.units.FREQUENCY_GIGAHERTZ)
units.set_time_unit(cst.units.TIME_SECOND)
units.set_temperature_unit(cst.units.TEMPERATURE_KELVIN)
units.set_geometry_unit(cst.units.GEOMETRY_MILLIMETER)
