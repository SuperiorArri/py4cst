from . import IVBAProvider, VBAObjWrapper, VBATypeName
from typing import Optional

class DiscretePort(VBAObjWrapper):
    TYPE_S_PARAMETER = 'Sparameter'
    TYPE_VOLTAGE = 'Voltage'
    TYPE_CURRENT = 'Current'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'DiscretePort')

    def reset(self):
        self.cache_method('Reset')

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create DiscretePort')

    def modify(self):
        self.cache_method('Modify')
        self.flush_cache('Modify DiscretePort')

    def set_number(self, number: int):
        self.cache_method('PortNumber', number)

    def set_label(self, label: str):
        self.cache_method('Label', label)

    def set_type(self, port_type: str):
        self.cache_method('Type', port_type)

    def set_impedance(self, impedance: float):
        self.cache_method('Impedance', impedance)

    def set_voltage(self, voltage: float):
        self.cache_method('Voltage', voltage)

    def set_voltage_port_impedance(self, impedance: float):
        self.cache_method('VoltagePortImpedance', impedance)

    def set_current(self, current: float):
        self.cache_method('Current', current)

    def set_current_port_admittance(self, admittance: float):
        self.cache_method('CurrentPortAdmittance', admittance)

    def set_radius(self, radius: float):
        self.cache_method('Radius', radius)

    def set_point1(self, x: float, y: float, z: float):
        self.cache_method('SetP1', False, x, y, z)

    def set_pick_as_point1(self):
        self.cache_method('SetP1', True, 0, 0, 0)

    def set_point2(self, x: float, y: float, z: float):
        self.cache_method('SetP2', False, x, y, z)

    def set_pick_as_point2(self):
        self.cache_method('SetP2', True, 0, 0, 0)

    def set_invert_direction(self, flag: bool = True):
        self.cache_method('InvertDirection', flag)

    def set_local_coordinates(self, flag: bool = True):
        self.cache_method('LocalCoordinates', flag)

    def set_monitor(self, flag: bool = True):
        self.cache_method('Monitor', flag)

    def set_wire(self, wire_name: str):
        self.cache_method('Wire', wire_name)

    def set_wire_end_to_end1(self):
        self.cache_method('Position', 'end1')

    def set_wire_end_to_end2(self):
        self.cache_method('Position', 'end2')

    def set_lumped_element_name(self, name: str):
        self.cache_method('LumpedElementName', name)

    def set_delete_lumped_element(self, flag: bool = True):
        self.cache_method('DeleteLumpedElement', flag)

    # returns: (dir, index)
    def get_element_dir_index(self, port_number: int) -> tuple[int, int]:
        L = VBATypeName.Long
        return self.query_method_t('GetElementDirIndex', None, port_number, L, L)

    def get_element_second_index(self, port_number: int) -> int:
        L = VBATypeName.Long
        return self.query_method_t('GetElement2ndIndex', None, port_number, L)[0]

    def get_length(self, port_number: int) -> float:
        return self.query_method_float('GetLength', port_number)

    def get_grid_length(self, port_number: int) -> float:
        return self.query_method_float('GetGridLength', port_number)

    # returns: (x0, y0, z0, x1, y1, z1) or None
    def get_coordinates(self, port_number: int) \
            -> Optional[tuple[float, float, float, float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetCoordinates', B, port_number, D, D, D, D, D, D)
        return None if not res[0] else res[1:]

    # returns: (type, impedance, current, voltage, voltage_port_impedance, radius, monitor)
    def get_properties(self, port_number: int) \
            -> Optional[tuple[str, float, float, float, float, float, bool]]:
        S, D, B = VBATypeName.String, VBATypeName.Double, VBATypeName.Boolean
        res = self.query_method_t('GetProperties', B, port_number, S, D, D, D, D, D, B)
        return None if not res[0] else res[1:]

    def delete(self, port_number: int):
        self.record_method('Delete', port_number)