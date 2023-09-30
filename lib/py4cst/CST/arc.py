from . import IVBAProvider, VBAObjWrapper

class Arc(VBAObjWrapper):
    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Arc')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, arc_name: str):
        self.record_method('Name', arc_name)

    def set_curve(self, curve_name: str):
        self.record_method('Curve', curve_name)

    def set_orientation_clockwise(self):
        self.record_method('Orientation', 'Clockwise')

    def set_orientation_counter_clockwise(self):
        self.record_method('Orientation', 'CounterClockwise')

    def set_center_x(self, x: float):
        self.record_method('Xcenter', x)

    def set_center_y(self, y: float):
        self.record_method('Ycenter', y)

    def set_center(self, x: float, y: float):
        self.set_center_x(x)
        self.set_center_y(y)

    def set_start_point_x(self, x: float):
        self.record_method('X1', x)

    def set_start_point_y(self, y: float):
        self.record_method('Y1', y)

    def set_start_point_x(self, x: float, y: float):
        self.set_start_point_x(x)
        self.set_start_point_y(y)