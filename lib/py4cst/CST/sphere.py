from . import Shape, IVBAProvider

class Sphere(Shape):
    AXIS_X = 'x'
    AXIS_Y = 'y'
    AXIS_Z = 'z'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Sphere')

    def set_axis(self, axis: str):
        self.cache_method('Axis', axis)

    def set_center_radius(self, radius: float):
        self.cache_method('CenterRadius', radius)

    def set_top_radius(self, radius: float):
        self.cache_method('TopRadius', radius)

    def set_bottom_radius(self, radius: float):
        self.cache_method('BottomRadius', radius)

    def set_center(self, x: float, y: float, z: float):
        self.cache_method('Center', x, y, z)

    def set_num_segments(self, num_segments: int):
        self.cache_method('Segments', num_segments)

    def set_smooth_geometry(self):
        self.set_num_segments(0)