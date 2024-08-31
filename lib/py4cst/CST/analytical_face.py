from . import Shape, IVBAProvider

class AnalyticalFace(Shape):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'AnalyticalFace')

    def set_law_x(self, expr: str):
        self.cache_method('LawX', expr)

    def set_law_y(self, expr: str):
        self.cache_method('LawY', expr)

    def set_law_z(self, expr: str):
        self.cache_method('LawZ', expr)

    def set_param_range_u(self, u_min: float, u_max: float):
        self.cache_method('ParameterRangeU', u_min, u_max)

    def set_param_range_v(self, v_min: float, v_max: float):
        self.cache_method('ParameterRangeV', v_min, v_max)
