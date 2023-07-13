# Welcome to py4cst

This is a small python library that provides wrappers for CST Studio Suite win32com object and also some useful high level tools to setup your projects and to read out the results.

**Be aware the library in it's current state is highly untested and will change a lot even in it's core. Any contributions are welcome.**

# Installation

The library is currently not available through pip. So to use it, you need to add it manually to the PYTHONPATH environment variable. Clone the repository so it's root directory path is `<DIR>` (path of your choice). There are two ways to modify PYTHONPATH variable. One is through code, which you need to add before importing the library itself:

    import sys.path
    import os.path

	sys.path.append(os.path.join('<DIR>', 'lib'))

	# your imports of the library (for example):
	from py4cst import CST

Where `<DIR>` has to be replaced with the directory of your choice.

The second option is through Windows Control Panel. Open the start menu and search for `Edit the system environment variables`.
Click on `Environment Variables...` button. Add or modify environment variable `PYTHONPATH` so it contains path `<DIR>/lib`.

# Known issues

There is sometimes a problem with win32com Dispatcher complaining. The solution is to delete `%TMP%/gen_py` in your filesystem. There is also an option to do so via the library itself:

    from py4cst.CST import Interface
    Interface.clear_cache()

It should resolve the problem. Otherwise try deleting other python cache directories.

# Examples

## Create a Microwave Studio project

	from py4cst.CST import Interface, Project

	# use the latest installed version of CST Studio Suite
	interface = Interface()
	# or use a specific version:
	# interface = Interface(version=2023)

	interface.create_new_mws_project()
	project = Project(interface)
	# project.close_without_saving()

This script activates the silent/scripting mode and creates an empty MWS project. By creating an instance of class `Project` you are refering to the current active project in the editor. All methods available for the project instance are wrappers for VBA methods described in the official documentation of CST Studio Suite. Sometimes the methods have the same name, just in snake case style, sometimes the methods have more understandable names. You can always find the wrapper method name by searching the VBA method name in the source code.

## Generate a simple patch antenna
To generate such a structure, we take the same approach as with VBA. We need to obtain objects like Brick, Solid and ProjectUnits and call their respective functions to perform the setup. Using the methods of these objects will also always ensure that the correct project is selected.

	from py4cst.CST import Interface
	from py4cst.CST import Project
	from py4cst.CST import ProjectUnits
	from py4cst.CST import Brick
	from py4cst.CST import HFSolver
	from py4cst.CST import Material
	from py4cst.CST import Solid
	from py4cst.CST import Boundary
	from py4cst.CST import Port
	from py4cst.CST import Monitor
	from py4cst.CST import MeshSettings
	from py4cst.CST import units
	from py4cst.results import Farfields
	from py4cst import CST
	from py4cst import material_utils

	# Python parameters in basic units to demonstrate unit conversions later
	CONDUCTOR_THICKNESS = 35e-6 # m
	GROUND_WIDTH = 80e-3 # m
	GROUND_LENGTH = 80e-3 # m

	# Other python parameters in project units:
	F_DESIGN = 2.4 # GHz
	F_MIN = F_DESIGN-F_DESIGN*0.5 # GHz
	F_MAX = F_DESIGN+F_DESIGN*0.5 # GHz
	SUBSTRATE_HEIGHT = 1.5 # mm
	PATCH_WIDTH = 48.62 # mm
	PATCH_LENGTH = 40.49 # mm
	FEED_WIDTH = 2.98 # mm
	PORT_MARGIN_X = 8 # mm
	PORT_MARGIN_Y = 8 # mm

	interface = Interface()
	interface.create_new_mws_project()
	project = Project(interface)

	# Setup units:
	# if you use unit conversions everywhere, this step is not necessary
	proj_units = ProjectUnits(project)
	proj_units.set_frequency_unit(units.FREQUENCY_GIGAHERTZ)
	proj_units.set_geometry_unit(units.GEOMETRY_MILLIMETER)
	proj_units.set_temperature_unit(units.TEMPERATURE_KELVIN)
	proj_units.set_time_unit(units.TIME_NANOSECOND)

	# Setup project parameters: (just for demonstration, not necessary)
	project.store_parameter_with_description('f_min', F_MIN, 'Minimum project frequency.')
	project.store_parameter('f_max', F_MAX)

	# Generate ground plane:
	geometry_factor = units.get_geometry_si_to_unit_factor()
	gnd_width_in_proj_units = GROUND_WIDTH*geometry_factor
	gnd_length_in_proj_units = GROUND_LENGTH*geometry_factor
	conductor_thickness_in_proj_units = CONDUCTOR_THICKNESS*geometry_factor

	brick = Brick(project)
	brick.reset()
	brick.set_name('ground_plane')
	brick.set_component('patch_antenna')
	brick.set_material('PEC')
	brick.set_x_range(-gnd_width_in_proj_units/2, gnd_width_in_proj_units/2)
	brick.set_y_range(-gnd_length_in_proj_units/2, gnd_length_in_proj_units/2)
	brick.set_z_range(-conductor_thickness_in_proj_units, 0)
	brick.create()

	# Setup custom dielectric using helper functions:
	material = Material(project)
	material_utils.prepare_simple_material(material, rel_permeability=2.3)
	material.set_name('dielectric_material')
	material.set_color_hsva(0.12, 1.0, 1.0, 0.4)
	material.create()

	# Generate dielectric:
	brick.reset()
	brick.set_name('dielectric')
	brick.set_component('patch_antenna')
	brick.set_material('dielectric_material')
	brick.set_x_range(-gnd_width_in_proj_units/2, gnd_width_in_proj_units/2)
	brick.set_y_range(-gnd_length_in_proj_units/2, gnd_length_in_proj_units/2)
	brick.set_z_range(0, SUBSTRATE_HEIGHT)
	brick.create()

	# Generate patch:
	brick = Brick(project)
	brick.reset()
	brick.set_name('patch')
	brick.set_component('patch_antenna')
	brick.set_material('PEC')
	brick.set_x_range(-PATCH_WIDTH/2, PATCH_WIDTH/2)
	brick.set_y_range(-PATCH_LENGTH/2, PATCH_LENGTH/2)
	brick.set_z_range(SUBSTRATE_HEIGHT, SUBSTRATE_HEIGHT+conductor_thickness_in_proj_units)
	brick.create()

	# Generate feed:
	brick = Brick(project)
	brick.reset()
	brick.set_name('feed')
	brick.set_component('patch_antenna')
	brick.set_material('PEC')
	brick.set_x_range(-FEED_WIDTH/2, FEED_WIDTH/2)
	brick.set_y_range(-gnd_length_in_proj_units/2, -PATCH_LENGTH/2)
	brick.set_z_range(SUBSTRATE_HEIGHT, SUBSTRATE_HEIGHT+conductor_thickness_in_proj_units)
	brick.create()

	# Add port:
	port = Port(project)
	port.reset()
	port.set_number(1)
	port.set_coordinates(Port.COORDINATES_FREE)
	port.set_orientation(Port.ORIENTATION_YMAX)
	port.set_x_range(-FEED_WIDTH/2-PORT_MARGIN_X, FEED_WIDTH/2+PORT_MARGIN_X)
	port.set_y_position(-gnd_length_in_proj_units/2)
	port.set_z_range(
		-conductor_thickness_in_proj_units,
		SUBSTRATE_HEIGHT+conductor_thickness_in_proj_units+PORT_MARGIN_Y)
	port.set_reference_plane_distance(0)
	port.set_number_of_modes(1)
	port.set_on_boundaries(False)
	port.set_waveguide_monitor(False)
	port.create()

	# Optinally we can merge feed and patch together:
	solid = Solid(project)
	solid.perform_add_operation('patch_antenna:patch', 'patch_antenna:feed')

	# Setup solver:
	project.set_solver_type(Project.SOLVER_HF_TIME_DOMAIN) # not necessary (default solver type)

	# Setup frequency range (using previously defined parameters):
	hf_solver = HFSolver(project)
	hf_solver.set_frequency_range('f_min', 'f_max')

	#   It can be of course done without parameters
	#   hf_solver.set_frequency_range(F_MIN, F_MAX)

	# Setup boundaries:
	boundary = Boundary(project)
	boundary.set_types_x(Boundary.BOUNDARY_EXPANDED_OPEN, Boundary.BOUNDARY_EXPANDED_OPEN)
	boundary.set_types_y(Boundary.BOUNDARY_EXPANDED_OPEN, Boundary.BOUNDARY_EXPANDED_OPEN)
	boundary.set_types_z(Boundary.BOUNDARY_EXPANDED_OPEN, Boundary.BOUNDARY_EXPANDED_OPEN)
	boundary.set_symmetries(Boundary.SYMMETRY_NONE, Boundary.SYMMETRY_NONE, Boundary.SYMMETRY_NONE)
	boundary.set_apply_in_all_directions(False)

	# Setup farfield monitor:
	monitor = Monitor(project)
	#   we use Farfields.get_name so we can later use helper class Farfields to get the results later
	monitor.set_name(Farfields.get_name(frequency=F_DESIGN, port=1))
	monitor.set_domain(Monitor.DOMAIN_FREQUENCY)
	monitor.set_field_type(Monitor.FIELD_TYPE_FARFIELD)
	monitor.set_monitor_value(F_DESIGN)
	monitor.set_export_farfield_source(False)
	monitor.create()

	# Setup mesh:
	mesh_settings = MeshSettings(project)
	mesh_settings.set_mesh_type(MeshSettings.MESH_TYPE_HEX)
	mesh_settings.set_number_of_steps_per_wave_near(25)
	mesh_settings.set_number_of_steps_per_wave_far(25)
	mesh_settings.set_wavelength_refinement_same_as_near(False)

## Analyze the patch antenna
