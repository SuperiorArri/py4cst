from . import IVBAProvider, VBAObjWrapper

class AnalyticalCurve(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'AnalyticalCurve')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, analytical_curve_name: str):
        self.record_method('Name', analytical_curve_name)

    def set_curve(self, curve_name: str):
        self.record_method('Curve', curve_name)

    def set_law_x(self, law: str):
        self.record_method('LawX', law)

    def set_law_y(self, law: str):
        self.record_method('LawY', law)

    def set_law_z(self, law: str):
        self.record_method('LawZ', law)

    def set_parameter_range(self, min: float, max: float):
        self.record_method('ParameterRange', min, max)

    def create(self):
        self.record_method('Create')