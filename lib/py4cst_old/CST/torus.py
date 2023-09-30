from . import Project
from . import Shape

class Torus(Shape):
    AXIS_X = 'x'
    AXIS_Y = 'y'
    AXIS_Z = 'z'

    def __init__(self, project: Project) -> None:
        super().__init__(project, project.com_object.Torus)

    def set_axis(self, axis: str):
        self.invoke_method('Axis', axis)

    def set_outer_radius(self, radius: float):
        self.invoke_method('Outerradius', radius)

    def set_inner_radius(self, radius: float):
        self.invoke_method('Innerradius', radius)

    def set_x_center(self, center: float):
        self.invoke_method('Xcenter', center)

    def set_y_center(self, center: float):
        self.invoke_method('Ycenter', center)

    def set_z_center(self, center: float):
        self.invoke_method('Zcenter', center)

    def set_num_segments(self, num_segments: int):
        self.invoke_method('Segments', num_segments)

    def set_smooth_geometry(self):
        self.set_num_segments(0)