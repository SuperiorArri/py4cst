from . import IVBAProvider, VBAObjWrapper

class Loft(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Loft')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def set_component(self, component_name: str):
        self.record_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.record_method('Material', mat_name)

    def set_tangency(self, tang: float):
        self.record_method('Tangency', tang)

    def create(self):
        #TODO: check if Create or CreateNew
        self.record_method('Create')
