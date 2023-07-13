from . import Project
from . import ComObjectWrapper
from . import w32com

class DiscreteFacePort(ComObjectWrapper):
    TYPE_S_PARAMETER = 'Sparameter'
    TYPE_VOLTAGE = 'Voltage'
    TYPE_CURRENT = 'Current'

    FACE_TYPE_LINEAR = 'Linear'
    FACE_TYPE_CURVED = 'Curved'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.DiscreteFacePort

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def create(self):
        self.invoke_method('Create')

    def modify(self):
        self.invoke_method('Modify')

    def set_number(self, number: int):
        self.invoke_method('PortNumber', number)

    def set_label(self, label: str):
        self.invoke_method('Label', label)

    def set_type(self, port_type: str):
        self.invoke_method('Type', port_type)

    def set_impedance(self, impedance: float):
        self.invoke_method('Impedance', impedance)

    def set_voltage_amplitude(self, amplitude: float):
        self.invoke_method('VoltageAmplitude', amplitude)

    def set_voltage_port_impedance(self, impedance: float):
        self.invoke_method('VoltagePortImpedance', impedance)

    def set_current_amplitude(self, amplitude: float):
        self.invoke_method('CurrentAmplitude', amplitude)

    def set_current_port_admittance(self, admittance: float):
        self.invoke_method('CurrentPortAdmittance', admittance)

    def set_point1(self, x: float, y: float, z: float):
        self.invoke_method('SetP1', False, x, y, z)

    def set_pick_as_point1(self):
        self.invoke_method('SetP1', True, 0, 0, 0)

    def set_point2(self, x: float, y: float, z: float):
        self.invoke_method('SetP2', False, x, y, z)

    def set_pick_as_point2(self):
        self.invoke_method('SetP2', True, 0, 0, 0)

    def set_invert_direction(self, flag: bool = True):
        self.invoke_method('InvertDirection', flag)

    def set_local_coordinates(self, flag: bool = True):
        self.invoke_method('LocalCoordinates', flag)

    def set_center_edge(self, flag: bool = True):
        self.invoke_method('CenterEdge', flag)

    def set_use_projection(self, flag: bool = True):
        self.invoke_method('UseProjection', flag)

    def set_reverse_projection(self, flag: bool = True):
        self.invoke_method('ReverseProjection', flag)

    def set_lumped_element_name(self, name: str):
        self.invoke_method('LumpedElementName', name)

    def set_delete_lumped_element(self, flag: bool = True):
        self.invoke_method('DeleteLumpedElement', flag)

    def set_monitor(self, flag: bool = True):
        self.invoke_method('Monitor', flag)

    def set_allow_full_size(self, flag: bool = True):
        self.invoke_method('AllowFullSize', flag)

    def set_face_type(self, face_type: str):
        self.invoke_method('FaceType', face_type)

    def get_properties(self, port_number: int):
        port_type = w32com.create_ref_str()
        impedance = w32com.create_ref_double()
        current = w32com.create_ref_double()
        voltage = w32com.create_ref_double()
        voltage_port_impedance = w32com.create_ref_double()
        monitor = w32com.create_ref_bool()
        success = self.invoke_method(
            'GetProperties', port_number, port_type, impedance, current, voltage,
            voltage_port_impedance, monitor)
        return (
            port_type.value, impedance.value, current.value, voltage.value,
            voltage_port_impedance.value, monitor.value) if success else None

    def delete(self, port_number: int):
        self.project.get_port().delete(port_number)
