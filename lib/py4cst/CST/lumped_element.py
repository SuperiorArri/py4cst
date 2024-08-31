from . import IVBAProvider, VBAObjWrapper, VBATypeName
from typing import Optional

class LumpedElement(VBAObjWrapper):
    TYPE_RLC_PARALLEL = 'rlcparallel'
    TYPE_RLC_SERIAL = 'rlcserial'
    TYPE_DIODE = 'diode'
    TYPE_SPICE_CIRCUIT = 'spicecircuit'
    TYPE_TOUCHSTONE = 'touchstone'
    TYPE_MULTIPIN_GROUP_ITEM = 'multipingroupitem'
    TYPE_MULTIPIN_GROUP_SPICE = 'multipingroupspice'
    TYPE_MULTIPIN_GROUP_TOUCHSTONE = 'multipingrouptouchstone'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'LumpedElement')

    def reset(self):
        self.cache_method('Reset')

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create LumpedElement')

    def create_multipin(self):
        self.cache_method('CreateMultipin')
        self.flush_cache('CreateMultipin LumpedElement')

    def modify(self):
        self.cache_method('Modify')
        self.flush_cache('Modify LumpedElement')

    def set_type(self, elem_type: str):
        self.cache_method('SetType', elem_type)

    def set_name(self, name: str):
        self.cache_method('SetName', name)

    def set_folder_name(self, folder_name: str):
        self.cache_method('Folder', folder_name)

    def set_resistance(self, value: float):
        self.cache_method('SetR', value)

    def set_inductance(self, value: float):
        self.cache_method('SetL', value)

    def set_capacitance(self, value: float):
        self.cache_method('SetC', value)

    def set_rlc(self, r: float, l: float, c: float):
        self.set_resistance(r)
        self.set_inductance(l)
        self.set_capacitance(c)

    def set_blocking_conductivity(self, value: float):
        self.cache_method('SetGs', value)

    def set_reverse_current(self, value: float):
        self.cache_method('SetI0', value)

    def set_temperature_kelvin(self, value: float):
        self.cache_method('SetT', value)

    def set_temperature_celsius(self, value: float):
        self.cache_method('SetT', value-273.15)

    def set_temperature_fahrenheit(self, value: float):
        self.cache_method('SetT', (value + 459.67)*(5/9))

    def set_point1(self, x: float, y: float, z: float):
        self.cache_method('SetP1', False, x, y, z)

    def set_pick_as_point1(self):
        self.cache_method('SetP1', True, 0, 0, 0)

    def set_point2(self, x: float, y: float, z: float):
        self.cache_method('SetP2', False, x, y, z)

    def set_pick_as_point2(self):
        self.cache_method('SetP2', True, 0, 0, 0)

    # returns: (x0, y0, z0, x1, y1, z1) or None
    def get_coordinates(self, name: str) \
            -> Optional[tuple[float, float, float, float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetCoordinates', B, name, D, D, D, D, D, D)
        return None if not res[0] else res[1:]

    # returns: (type, R, L, C, Gs, I0, T, Radius) or None
    def get_properties(self, name: str) \
            -> Optional[tuple[str, float, float, float, float, float, float, float]]:
        B, S, D = VBATypeName.Boolean, VBATypeName.String, VBATypeName.Double
        res = self.query_method_t('GetProperties', B, name, S, D, D, D, D, D, D, D)
        return None if not res[0] else res[1:]

    def set_circuit_file_name(self, file_name: str):
        self.cache_method('CircuitFileName', file_name)

    def set_use_relative_path(self, flag: bool = True):
        self.cache_method('UseRelativePath', flag)

    def set_circuit_id(self, id: int):
        self.cache_method('CircuitId', id)

    def set_use_copy_only(self, flag: bool = True):
        self.cache_method('UseCopyOnly', flag)

    def set_invert(self, flag: bool = True):
        self.cache_method('SetInvert', flag)

    def set_monitor(self, flag: bool = True):
        self.cache_method('SetMonitor', flag)

    def set_radius(self, radius: float):
        self.cache_method('SetRadius', radius)

    def set_wire(self, wire: str):
        self.cache_method('Wire', wire)

    def set_wire_end_to_end1(self):
        self.cache_method('Position', 'end1')

    def set_wire_end_to_end2(self):
        self.cache_method('Position', 'end2')

    def set_port_name(self, name: str):
        self.cache_method('PortName', name)

    def start_name_iteration(self):
        self.invoke_method('StartLumpedElementNameIteration')

    def connect_multipin_element_pin_to_sub_element(
            self, multipin_name: str, circuit_pin_name: str, multipin_sub_element_name: str):
        self.record_method(
            'ConnectMultipinElementPinToSubElement', multipin_name, circuit_pin_name,
            multipin_sub_element_name)

    def connect_multipin_element_pin_to_short(self, multipin_name: str, circuit_pin_name: str):
        self.record_method('ConnectMultipinElementPinToShort', multipin_name, circuit_pin_name)

    def connect_multipin_element_pin_to_open(self, multipin_name: str, circuit_pin_name: str):
        self.record_method('ConnectMultipinElementPinToOpen', multipin_name, circuit_pin_name)

    def get_next_lumped_element_name(self) -> Optional[str]:
        B, S = VBATypeName.Boolean, VBATypeName.String
        res = self.query_method_t('GetNextLumpedElementName', B, S)
        return None if not res[0] else res[1]

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