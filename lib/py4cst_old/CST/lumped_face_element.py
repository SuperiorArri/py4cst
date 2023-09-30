from . import Project
from . import ComObjectWrapper

class LumpedFaceElement(ComObjectWrapper):
    TYPE_RLC_PARALLEL = 'rlcparallel'
    TYPE_RLC_SERIAL = 'rlcserial'
    TYPE_DIODE = 'diode'
    TYPE_SPICE_CIRCUIT = 'spicecircuit'
    TYPE_TOUCHSTONE = 'touchstone'
    TYPE_MULTIPIN_GROUP_ITEM = 'multipingroupitem'
    TYPE_MULTIPIN_GROUP_SPICE = 'multipingroupspice'
    TYPE_MULTIPIN_GROUP_TOUCHSTONE = 'multipingrouptouchstone'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.LumpedFaceElement

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def create(self):
        self.invoke_method('Create')

    def modify(self):
        self.invoke_method('Modify')

    def set_type(self, elem_type: str):
        self.invoke_method('Type', elem_type)

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_folder_name(self, folder_name: str):
        self.invoke_method('Folder', folder_name)

    def set_resistance(self, value: float):
        self.invoke_method('SetR', value)

    def set_inductance(self, value: float):
        self.invoke_method('SetL', value)

    def set_capacity(self, value: float):
        self.invoke_method('SetC', value)

    def set_blocking_conductivity(self, value: float):
        self.invoke_method('SetGs', value)

    def set_reverse_current(self, value: float):
        self.invoke_method('SetI0', value)

    def set_temperature_kelvin(self, value: float):
        self.invoke_method('SetT', value)

    def set_temperature_celsius(self, value: float):
        self.invoke_method('SetT', value-273.15)

    def set_temperature_fahrenheit(self, value: float):
        self.invoke_method('SetT', (value + 459.67)*(5/9))

    def set_point1(self, x: float, y: float, z: float):
        self.invoke_method('SetP1', False, x, y, z)

    def set_pick_as_point1(self):
        self.invoke_method('SetP1', True, 0, 0, 0)

    def set_point2(self, x: float, y: float, z: float):
        self.invoke_method('SetP2', False, x, y, z)

    def set_pick_as_point2(self):
        self.invoke_method('SetP2', True, 0, 0, 0)

    def set_circuit_file_name(self, file_name: str):
        self.invoke_method('CircuitFileName', file_name)

    def set_use_relative_path(self, flag: bool = True):
        self.invoke_method('UseRelativePath', flag)

    def set_circuit_id(self, id: int):
        self.invoke_method('CircuitId', id)

    def set_use_copy_only(self, flag: bool = True):
        self.invoke_method('UseCopyOnly', flag)

    def set_invert(self, flag: bool = True):
        self.invoke_method('SetInvert', flag)

    def set_monitor(self, flag: bool = True):
        self.invoke_method('SetMonitor', flag)

    def set_use_projection(self, flag: bool = True):
        self.invoke_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.invoke_method('ReverseProjection', flag)

    def set_port_name(self, port_name: str):
        self.invoke_method('PortName', port_name)

    def set_circuit_file_name(self, file_name: str):
        self.invoke_method('CircuitFileName', file_name)

    def set_use_relative_path(self, flag: bool = True):
        self.invoke_method('UseRelativePath', flag)

    def set_circuit_id(self, id: int):
        self.invoke_method('CircuitId', id)

    def set_use_copy_only(self, flag: bool = True):
        self.invoke_method('UseCopyOnly', flag)

    def set_invert(self, flag: bool = True):
        self.invoke_method('SetInvert', flag)

    def set_monitor(self, flag: bool = True):
        self.invoke_method('SetMonitor', flag)

    def set_use_projection(self, flag: bool = True):
        self.invoke_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.invoke_method('ReverseProjection', flag)

    def set_port_name(self, name: str):
        self.invoke_method('PortName', name)

    def set_delete_port(self, flag: bool = True):
        self.invoke_method('DeletePort', flag)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def delete(self, name: str):
        self.invoke_method('Delete', name)

    def create_folder(self, name: str):
        self.invoke_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.invoke_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.invoke_method('RenameFolder', old_name, new_name)