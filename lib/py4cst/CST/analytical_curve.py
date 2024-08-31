from . import IVBAProvider, VBAObjWrapper

class AnalyticalCurve(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'AnalyticalCurve')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, analytical_curve_name: str):
        self.cache_method('Name', analytical_curve_name)

    def set_curve(self, curve_name: str):
        self.cache_method('Curve', curve_name)

    def set_law_x(self, law: str):
        self.cache_method('LawX', law)

    def set_law_y(self, law: str):
        self.cache_method('LawY', law)

    def set_law_z(self, law: str):
        self.cache_method('LawZ', law)

    def set_parameter_range(self, min: float, max: float):
        self.cache_method('ParameterRange', min, max)

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create AnalyticalCurve')