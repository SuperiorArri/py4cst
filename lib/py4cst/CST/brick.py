from . import Shape, IVBAProvider

class Brick(Shape):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Brick')

    def set_x_range(self, x_min: float, x_max: float):
        self.record_method('Xrange', x_min, x_max)

    def set_y_range(self, y_min: float, y_max: float):
        self.record_method('Yrange', y_min, y_max)

    def set_z_range(self, z_min: float, z_max: float):
        self.record_method('Zrange', z_min, z_max)