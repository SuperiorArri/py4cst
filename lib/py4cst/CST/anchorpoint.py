from . import Project
from . import ComObjectWrapper
from . import w32com

class Anchorpoint(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Anchorpoint

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def store(self, name: str):
        self.invoke_method('Store', name)

    def define(
            self, name: str,
            pos_x: float, pos_y: float, pos_z: float,
            normal_x: float, normal_y: float, normal_z: float,
            u_vector_x: float, u_vector_y: float, u_vector_z: float):
        self.invoke_method(
            'Define', name,
            pos_x, pos_y, pos_z,
            normal_x, normal_y, normal_z,
            u_vector_x, u_vector_y, u_vector_z)

    def restore(self, name: str):
        self.invoke_method('Restore', name)

    def delete(self, name: str):
        self.invoke_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def create_folder(self, name: str):
        self.invoke_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.invoke_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.invoke_method('RenameFolder', old_name, new_name)

    def does_exist(self, name: str) -> bool:
        return self.invoke_method('DoesExist', name)

    def get_origin(self, name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        success = self.invoke_method('GetOrigin', name, x, y, z)
        return (x.value, y.value, z.value) if success else None

    def get_normal(self, name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        success = self.invoke_method('GetNormal', name, x, y, z)
        return (x.value, y.value, z.value) if success else None

    def get_u_vector(self, name: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        success = self.invoke_method('GetUVector', name, x, y, z)
        return (x.value, y.value, z.value) if success else None