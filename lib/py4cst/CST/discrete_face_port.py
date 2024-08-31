from . import IVBAProvider, VBAObjWrapper, VBATypeName, Port
from typing import Optional

class DiscreteFacePort(VBAObjWrapper):
    TYPE_S_PARAMETER = 'Sparameter'
    TYPE_VOLTAGE = 'Voltage'
    TYPE_CURRENT = 'Current'

    FACE_TYPE_LINEAR = 'Linear'
    FACE_TYPE_CURVED = 'Curved'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'DiscreteFacePort')

    def reset(self):
        self.cache_method('Reset')

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create DiscreteFacePort')

    def modify(self):
        self.cache_method('Modify')
        self.flush_cache('Modify DiscreteFacePort')

    def set_number(self, number: int):
        self.cache_method('PortNumber', number)

    def set_label(self, label: str):
        self.cache_method('Label', label)

    def set_type(self, port_type: str):
        self.cache_method('Type', port_type)

    def set_impedance(self, impedance: float):
        self.cache_method('Impedance', impedance)

    def set_voltage_amplitude(self, amplitude: float):
        self.cache_method('VoltageAmplitude', amplitude)

    def set_voltage_port_impedance(self, impedance: float):
        self.cache_method('VoltagePortImpedance', impedance)

    def set_current_amplitude(self, amplitude: float):
        self.cache_method('CurrentAmplitude', amplitude)

    def set_current_port_admittance(self, admittance: float):
        self.cache_method('CurrentPortAdmittance', admittance)

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

    def set_center_edge(self, flag: bool = True):
        self.cache_method('CenterEdge', flag)

    def set_use_projection(self, flag: bool = True):
        self.cache_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.cache_method('ReverseProjection', flag)

    def set_lumped_element_name(self, name: str):
        self.cache_method('LumpedElementName', name)

    def set_delete_lumped_element(self, flag: bool = True):
        self.cache_method('DeleteLumpedElement', flag)

    def set_monitor(self, flag: bool = True):
        self.cache_method('Monitor', flag)

    def set_allow_full_size(self, flag: bool = True):
        self.cache_method('AllowFullSize', flag)

    def set_face_type(self, face_type: str):
        self.cache_method('FaceType', face_type)

    # returns: (type, impedance, current, voltage, voltage_port_impedance, monitor) or None
    def get_properties(self, port_number: int) \
            -> Optional[tuple[str, float, float, float, float, bool]]:
        S, D, B = VBATypeName.String, VBATypeName.Double, VBATypeName.Boolean
        res = self.query_method_t('GetProperties', B, port_number, S, D, D, D, D, B)
        return None if not res[0] else res[1:]

    def delete(self, port_number: int):
        Port(self.vbap).delete(port_number)
