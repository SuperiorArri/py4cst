from . import IVBAProvider, VBAObjWrapper

class Component(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Component')

    def create(self, component_name: str):
        self.record_method('New', component_name)

    def delete(self, component_name: str):
        self.record_method('Delete', component_name)

    def delete_all_empty_components(self, component_name: str):
        self.record_method('DeleteAllEmptyComponents', component_name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def does_exist(self, component_name: str) -> bool:
        return self.query_method_bool('DoesExist', component_name)

    def get_next_free_name(self) -> str:
        return self.query_method_str('GetNextFreeName')

    def hide(self, component_name: str):
        self.record_method('HideComponent', component_name)

    def show(self, component_name: str):
        self.record_method('ShowComponent', component_name)

    def hide_selected(self):
        self.record_method('Hide')

    def show_selected(self):
        self.record_method('Show')

    def hide_unselected(self):
        self.record_method('HideUnselected')

    def show_unselected(self):
        self.record_method('ShowUnselected')

    def hide_all(self):
        self.record_method('HideAll')

    def show_all(self):
        self.record_method('ShowAll')

    def hide_all_ports(self):
        self.record_method('HideAllPorts')

    def show_all_ports(self):
        self.record_method('ShowAllPorts')

    def hide_all_field_sources(self):
        self.record_method('HideAllFieldSources')

    def show_all_field_sources(self):
        self.record_method('ShowAllFieldSources')

    def hide_all_lumped_elements(self):
        self.record_method('HideAllLumpedElements')

    def show_all_lumped_elements(self):
        self.record_method('ShowAllLumpedElements')

    def hide_all_wires(self):
        self.record_method('HideAllWires')

    def show_all_wires(self):
        self.record_method('ShowAllWires')

    def hide_all_dielectric(self):
        self.record_method('HideAllDielectric')

    def show_all_dielectric(self):
        self.record_method('ShowAllDielectric')

    def hide_all_metals(self):
        self.record_method('HideAllMetals')

    def show_all_metals(self):
        self.record_method('ShowAllMetals')