from . import IVBAProvider, VBAObjWrapper

class Shape(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider, shape_name: str) -> None:
        super().__init__(vbap, shape_name)

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def set_component(self, component_name: str):
        self.record_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.record_method('Material', mat_name)

    def create(self):
        self.record_method('Create')