from . import IVBAProvider, VBAObjWrapper

class MeshShapes(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'MeshShapes')

    def reset(self):
        self.record_method('Reset')

    def delete(self, mesh_shape_name: str):
        self.record_method('Delete', mesh_shape_name)

    def rename(self, old_mesh_shape_name: str, new_mesh_shape_name: str):
        self.record_method('Rename', old_mesh_shape_name, new_mesh_shape_name)

    def create_folder(self, name: str):
        self.record_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.record_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.record_method('RenameFolder', old_name, new_name)

    def change_material(self, mesh_shape_name: str, material_name: str):
        self.record_method('ChangeMaterial', mesh_shape_name, material_name)

    def add_name(self, element_name: str):
        self.record_method('AddName', element_name)

    def delete_multiple(self):
        self.record_method('DeleteMultiple')

    def set_tolerance(self, value: float):
        self.record_method('Tolerance', value)

    def resolve_intersections(self):
        self.record_method('ResolveIntersections')

    def set_mesh_element_size(self, value: float):
        self.record_method('MeshElementSize', value)

    def create_mesh_shapes_by_facetting(self):
        self.record_method('CreateMeshShapesByFacetting')

    def create_mesh_shapes_by_remeshing(self):
        self.record_method('CreateMeshShapesByRemeshing')