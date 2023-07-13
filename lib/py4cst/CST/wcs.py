from . import Project
from . import ComObjectWrapper
from . import w32com
import numpy as np

class WCS(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.WCS

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def activate_local(self):
        self.invoke_method('ActivateWCS', 'local')

    def activate_global(self):
        self.invoke_method('ActivateWCS', 'global')

    def store(self, name: str):
        self.invoke_method('Store', name)

    def restore(self, name: str):
        self.invoke_method('Restore', name)

    def delete(self, name: str):
        self.invoke_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def set_normal(self, x: float, y: float, z: float):
        self.invoke_method('SetNormal', x, y, z)

    def set_origin(self, x: float, y: float, z: float):
        self.invoke_method('SetOrigin', x, y, z)

    def set_u_vector(self, x: float, y: float, z: float):
        self.invoke_method('SetUVector', x, y, z)

    def align_wcs_with_selected_point(self):
        self.invoke_method('AlignWCSWithSelected', 'Point')

    def align_wcs_with_selected_3_points(self):
        self.invoke_method('AlignWCSWithSelected', '3Points')

    def align_wcs_with_selected_edge(self):
        self.invoke_method('AlignWCSWithSelected', 'Edge')

    def align_wcs_with_selected_edge_center(self):
        self.invoke_method('AlignWCSWithSelected', 'EdgeCenter')

    def align_wcs_with_selected_rotation_edge(self):
        self.invoke_method('AlignWCSWithSelected', 'RotationEdge')

    def align_wcs_with_selected_face(self):
        self.invoke_method('AlignWCSWithSelected', 'Face')

    def rotate_wcs_around_u_deg(self, angle_deg: float):
        self.invoke_method('RotateWCS', 'u', angle_deg)

    def rotate_wcs_around_u_rad(self, angle_rad: float):
        self.rotate_wcs_around_u_deg(np.rad2deg(angle_rad))

    def rotate_wcs_around_v_deg(self, angle_deg: float):
        self.invoke_method('RotateWCS', 'v', angle_deg)

    def rotate_wcs_around_v_rad(self, angle_rad: float):
        self.rotate_wcs_around_v_deg(np.rad2deg(angle_rad))

    def rotate_wcs_around_w_deg(self, angle_deg: float):
        self.invoke_method('RotateWCS', 'w', angle_deg)

    def rotate_wcs_around_w_rad(self, angle_rad: float):
        self.rotate_wcs_around_w_deg(np.rad2deg(angle_rad))

    def move_local_wcs(self, du: float, dv: float, dw: float):
        self.invoke_method('MoveWCS', 'local', du, dv, dw)

    def move_global_wcs(self, du: float, dv: float, dw: float):
        self.invoke_method('MoveWCS', 'global', du, dv, dw)

    def align_wcs_with_global_coordinates(self):
        self.invoke_method('AlignWCSWithGlobalCoordinates')

    def set_workplane_size(self, size: float):
        self.invoke_method('SetWorkplaneSize', size)

    def set_workplane_raster(self, raster_size: float):
        self.invoke_method('SetWorkplaneRaster', raster_size)

    def set_workplane_snap(self, flag: bool = True):
        self.invoke_method('SetWorkplaneSnap', flag)

    def set_workplane_autoadjust(self, flag: bool = True):
        self.invoke_method('SetWorkplaneAutoadjust', flag)

    def set_workplane_snap_autoadjust(self, flag: bool = True):
        self.invoke_method('SetWorkplaneSnapAutoadjust', flag)

    def set_workplane_autosnap_factor(self, factor: float):
        self.invoke_method('SetWorkplaneAutosnapFactor', factor)

    def set_workplane_snap_raster(self, raster_size: float):
        self.invoke_method('SetWorkplaneSnapRaster', raster_size)

    def is_local_wcs_active(self) -> bool:
        return self.invoke_method('IsWCSActive') == 'local'

    def is_global_wcs_active(self) -> bool:
        return self.invoke_method('IsWCSActive') == 'global'

    def does_exist(self, wcs_name: str):
        return self.invoke_method('DoesExist', wcs_name)

    def get_origin(self, wcs_name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        self.invoke_method('GetOrigin', wcs_name, x, y, z)
        return (x.value, y.value, z.value)

    def get_normal(self, wcs_name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        self.invoke_method('GetNormal', wcs_name, x, y, z)
        return (x.value, y.value, z.value)

    def get_u_vector(self, wcs_name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        self.invoke_method('GetUVector', wcs_name, x, y, z)
        return (x.value, y.value, z.value)

    def get_affine_matrix_uvw_to_xyz(self, wcs_name: str):
        ux = w32com.create_ref_double()
        uy = w32com.create_ref_double()
        uz = w32com.create_ref_double()
        vx = w32com.create_ref_double()
        vy = w32com.create_ref_double()
        vz = w32com.create_ref_double()
        wx = w32com.create_ref_double()
        wy = w32com.create_ref_double()
        wz = w32com.create_ref_double()
        success = self.invoke_method(
            'GetAffineMatrixUVW2XYZ', wcs_name, ux, uy, uz, vx, vy, vz, wx, wy, wz)
        return (ux, uy, uz, vx, vy, vz, wx, wy, wz) if success else None

    def get_affine_matrix_xyz_to_uvw(self, wcs_name: str):
        ux = w32com.create_ref_double()
        uy = w32com.create_ref_double()
        uz = w32com.create_ref_double()
        vx = w32com.create_ref_double()
        vy = w32com.create_ref_double()
        vz = w32com.create_ref_double()
        wx = w32com.create_ref_double()
        wy = w32com.create_ref_double()
        wz = w32com.create_ref_double()
        success = self.invoke_method(
            'GetAffineMatrixXYZ2UVW', wcs_name, ux, uy, uz, vx, vy, vz, wx, wy, wz)
        return (ux, uy, uz, vx, vy, vz, wx, wy, wz) if success else None

    def get_wcs_point_from_global(self, wcs_name: str, x: float, y: float, z: float):
        u = w32com.create_ref_double()
        v = w32com.create_ref_double()
        w = w32com.create_ref_double()
        success = self.invoke_method('GetWCSPointFromGlobal', wcs_name, u, v, w, x, y, z)
        return (u.value, v.value, w.value) if success else None

    def get_global_point_from_wcs(self, wcs_name: str, u: float, v: float, w: float):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        success = self.invoke_method('GetWCSPointFromGlobal', wcs_name, x, y, z, u, v, w)
        return (x.value, y.value, z.value) if success else None