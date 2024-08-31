from . import IVBAProvider, VBAObjWrapper

class Shape(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider, shape_name: str) -> None:
        super().__init__(vbap, shape_name)
        self.shape_name = shape_name

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def set_component(self, component_name: str):
        self.cache_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.cache_method('Material', mat_name)

    def create(self):
        self.cache_method('Create')
        self.flush_cache(f'Create {self.shape_name}')