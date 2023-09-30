from . import Project
from . import ComObjectWrapper

class Shape(ComObjectWrapper):
    def __init__(self, project: Project, com_object) -> None:
        self.project = project
        self.com_object = com_object

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

    def create(self):
        self.invoke_method('Create')