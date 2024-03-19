from py4cst.CST import Interface, Boundary

interface = Interface()
proj = interface.new_microwave_studio_project()
boundary = Boundary(proj)

boundary.set_symmetries(Boundary.SYMMETRY_ELECTRIC, Boundary.SYMMETRY_ELECTRIC, Boundary.SYMMETRY_NONE)
boundary.set_apply_in_all_directions(False)
boundary.set_type_x_max(Boundary.BOUNDARY_EXPANDED_OPEN)
boundary.set_type_y_max(Boundary.BOUNDARY_EXPANDED_OPEN)
boundary.set_types_z(Boundary.BOUNDARY_ELECTRIC, Boundary.BOUNDARY_EXPANDED_OPEN)