from . import Project
from . import ComObjectWrapper
import numpy as np

class Rotate(ComObjectWrapper):
    MODE_POINT_LIST = 'pointlist'
    MODE_PICKS = 'picks'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Rotate

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_component(self, component_name: str):
        self.invoke_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.invoke_method('Material', mat_name)

    def set_mode(self, mode: str):
        self.invoke_method('Mode', mode)

    def set_start_angle_deg(self, angle_deg: float):
        self.invoke_method('StartAngle', angle_deg)

    def set_start_angle_rad(self, angle_rad: float):
        self.set_start_angle_deg(np.rad2deg(angle_rad))

    def set_angle_deg(self, angle_deg: float):
        self.invoke_method('Angle', angle_deg)

    def set_angle_rad(self, angle_rad: float):
        self.set_angle_deg(np.rad2deg(angle_rad))

    def set_height(self, height: float):
        self.invoke_method('Height', height)

    def set_origin(self, x: float, y: float, z: float):
        self.invoke_method('Origin', x, y, z)

    def set_r_vector(self, u: float, v: float, w: float):
        self.invoke_method('Rvector', u, v, w)

    def set_z_vector(self, u: float, v: float, w: float):
        self.invoke_method('Zvector', u, v, w)

    def set_first_point(self, u: float, v: float):
        self.invoke_method('Point', u, v)

    def add_line_to(self, u: float, v: float):
        self.invoke_method('LineTo', u, v)

    def add_line_relative(self, u: float, v: float):
        self.invoke_method('RLine', u, v)

    def set_radius_ratio(self, ratio: float):
        self.invoke_method('RadiusRatio', ratio)

    def modify_angle(self):
        self.invoke_method('ModifyAngle')

    def set_num_steps(self, count: int):
        self.invoke_method('NSteps', count)

    def set_split_closed_edges(self, flag: bool = True):
        self.invoke_method('SplitClosedEdges', flag)

    def set_segmented_profile(self, flag: bool = True):
        self.invoke_method('SegmentedProfile', flag)

    def set_delete_base_face_solid(self, flag: bool = True):
        self.invoke_method('DeleteBaseFaceSolid', flag)

    def set_clear_picked_face(self, flag: bool = True):
        self.invoke_method('ClearPickedFace', flag)

    def set_simplify_solid(self, flag: bool = True):
        self.invoke_method('SimplifySolid', flag)

    def set_use_advanced_segmented_rotation(self, flag: bool = True):
        self.invoke_method('UseAdvancedSegmentedRotation', flag)

    def set_simplify_active(self, flag: bool = True):
        self.invoke_method('SetSimplifyActive', flag)

    def set_simplify_min_points_arc(self, count: int):
        self.invoke_method('SetSimplifyMinPointsArc', count)

    def set_simplify_min_points_circle(self, count: int):
        self.invoke_method('SetSimplifyMinPointsCircle', count)

    def set_simplify_angle_deg(self, angle_deg: float):
        self.invoke_method('SetSimplifyAngle', angle_deg)

    def set_simplify_angle_rad(self, angle_rad: float):
        self.set_simplify_angle_deg(np.rad2deg(angle_rad))

    def set_simplify_adjacent_tol_deg(self, angle_deg: float):
        self.invoke_method('SetSimplifyAdjacentTol', angle_deg)

    def set_simplify_adjacent_tol_rad(self, angle_rad: float):
        self.set_simplify_adjacent_tol_deg(np.rad2deg(angle_rad))

    def set_simplify_radius_tol(self, deviation: float):
        self.invoke_method('SetSimplifyRadiusTol', deviation)

    def set_simplify_angle_tang_deg(self, angle_deg: float):
        self.invoke_method('SetSimplifyAngleTang', angle_deg)

    def set_simplify_angle_tang_rad(self, angle_rad: float):
        self.set_simplify_angle_tang_deg(np.rad2deg(angle_rad))

    def set_simplify_edge_length(self, length: float):
        self.invoke_method('SetSimplifyEdgeLength', length)

    def create(self):
        self.invoke_method('Create')