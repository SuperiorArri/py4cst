from . import IVBAProvider, VBAObjWrapper
import numpy as np

class Arc(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Arc')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, arc_name: str):
        self.cache_method('Name', arc_name)

    def set_curve(self, curve_name: str):
        self.cache_method('Curve', curve_name)

    def set_orientation_clockwise(self):
        self.cache_method('Orientation', 'Clockwise')

    def set_orientation_counter_clockwise(self):
        self.cache_method('Orientation', 'CounterClockwise')

    def set_center_x(self, x: float):
        self.cache_method('Xcenter', x)

    def set_center_y(self, y: float):
        self.cache_method('Ycenter', y)

    def set_center(self, x: float, y: float):
        self.set_center_x(x)
        self.set_center_y(y)

    def set_start_point_x(self, x: float):
        self.cache_method('X1', x)

    def set_start_point_y(self, y: float):
        self.cache_method('Y1', y)

    def set_start_point(self, x: float, y: float):
        self.set_start_point_x(x)
        self.set_start_point_y(y)

    def set_end_point_x(self, x: float):
        self.cache_method('X2', x)

    def set_end_point_y(self, y: float):
        self.cache_method('Y2', y)

    def set_end_point(self, x: float, y: float):
        self.set_end_point_x(x)
        self.set_end_point_y(y)

    def set_angle_deg(self, angle_deg: float) -> int:
        self.cache_method('Angle', angle_deg)

    def set_angle_rad(self, angle_rad: float) -> int:
        self.set_angle_deg(np.rad2deg(angle_rad))

    def set_use_angle(self, flag: bool = True):
        self.cache_method('UseAngle', flag)

    def set_number_of_segments(self, num: int):
        self.cache_method('Segments', num)

    def set_infinite_number_of_segments(self):
        self.cache_method('Segments', 0)

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create Arc')