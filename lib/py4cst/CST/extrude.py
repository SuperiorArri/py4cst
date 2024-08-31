from . import IVBAProvider, VBAObjWrapper
import numpy as np

class Extrude(VBAObjWrapper):
    MODE_POINT_LIST = 'pointlist'
    MODE_PICKS = 'picks'
    MODE_MULTIPLE_PICKS = 'multiplepicks'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Extrude')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def set_component(self, component_name: str):
        self.cache_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.cache_method('Material', mat_name)

    def set_mode(self, mode: str):
        self.cache_method('Mode', mode)

    def set_height(self, height: float):
        self.cache_method('Height', height)

    def set_origin(self, x: float, y: float, z: float):
        self.cache_method('Origin', x, y, z)

    def set_u_vector(self, u: float, v: float, w: float):
        self.cache_method('Uvector', u, v, w)

    def set_v_vector(self, u: float, v: float, w: float):
        self.cache_method('Vvector', u, v, w)

    def set_first_point(self, u: float, v: float):
        self.cache_method('Point', u, v)

    def add_line_to(self, u: float, v: float):
        self.cache_method('LineTo', u, v)

    def add_line_relative(self, u: float, v: float):
        self.cache_method('RLine', u, v)

    def set_taper(self, taper: float):
        self.cache_method('Taper', taper)

    def set_twist_deg(self, angle_deg: float):
        self.cache_method('Twist', angle_deg)

    def set_twist_rad(self, angle_rad: float):
        self.set_twist_deg(np.rad2deg(angle_rad))

    def set_use_picks_for_height(self, flag: bool = True):
        self.cache_method('UsePicksForHeight', flag)

    def set_pick_height_determined_by_first_face(self, flag: bool = True):
        self.cache_method('PickHeightDeterminedByFirstFace', flag)

    def set_num_picked_faces(self, count: int):
        self.cache_method('NumberOfPickedFaces', count)

    def set_delete_base_face_solid(self, flag: bool = True):
        self.cache_method('DeleteBaseFaceSolid', flag)

    def set_clear_picked_face(self, flag: bool = True):
        self.cache_method('ClearPickedFace', flag)

    def modify_height(self):
        self.cache_method('ModifyHeight')
        self.flush_cache('ModifyHeight (Extrude)')

    def set_simplify_active(self, flag: bool = True):
        self.cache_method('SetSimplifyActive', flag)

    def set_simplify_min_points_arc(self, count: int):
        self.cache_method('SetSimplifyMinPointsArc', count)

    def set_simplify_min_points_circle(self, count: int):
        self.cache_method('SetSimplifyMinPointsCircle', count)

    def set_simplify_angle_deg(self, angle_deg: float):
        self.cache_method('SetSimplifyAngle', angle_deg)

    def set_simplify_angle_rad(self, angle_rad: float):
        self.set_simplify_angle_deg(np.rad2deg(angle_rad))

    def set_simplify_adjacent_tol_deg(self, angle_deg: float):
        self.cache_method('SetSimplifyAdjacentTol', angle_deg)

    def set_simplify_adjacent_tol_rad(self, angle_rad: float):
        self.set_simplify_adjacent_tol_deg(np.rad2deg(angle_rad))

    def set_simplify_radius_tol(self, deviation: float):
        self.cache_method('SetSimplifyRadiusTol', deviation)

    def set_simplify_angle_tang_deg(self, angle_deg: float):
        self.cache_method('SetSimplifyAngleTang', angle_deg)

    def set_simplify_angle_tang_rad(self, angle_rad: float):
        self.set_simplify_angle_tang_deg(np.rad2deg(angle_rad))

    def set_simplify_edge_length(self, length: float):
        self.cache_method('SetSimplifyEdgeLength', length)

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create Extrude')
