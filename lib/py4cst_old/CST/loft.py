from . import Project
from . import ComObjectWrapper

class Loft(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Loft

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_component(self, component_name: str):
        self.invoke_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.invoke_method('Material', mat_name)

    def set_tangency(self, tang: float):
        self.invoke_method('Tangency', tang)

    def create(self):
        #TODO: check if Create or CreateNew
        self.invoke_method('Create')
