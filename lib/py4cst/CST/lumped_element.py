from . import Project
from . import ComObjectWrapper
from . import w32com
from typing import Optional

class LumpedElement(ComObjectWrapper):
    TYPE_RLC_PARALLEL = 'rlcparallel'
    TYPE_RLC_SERIAL = 'rlcserial'
    TYPE_DIODE = 'diode'
    TYPE_SPICE_CIRCUIT = 'spicecircuit'
    TYPE_TOUCHSTONE = 'touchstone'
    TYPE_MULTIPIN_GROUP_ITEM = 'multipingroupitem'
    TYPE_MULTIPIN_GROUP_SPICE = 'multipingroupspice'
    TYPE_MULTIPIN_GROUP_TOUCHSTONE = 'multipingrouptouchstone'

    def __init__(self, project) -> None:
        self.project: Project = project
        self.com_object = project.com_object.LumpedElement

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def create(self):
        self.invoke_method('Create')

    def create_multipin(self):
        self.invoke_method('CreateMultipin')

    def modify(self):
        self.invoke_method('Modify')

    def set_type(self, elem_type: str):
        self.invoke_method('SetType', elem_type)

    def set_name(self, name: str):
        self.invoke_method('SetName', name)

    def set_folder_name(self, folder_name: str):
        self.invoke_method('Folder', folder_name)

    def set_resistance(self, value: float):
        self.invoke_method('SetR', value)

    def set_inductance(self, value: float):
        self.invoke_method('SetL', value)

    def set_capacitance(self, value: float):
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

    def get_coordinates(self, name: str):
        x0 = w32com.create_ref_double()
        y0 = w32com.create_ref_double()
        z0 = w32com.create_ref_double()
        x1 = w32com.create_ref_double()
        y1 = w32com.create_ref_double()
        z1 = w32com.create_ref_double()
        success = self.invoke_method('GetCoordinates', name, x0, y0, z0, x1, y1, z1)
        return (x0.value, y0.value, z0.value, x1.value, y1.value, z1.value) if success else None

    def get_properties(self, name: str):
        elem_type = w32com.create_ref_str()
        resistance = w32com.create_ref_double()
        inductance = w32com.create_ref_double()
        capacity = w32com.create_ref_double()
        blocking_conductivity = w32com.create_ref_double()
        reverse_current = w32com.create_ref_double()
        temperature = w32com.create_ref_double()
        radius = w32com.create_ref_double()
        success = self.invoke_method(
            'GetProperties', name, elem_type, resistance, inductance, capacity,
            blocking_conductivity, reverse_current, temperature, radius)
        return (
            elem_type.value, resistance.value, inductance.value, capacity.value,
            blocking_conductivity.value, reverse_current.value, temperature.value,
            radius.value) if success else None

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

    def set_radius(self, radius: float):
        self.invoke_method('SetRadius', radius)

    def set_wire(self, wire: str):
        self.invoke_method('Wire', wire)

    def set_wire_end_to_end1(self):
        self.invoke_method('Position', 'end1')

    def set_wire_end_to_end2(self):
        self.invoke_method('Position', 'end2')

    def set_port_name(self, name: str):
        self.invoke_method('PortName', name)

    def start_name_iteration(self):
        self.invoke_method('StartLumpedElementNameIteration')

    def connect_multipin_element_pin_to_sub_element(
            self, multipin_name: str, circuit_pin_name: str, multipin_sub_element_name: str):
        self.invoke_method(
            'ConnectMultipinElementPinToSubElement', multipin_name, circuit_pin_name,
            multipin_sub_element_name)

    def connect_multipin_element_pin_to_short(self, multipin_name: str, circuit_pin_name: str):
        self.invoke_method('ConnectMultipinElementPinToShort', multipin_name, circuit_pin_name)

    def connect_multipin_element_pin_to_open(self, multipin_name: str, circuit_pin_name: str):
        self.invoke_method('ConnectMultipinElementPinToOpen', multipin_name, circuit_pin_name)

    def get_next_lumped_element_name(self) -> Optional[str]:
        name = w32com.create_ref_str()
        success = self.invoke_method('GetNextLumpedElementName', name)
        return name.value if success else None

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