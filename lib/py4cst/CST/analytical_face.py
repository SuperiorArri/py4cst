from . import Project
from . import Shape

class AnalyticalFace(Shape):
    def __init__(self, project: Project) -> None:
        super().__init__(project, project.com_object.AnalyticalFace)

    def set_law_x(self, expr: str):
        self.invoke_method('LawX', expr)

    def set_law_y(self, expr: str):
        self.invoke_method('LawY', expr)

    def set_law_z(self, expr: str):
        self.invoke_method('LawZ', expr)

    def set_param_range_u(self, u_min: float, u_max: float):
        self.invoke_method('ParameterRangeU', u_min, u_max)

    def set_param_range_v(self, v_min: float, v_max: float):
        self.invoke_method('ParameterRangeV', v_min, v_max)
