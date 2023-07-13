from . import Project
from . import ComObjectWrapper
import numpy as np

class Wire(ComObjectWrapper):
    TYPE_BOND_WIRE = 'Bondwire'
    TYPE_CURVE_WIRE = 'Curvewire'

    BOND_WIRE_TYPE_SPLINE = 'Spline'
    BOND_WIRE_TYPE_JEDEC4 = 'JEDEC4'
    BOND_WIRE_TYPE_JEDEC5 = 'JEDEC5'

    TERMINATION_NATURAL = 'natural'
    TERMINATION_ROUNDED = 'rounded'
    TERMINATION_EXTENDED = 'extended'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Wire

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_folder(self, folder_name: str):
        self.invoke_method('Folder', folder_name)

    def set_type(self, wire_type: str):
        self.invoke_method('Type', wire_type)

    def set_bond_wire_type(self, bond_wire_type: str):
        self.invoke_method('BondWireType', bond_wire_type)

    def set_height(self, height: float):
        self.invoke_method('Height', height)

    def set_relative_center_position(self, pos: float):
        self.invoke_method('RelativeCenterPosition', pos)

    def set_point1(self, x: float, y: float, z: float):
        self.invoke_method('Point1', x, y, z, False)

    def set_pick_as_point1(self):
        self.invoke_method('Point1', 0, 0, 0, True)

    def set_point2(self, x: float, y: float, z: float):
        self.invoke_method('Point2', x, y, z, False)

    def set_pick_as_point2(self):
        self.invoke_method('Point2', 0, 0, 0, True)

    def set_alpha_angle_deg(self, angle_deg: float):
        self.invoke_method('Alpha', angle_deg)

    def set_alpha_angle_rad(self, angle_rad: float):
        self.set_alpha_angle_deg(np.rad2deg(angle_rad))

    def set_beta_angle_deg(self, angle_deg: float):
        self.invoke_method('Beta', angle_deg)

    def set_beta_angle_rad(self, angle_rad: float):
        self.set_beta_angle_deg(np.rad2deg(angle_rad))

    def set_curve_name(self, name: str):
        self.invoke_method('Curve', name)

    def set_radius(self, radius: float):
        self.invoke_method('Radius', radius)

    def set_solid_wire_model(self, flag: bool = True):
        self.invoke_method('SolidWireModel', flag)

    def set_material(self, mat_name: str):
        self.invoke_method('Material', mat_name)

    def change_material(self, wire_name: str, material_name: str):
        self.invoke_method('ChangeMaterial', wire_name, material_name)

    def set_termination(self, termination: str):
        self.invoke_method('Termination', termination)

    def enable_advanced_chain_selection(self, flag: bool = True):
        self.invoke_method('AdvancedChainSelection', flag)

    def create(self):
        self.invoke_method('Add')

    def set_solid_name(self, name: str):
        self.invoke_method('SolidName', name)

    def keep_wire_after_conversion(self, flag: bool = True):
        self.invoke_method('KeepWire', flag)

    def convert_to_solid_shape(self):
        self.invoke_method('ConvertToSolidShape')

    def delete(self, wire_name: str):
        self.invoke_method('Delete', wire_name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def set_automesh_fixpoints(self, wire_name: str, flag: bool = True):
        self.invoke_method('SetAutomeshFixpoints', wire_name, flag)

    def set_priority(self, wire_name: str, priority: float):
        self.invoke_method('SetPriority', wire_name, priority)

    def set_material_based_refinement(self, wire_name: str, flag: bool = True):
        self.invoke_method('SetMaterialBasedRefinement', wire_name, flag)

    def set_mesh_step_width(self, wire_name: str, x: float, y: float, z: float):
        self.invoke_method('SetMeshStepwidth', wire_name, x, y, z)

    def set_mesh_step_width_tet(self, wire_name: str, step_width: float):
        #TODO: find out the correct name (instead of abbrev)
        self.invoke_method('SetMeshStepwidthTet', wire_name, step_width)

    def set_mesh_step_width_surface(self, wire_name: str, step_width: float):
        self.invoke_method('SetMeshStepwidthSrf', wire_name, step_width)

    def set_mesh_extend_with(self, x: float, y: float, z: float):
        self.invoke_method('SetMeshExtendwidth', x, y, z)

    def activate_mesh_refinement(self, factor: float):
        self.invoke_method('SetMeshRefinement', True, factor)

    def deactivate_mesh_refinement(self):
        self.invoke_method('SetMeshRefinement', False, 1.0)

    def activate_mesh_volume_refinement(self, factor: float):
        self.invoke_method('SetMeshVolumeRefinement', True, factor)

    def deactivate_mesh_volume_refinement(self):
        self.invoke_method('SetMeshVolumeRefinement', False, 1.0)

    def set_use_for_simulation(self, flag: bool = True):
        self.invoke_method('SetUseForSimulation', flag)

    def get_length(self, wire_name: str):
        return self.invoke_method('GetLength', wire_name)

    def get_grid_length(self, wire_name: str):
        return self.invoke_method('GetGridLength', wire_name)

    def create_folder(self, name: str):
        self.invoke_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.invoke_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.invoke_method('RenameFolder', old_name, new_name)

    def does_folder_exist(self, name: str):
        return self.invoke_method('DoesFolderExist', name)

    def slice(self, name: str):
        self.invoke_method('Slice', name)

    def slice_folder(self, name: str):
        self.invoke_method('SliceFolder', name)