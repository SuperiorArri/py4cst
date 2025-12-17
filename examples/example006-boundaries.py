from py4cst.cst import Interface
from py4cst.cst.wrappers import Boundary

interface = Interface()
proj = interface.new_microwave_studio_project()
boundary = Boundary(proj)

boundary.set_symmetry_x(Boundary.SymmetryType.ELECTRIC)
boundary.set_symmetry_y(Boundary.SymmetryType.ELECTRIC)
boundary.set_symmetry_z(Boundary.SymmetryType.NONE)
boundary.set_apply_in_all_directions(False)
boundary.set_type_x_max(Boundary.BoundaryType.EXPANDED_OPEN)
boundary.set_type_y_max(Boundary.BoundaryType.EXPANDED_OPEN)
boundary.set_type_z_min(Boundary.BoundaryType.ELECTRIC)
boundary.set_type_z_max(Boundary.BoundaryType.EXPANDED_OPEN)
