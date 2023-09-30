from . import IVBAProvider, VBAObjWrapper

class LumpedFaceElement(VBAObjWrapper):
    TYPE_RLC_PARALLEL = 'rlcparallel'
    TYPE_RLC_SERIAL = 'rlcserial'
    TYPE_DIODE = 'diode'
    TYPE_SPICE_CIRCUIT = 'spicecircuit'
    TYPE_TOUCHSTONE = 'touchstone'
    TYPE_MULTIPIN_GROUP_ITEM = 'multipingroupitem'
    TYPE_MULTIPIN_GROUP_SPICE = 'multipingroupspice'
    TYPE_MULTIPIN_GROUP_TOUCHSTONE = 'multipingrouptouchstone'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'LumpedFaceElement')

    def reset(self):
        self.record_method('Reset')

    def create(self):
        self.record_method('Create')

    def modify(self):
        self.record_method('Modify')

    def set_type(self, elem_type: str):
        self.record_method('Type', elem_type)

    def set_name(self, name: str):
        self.record_method('Name', name)

    def set_folder_name(self, folder_name: str):
        self.record_method('Folder', folder_name)

    def set_resistance(self, value: float):
        self.record_method('SetR', value)

    def set_inductance(self, value: float):
        self.record_method('SetL', value)

    def set_capacity(self, value: float):
        self.record_method('SetC', value)

    def set_blocking_conductivity(self, value: float):
        self.record_method('SetGs', value)

    def set_reverse_current(self, value: float):
        self.record_method('SetI0', value)

    def set_temperature_kelvin(self, value: float):
        self.record_method('SetT', value)

    def set_temperature_celsius(self, value: float):
        self.record_method('SetT', value-273.15)

    def set_temperature_fahrenheit(self, value: float):
        self.record_method('SetT', (value + 459.67)*(5/9))

    def set_point1(self, x: float, y: float, z: float):
        self.record_method('SetP1', False, x, y, z)

    def set_pick_as_point1(self):
        self.record_method('SetP1', True, 0, 0, 0)

    def set_point2(self, x: float, y: float, z: float):
        self.record_method('SetP2', False, x, y, z)

    def set_pick_as_point2(self):
        self.record_method('SetP2', True, 0, 0, 0)

    def set_circuit_file_name(self, file_name: str):
        self.record_method('CircuitFileName', file_name)

    def set_use_relative_path(self, flag: bool = True):
        self.record_method('UseRelativePath', flag)

    def set_circuit_id(self, id: int):
        self.record_method('CircuitId', id)

    def set_use_copy_only(self, flag: bool = True):
        self.record_method('UseCopyOnly', flag)

    def set_invert(self, flag: bool = True):
        self.record_method('SetInvert', flag)

    def set_monitor(self, flag: bool = True):
        self.record_method('SetMonitor', flag)

    def set_use_projection(self, flag: bool = True):
        self.record_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.record_method('ReverseProjection', flag)

    def set_port_name(self, port_name: str):
        self.record_method('PortName', port_name)

    def set_circuit_file_name(self, file_name: str):
        self.record_method('CircuitFileName', file_name)

    def set_use_relative_path(self, flag: bool = True):
        self.record_method('UseRelativePath', flag)

    def set_circuit_id(self, id: int):
        self.record_method('CircuitId', id)

    def set_use_copy_only(self, flag: bool = True):
        self.record_method('UseCopyOnly', flag)

    def set_invert(self, flag: bool = True):
        self.record_method('SetInvert', flag)

    def set_monitor(self, flag: bool = True):
        self.record_method('SetMonitor', flag)

    def set_use_projection(self, flag: bool = True):
        self.record_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.record_method('ReverseProjection', flag)

    def set_port_name(self, name: str):
        self.record_method('PortName', name)

    def set_delete_port(self, flag: bool = True):
        self.record_method('DeletePort', flag)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def create_folder(self, name: str):
        self.record_method('NewFolder', name)

    def delete_folder(self, name: str):
        self.record_method('DeleteFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.record_method('RenameFolder', old_name, new_name)