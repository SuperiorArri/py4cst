from . import FarfieldExporter
import numpy as np

class UVSphereFarfieldExporter(FarfieldExporter):
    DEFAULT_STEP_DEG: float = 5.0

    def __init__(self) -> None:
        super().__init__()
        self.set_polar_angle_step_deg(UVSphereFarfieldExporter.DEFAULT_STEP_DEG) # theta
        self.set_lateral_angle_step_deg(UVSphereFarfieldExporter.DEFAULT_STEP_DEG) # phi
        self.radius = 1.0

    def set_polar_angles_deg(self, angles_deg: np.array):
        self.polar_angles = angles_deg

    def set_polar_angles_rad(self, angles_rad: np.array):
        self.set_polar_angles_deg(np.rad2deg(angles_rad))

    def set_lateral_angles_deg(self, angles_deg: np.array):
        self.lateral_angles = angles_deg

    def set_lateral_angles_rad(self, angles_rad: np.array):
        self.set_lateral_angles_deg(np.rad2deg(angles_rad))

    def set_polar_angle_step_deg(self, step_deg: float):
        self.set_polar_angles_deg(np.arange(0, 180+step_deg, step_deg))

    def set_polar_angle_step_rad(self, step_rad: float):
        self.set_polar_angle_step_deg(np.rad2deg(step_rad))

    def set_lateral_angle_step_deg(self, step_deg: float):
        self.set_lateral_angles_deg(np.arange(0, 360+step_deg, step_deg))

    def set_lateral_angle_step_rad(self, step_rad: float):
        self.set_lateral_angle_step_deg(np.rad2deg(step_rad))

    def set_radius(self, radius: float):
        self.radius = radius

    def export_abs(self):
        values = super().export_abs()
        return values.reshape((len(self.polar_angles), len(self.lateral_angles)))

    def export_complex_theta(self):
        values = super().export_complex_theta()
        return values.reshape((len(self.polar_angles), len(self.lateral_angles)))

    def export_complex_phi(self):
        values = super().export_complex_phi()
        return values.reshape((len(self.polar_angles), len(self.lateral_angles)))

    def __generate_points(self):
        self.clear_points()
        for polar_angle in self.polar_angles:
            for lateral_angle in self.lateral_angles:
                self.add_point(polar_angle, lateral_angle, self.radius)