from . import Project
from . import ComObjectWrapper

class Arc(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Arc

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, arc_name: str):
        self.invoke_method('Name', arc_name)

    def set_curve(self, curve_name: str):
        self.invoke_method('Curve', curve_name)

    def set_orientation_clockwise(self):
        self.invoke_method('Orientation', 'Clockwise')

    def set_orientation_counter_clockwise(self):
        self.invoke_method('Orientation', 'CounterClockwise')

    def set_center_x(self, x: float):
        self.invoke_method('Xcenter', x)

    def set_center_y(self, y: float):
        self.invoke_method('Ycenter', y)

    def set_center(self, x: float, y: float):
        self.set_center_x(x)
        self.set_center_y(y)

    def set_start_point_x(self, x: float):
        self.invoke_method('X1', x)

    def set_start_point_y(self, y: float):
        self.invoke_method('Y1', y)

    def set_start_point_x(self, x: float, y: float):
        self.set_start_point_x(x)
        self.set_start_point_y(y)