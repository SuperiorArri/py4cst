from . import Project
from . import Shape

class Sphere(Shape):
    AXIS_X = 'x'
    AXIS_Y = 'y'
    AXIS_Z = 'z'

    def __init__(self, project: Project) -> None:
        super().__init__(project, project.com_object.Sphere)

    def set_axis(self, axis: str):
        self.invoke_method('Axis', axis)

    def set_center_radius(self, radius: float):
        self.invoke_method('CenterRadius', radius)

    def set_top_radius(self, radius: float):
        self.invoke_method('TopRadius', radius)

    def set_bottom_radius(self, radius: float):
        self.invoke_method('BottomRadius', radius)

    def set_center(self, x: float, y: float, z: float):
        self.invoke_method('Center', x, y, z)

    def set_num_segments(self, num_segments: int):
        self.invoke_method('Segments', num_segments)

    def set_smooth_geometry(self):
        self.set_num_segments(0)