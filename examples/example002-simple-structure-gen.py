from py4cst.cst import Interface
from py4cst.cst.wrappers import Brick, DiscretePort, Material, Units
from py4cst import cst, material_utils

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.new_microwave_studio_project()
brick = Brick(proj)
discrete_port = DiscretePort(proj)
material = Material(proj)
units = Units(proj)

# Patch parameters for frequency of 5.5 GHz
patch_w = 19.2233905380 # mm
patch_l = 15.3697748305 # mm
patch_s = 5.40358898897 # mm
substrate_h = 508e-3 # mm
copper_t = 32e-3 # mm
padding = 10 # mm

gnd_w = 2*padding + patch_w
gnd_l = 2*padding + patch_l

# Use millimeters as geometry units
units.set_geometry_unit(cst.units.GEOMETRY_MILLIMETER)

# Prepare substrate material
material_utils.prepare_simple_material(material, rel_permeability=3.0)
material.set_name('Substrate')
material.create()

# Generate patch antenna
# - substrate
brick.reset()
brick.set_name('substrate')
brick.set_component('patch_antenna')
brick.set_material('Substrate')
brick.set_x_range(-gnd_w/2, gnd_w/2)
brick.set_y_range(-gnd_l/2, gnd_l/2)
brick.set_z_range(0, substrate_h)
brick.create()
# - ground plane
brick.set_name('ground')
brick.set_material('PEC')
brick.set_z_range(-copper_t, 0)
brick.create()
# - patch
brick.set_name('patch')
brick.set_x_range(-patch_w/2, patch_w/2)
brick.set_y_range(-patch_l/2, patch_l/2)
brick.set_z_range(substrate_h, substrate_h+copper_t)
brick.create()

# Add a discrete port
discrete_port.reset()
discrete_port.set_number(1)
discrete_port.set_type(DiscretePort.PortType.S_PARAMETER)
discrete_port.set_impedance(50)
discrete_port.set_monitor(True)
discrete_port.set_radius(0)
discrete_port.set_point1((0, -patch_l/2+patch_s, substrate_h))
discrete_port.set_point2((0, -patch_l/2+patch_s, 0))
discrete_port.create()
