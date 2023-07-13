from . import Project
from . import ComObjectWrapper

class Component(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Component

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def create(self, component_name: str):
        self.invoke_method('New', component_name)

    def delete(self, component_name: str):
        self.invoke_method('Delete', component_name)

    def delete_all_empty_components(self, component_name: str):
        self.invoke_method('DeleteAllEmptyComponents', component_name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def does_exist(self, component_name: str) -> bool:
        return self.invoke_method('DoesExist', component_name)

    def get_next_free_name(self) -> str:
        return self.invoke_method('GetNextFreeName')

    def hide(self, component_name: str):
        self.invoke_method('HideComponent', component_name)

    def show(self, component_name: str):
        self.invoke_method('ShowComponent', component_name)

    def hide_selected(self):
        self.invoke_method('Hide')

    def show_selected(self):
        self.invoke_method('Show')

    def hide_unselected(self):
        self.invoke_method('HideUnselected')

    def show_unselected(self):
        self.invoke_method('ShowUnselected')

    def hide_all(self):
        self.invoke_method('HideAll')

    def show_all(self):
        self.invoke_method('ShowAll')

    def hide_all_ports(self):
        self.invoke_method('HideAllPorts')

    def show_all_ports(self):
        self.invoke_method('ShowAllPorts')

    def hide_all_field_sources(self):
        self.invoke_method('HideAllFieldSources')

    def show_all_field_sources(self):
        self.invoke_method('ShowAllFieldSources')

    def hide_all_lumped_elements(self):
        self.invoke_method('HideAllLumpedElements')

    def show_all_lumped_elements(self):
        self.invoke_method('ShowAllLumpedElements')

    def hide_all_wires(self):
        self.invoke_method('HideAllWires')

    def show_all_wires(self):
        self.invoke_method('ShowAllWires')

    def hide_all_dielectric(self):
        self.invoke_method('HideAllDielectric')

    def show_all_dielectric(self):
        self.invoke_method('ShowAllDielectric')

    def hide_all_metals(self):
        self.invoke_method('HideAllMetals')

    def show_all_metals(self):
        self.invoke_method('ShowAllMetals')