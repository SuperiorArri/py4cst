from . import IVBAProvider, VBAObjWrapper, VBATypeName
from typing import Optional

class Anchorpoint(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Anchorpoint')

    def store(self, name: str):
        self.record_method('Store', name)

    def define(
            self, name: str,
            pos_x: float, pos_y: float, pos_z: float,
            normal_x: float, normal_y: float, normal_z: float,
            u_vector_x: float, u_vector_y: float, u_vector_z: float):
        self.record_method(
            'Define', name,
            pos_x, pos_y, pos_z,
            normal_x, normal_y, normal_z,
            u_vector_x, u_vector_y, u_vector_z)

    def restore(self, name: str):
        self.record_method('Restore', name)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def create_folder(self, name: str):
        self.record_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.record_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.record_method('RenameFolder', old_name, new_name)

    def does_exist(self, name: str) -> bool:
        return self.query_method_bool('DoesExist', name)

    # returns: (x, y, z)
    def get_origin(self, name: str) -> Optional[tuple[float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetOrigin', B, name, D, D, D)
        return None if not res[0] else res[1:]

    # returns: (x, y, z)
    def get_normal(self, name: str):
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetNormal', B, name, D, D, D)
        return None if not res[0] else res[1:]

    # returns: (x, y, z)
    def get_u_vector(self, name: str):
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetUVector', B, name, D, D, D)
        return None if not res[0] else res[1:]