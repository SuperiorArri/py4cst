from . import IVBAProvider, VBAObjWrapper

class Loft(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Loft')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def set_component(self, component_name: str):
        self.cache_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.cache_method('Material', mat_name)

    def set_tangency(self, tang: float):
        self.cache_method('Tangency', tang)

    def create(self):
        self.cache_method('CreateNew')
        self.flush_cache('Create Loft')
