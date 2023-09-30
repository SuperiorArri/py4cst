from . import Project
from . import ComObjectWrapper
from . import w32com

class DiscretePort(ComObjectWrapper):
    TYPE_S_PARAMETER = 'Sparameter'
    TYPE_VOLTAGE = 'Voltage'
    TYPE_CURRENT = 'Current'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.DiscretePort

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

    def set_voltage(self, voltage: float):
        self.invoke_method('Voltage', voltage)

    def set_voltage_port_impedance(self, impedance: float):
        self.invoke_method('VoltagePortImpedance', impedance)

    def set_current(self, current: float):
        self.invoke_method('Current', current)

    def set_current_port_admittance(self, admittance: float):
        self.invoke_method('CurrentPortAdmittance', admittance)

    def set_radius(self, radius: float):
        self.invoke_method('Radius', radius)

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

    def set_monitor(self, flag: bool = True):
        self.invoke_method('Monitor', flag)

    def set_wire(self, wire_name: str):
        self.invoke_method('Wire', wire_name)

    def set_wire_end_to_end1(self):
        self.invoke_method('Position', 'end1')

    def set_wire_end_to_end2(self):
        self.invoke_method('Position', 'end2')

    def set_lumped_element_name(self, name: str):
        self.invoke_method('LumpedElementName', name)

    def set_delete_lumped_element(self, flag: bool = True):
        self.invoke_method('DeleteLumpedElement', flag)

    def get_element_dir_index(self, port_number: int):
        dir = w32com.create_ref_long()
        index = w32com.create_ref_long()
        self.invoke_method('GetElementDirIndex', port_number, dir, index)
        return (dir.value, index.value)

    def get_element_second_index(self, port_number: int):
        index = w32com.create_ref_long()
        self.invoke_method('GetElement2ndIndex', port_number, index)
        return index.value

    def get_length(self, port_number: int) -> float:
        return self.invoke_method('GetLength', port_number)

    def get_grid_length(self, port_number: int) -> float:
        return self.invoke_method('GetGridLength', port_number)

    def get_coordinates(self, port_number: int):
        x0 = w32com.create_ref_double()
        y0 = w32com.create_ref_double()
        z0 = w32com.create_ref_double()
        x1 = w32com.create_ref_double()
        y1 = w32com.create_ref_double()
        z1 = w32com.create_ref_double()
        success = self.invoke_method('GetCoordinates', port_number, x0, y0, z0, x1, y1, z1)
        return (x0.value, y0.value, z0.value, x1.value, y1.value, z1.value) if success else None

    def get_properties(self, port_number: int):
        port_type = w32com.create_ref_str()
        impedance = w32com.create_ref_double()
        current = w32com.create_ref_double()
        voltage = w32com.create_ref_double()
        voltage_port_impedance = w32com.create_ref_double()
        radius = w32com.create_ref_double()
        monitor = w32com.create_ref_bool()
        success = self.invoke_method(
            'GetProperties', port_number, port_type, impedance, current, voltage,
            voltage_port_impedance, radius, monitor)
        return (
            port_type.value, impedance.value, current.value, voltage.value,
            voltage_port_impedance.value, radius.value, monitor.value) if success else None

    def delete(self, port_number: int):
        self.invoke_method('Delete', port_number)