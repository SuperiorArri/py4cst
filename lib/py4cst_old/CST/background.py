from . import Project
from . import ComObjectWrapper

class Background(ComObjectWrapper):
    MATERIAL_NORMAL = 'normal'
    MATERIAL_PEC = 'pec'

    THERMAL_TYPE_NORMAL = 'normal'
    THERMAL_TYPE_PTC = 'ptc'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Background

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_type(self, material_type: str):
        self.invoke_method('Type', material_type)

    def set_permitivity(self, epsilon: float):
        self.invoke_method('Epsilon', epsilon)

    def set_permeability(self, mu: float):
        self.invoke_method('Mu', mu)

    def set_conductivity(self, sigma: float):
        self.invoke_method('ElConductivity', sigma)

    def set_space_x_min(self, value: float):
        self.invoke_method('XminSpace', value)

    def set_space_x_max(self, value: float):
        self.invoke_method('XmaxSpace', value)

    def set_space_x(self, min_value: float, max_value: float):
        self.set_space_x_min(min_value)
        self.set_space_x_max(max_value)

    def set_space_y_min(self, value: float):
        self.invoke_method('YminSpace', value)

    def set_space_y_max(self, value: float):
        self.invoke_method('YmaxSpace', value)

    def set_space_y(self, min_value: float, max_value: float):
        self.set_space_y_min(min_value)
        self.set_space_y_max(max_value)

    def set_space_z_min(self, value: float):
        self.invoke_method('ZminSpace', value)

    def set_space_z_max(self, value: float):
        self.invoke_method('ZmaxSpace', value)

    def set_space_z(self, min_value: float, max_value: float):
        self.set_space_z_min(min_value)
        self.set_space_z_max(max_value)

    def set_thermal_type(self, thermal_type: str):
        self.invoke_method('ThermalType', thermal_type)

    def set_thermal_conductivity(self, value: float):
        self.invoke_method('ThermalConductivity', value)

    def set_apply_in_all_directions(self, flag: bool = True):
        self.invoke_method('ApplyInAllDirections', flag)