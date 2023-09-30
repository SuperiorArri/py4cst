from . import Project
from . import Shape

class Brick(Shape):
    def __init__(self, project: Project) -> None:
        super().__init__(project, project.com_object.Brick)

    def set_x_range(self, x_min: float, x_max: float):
        self.invoke_method('Xrange', x_min, x_max)

    def set_y_range(self, y_min: float, y_max: float):
        self.invoke_method('Yrange', y_min, y_max)

    def set_z_range(self, z_min: float, z_max: float):
        self.invoke_method('Zrange', z_min, z_max)