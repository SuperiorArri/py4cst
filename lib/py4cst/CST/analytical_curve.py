from . import Project
from . import ComObjectWrapper

class AnalyticalCurve(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.AnalyticalCurve

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, analytical_curve_name: str):
        self.invoke_method('Name', analytical_curve_name)

    def set_curve(self, curve_name: str):
        self.invoke_method('Curve', curve_name)

    def set_law_x(self, law: str):
        self.invoke_method('LawX', law)

    def set_law_y(self, law: str):
        self.invoke_method('LawY', law)

    def set_law_z(self, law: str):
        self.invoke_method('LawZ', law)

    def set_parameter_range(self, min: float, max: float):
        self.invoke_method('ParameterRange', min, max)

    def create(self):
        self.invoke_method('Create')