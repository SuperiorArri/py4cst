from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np
from typing import Optional

class WCS(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'WCS')

    def activate_local(self):
        self.record_method('ActivateWCS', 'local')

    def activate_global(self):
        self.record_method('ActivateWCS', 'global')

    def store(self, name: str):
        self.record_method('Store', name)

    def restore(self, name: str):
        self.record_method('Restore', name)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def set_normal(self, x: float, y: float, z: float):
        self.record_method('SetNormal', x, y, z)

    def set_origin(self, x: float, y: float, z: float):
        self.record_method('SetOrigin', x, y, z)

    def set_u_vector(self, x: float, y: float, z: float):
        self.record_method('SetUVector', x, y, z)

    def align_wcs_with_selected_point(self):
        self.record_method('AlignWCSWithSelected', 'Point')

    def align_wcs_with_selected_3_points(self):
        self.record_method('AlignWCSWithSelected', '3Points')

    def align_wcs_with_selected_edge(self):
        self.record_method('AlignWCSWithSelected', 'Edge')

    def align_wcs_with_selected_edge_center(self):
        self.record_method('AlignWCSWithSelected', 'EdgeCenter')

    def align_wcs_with_selected_rotation_edge(self):
        self.record_method('AlignWCSWithSelected', 'RotationEdge')

    def align_wcs_with_selected_face(self):
        self.record_method('AlignWCSWithSelected', 'Face')

    def rotate_wcs_around_u_deg(self, angle_deg: float):
        self.record_method('RotateWCS', 'u', angle_deg)

    def rotate_wcs_around_u_rad(self, angle_rad: float):
        self.rotate_wcs_around_u_deg(np.rad2deg(angle_rad))

    def rotate_wcs_around_v_deg(self, angle_deg: float):
        self.record_method('RotateWCS', 'v', angle_deg)

    def rotate_wcs_around_v_rad(self, angle_rad: float):
        self.rotate_wcs_around_v_deg(np.rad2deg(angle_rad))

    def rotate_wcs_around_w_deg(self, angle_deg: float):
        self.record_method('RotateWCS', 'w', angle_deg)

    def rotate_wcs_around_w_rad(self, angle_rad: float):
        self.rotate_wcs_around_w_deg(np.rad2deg(angle_rad))

    def move_local_wcs(self, du: float, dv: float, dw: float):
        self.record_method('MoveWCS', 'local', du, dv, dw)

    def move_global_wcs(self, du: float, dv: float, dw: float):
        self.record_method('MoveWCS', 'global', du, dv, dw)

    def align_wcs_with_global_coordinates(self):
        self.record_method('AlignWCSWithGlobalCoordinates')

    def set_workplane_size(self, size: float):
        self.record_method('SetWorkplaneSize', size)

    def set_workplane_raster(self, raster_size: float):
        self.record_method('SetWorkplaneRaster', raster_size)

    def set_workplane_snap(self, flag: bool = True):
        self.record_method('SetWorkplaneSnap', flag)

    def set_workplane_autoadjust(self, flag: bool = True):
        self.record_method('SetWorkplaneAutoadjust', flag)

    def set_workplane_snap_autoadjust(self, flag: bool = True):
        self.record_method('SetWorkplaneSnapAutoadjust', flag)

    def set_workplane_autosnap_factor(self, factor: float):
        self.record_method('SetWorkplaneAutosnapFactor', factor)

    def set_workplane_snap_raster(self, raster_size: float):
        self.record_method('SetWorkplaneSnapRaster', raster_size)

    def is_local_wcs_active(self) -> bool:
        return self.query_method_str('IsWCSActive') == 'local'

    def is_global_wcs_active(self) -> bool:
        return self.query_method_str('IsWCSActive') == 'global'

    def does_exist(self, wcs_name: str) -> bool:
        return self.query_method_bool('DoesExist', wcs_name)

    # returns: (x, y, z)
    def get_origin(self, wcs_name: str) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetOrigin', None, wcs_name, D, D, D)

    def get_normal(self, wcs_name: str) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetNormal', None, wcs_name, D, D, D)

    def get_u_vector(self, wcs_name: str) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetUVector', None, wcs_name, D, D, D)

    # returns: (ux, uy, yz, vx, vy, vz, wx, wy, wz) or None
    def get_affine_matrix_uvw_to_xyz(self, wcs_name: str) \
            -> Optional[tuple[float, float, float, float, float, float, float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetAffineMatrixUVW2XYZ', B, wcs_name, D, D, D, D, D, D, D, D, D)
        return None if not res[0] else res[1:]

    # returns: (ux, uy, yz, vx, vy, vz, wx, wy, wz) or None
    def get_affine_matrix_xyz_to_uvw(self, wcs_name: str) \
            -> Optional[tuple[float, float, float, float, float, float, float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetAffineMatrixXYZ2UVW', B, wcs_name, D, D, D, D, D, D, D, D, D)
        return None if not res[0] else res[1:]

    # returns (u, v, w) or None
    def get_wcs_point_from_global(self, wcs_name: str, x: float, y: float, z: float) \
            -> Optional[tuple[float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetWCSPointFromGlobal', B, wcs_name, D, D, D, x, y, z)
        return None if not res[0] else res[1:]

    # returns: (x, y, z) or None
    def get_global_point_from_wcs(self, wcs_name: str, u: float, v: float, w: float) \
            -> Optional[tuple[float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetGlobalPointFromWCS', B, wcs_name, D, D, D, u, v, w)
        return None if not res[0] else res[1:]