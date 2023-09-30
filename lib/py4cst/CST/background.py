from . import IVBAProvider, VBAObjWrapper

class Background(VBAObjWrapper):
    MATERIAL_NORMAL = 'normal'
    MATERIAL_PEC = 'pec'

    THERMAL_TYPE_NORMAL = 'normal'
    THERMAL_TYPE_PTC = 'ptc'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Background')

    def reset(self):
        self.record_method('Reset')

    def set_type(self, material_type: str):
        self.record_method('Type', material_type)

    def set_permitivity(self, epsilon: float):
        self.record_method('Epsilon', epsilon)

    def set_permeability(self, mu: float):
        self.record_method('Mu', mu)

    def set_conductivity(self, sigma: float):
        self.record_method('ElConductivity', sigma)

    def set_space_x_min(self, value: float):
        self.record_method('XminSpace', value)

    def set_space_x_max(self, value: float):
        self.record_method('XmaxSpace', value)

    def set_space_x(self, min_value: float, max_value: float):
        self.set_space_x_min(min_value)
        self.set_space_x_max(max_value)

    def set_space_y_min(self, value: float):
        self.record_method('YminSpace', value)

    def set_space_y_max(self, value: float):
        self.record_method('YmaxSpace', value)

    def set_space_y(self, min_value: float, max_value: float):
        self.set_space_y_min(min_value)
        self.set_space_y_max(max_value)

    def set_space_z_min(self, value: float):
        self.record_method('ZminSpace', value)

    def set_space_z_max(self, value: float):
        self.record_method('ZmaxSpace', value)

    def set_space_z(self, min_value: float, max_value: float):
        self.set_space_z_min(min_value)
        self.set_space_z_max(max_value)

    def set_thermal_type(self, thermal_type: str):
        self.record_method('ThermalType', thermal_type)

    def set_thermal_conductivity(self, value: float):
        self.record_method('ThermalConductivity', value)

    def set_apply_in_all_directions(self, flag: bool = True):
        self.record_method('ApplyInAllDirections', flag)