from . import Project
from . import ComObjectWrapper

class TraceFromCurve(ComObjectWrapper):
    GAP_TYPE_ROUNDED = 0
    GAP_TYPE_EXTENDED = 1
    GAP_TYPE_NATURAL = 2

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.TraceFromCurve

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_component(self, component_name: str):
        self.invoke_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.invoke_method('Material', mat_name)

    def set_curve(self, curve_name: str):
        self.invoke_method('Curve', curve_name)

    def set_thickness(self, thickness: float):
        self.invoke_method('Thickness', thickness)

    def set_width(self, width: float):
        self.invoke_method('Width', width)

    def set_start_round(self, flag: bool = True):
        self.invoke_method('RoundStart', flag)

    def set_end_round(self, flag: bool = True):
        self.invoke_method('RoundEnd', flag)

    def set_gap_type(self, gap_type: int):
        self.invoke_method('GapType', gap_type)

    def create(self):
        #TODO: check if Create or CreateNew
        self.invoke_method('Create')