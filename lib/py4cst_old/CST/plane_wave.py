from . import Project
from . import ComObjectWrapper
from . import w32com
import numpy as np

class PlaneWave(ComObjectWrapper):
    POLARIZATION_LINEAR = 'Linear'
    POLARIZATION_CIRCULAR = 'Circular'
    POLARIZATION_ELLIPTICAL = 'Elliptical'

    CIRCULAR_DIRECTION_LEFT = 'Left'
    CIRCULAR_DIRECTION_RIGHT = 'Right'

    DIRECTION_X = 'x'
    DIRECTION_Y = 'y'
    DIRECTION_Z = 'z'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.PlaneWave

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def store(self):
        self.invoke_method('Store')

    def delete(self):
        self.invoke_method('Delete')

    def set_normal_vector(self, x: float, y: float, z: float):
        self.invoke_method('Normal', x, y, z)

    def set_e_vector(self, x: float, y: float, z: float):
        self.invoke_method('EVector', x, y, z)

    def set_polarization(self, polarization_type: str):
        self.invoke_method('Polarization', polarization_type)

    def set_reference_frequency(self, frequency: float):
        self.invoke_method('ReferenceFrequency', frequency)

    def set_phase_difference_deg(self, angle: float):
        self.invoke_method('PhaseDifference', angle)

    def set_phase_difference_rad(self, angle: float):
        self.set_phase_difference_deg(np.rad2deg(angle))

    def set_circular_direction(self, direction: str):
        self.invoke_method('CircularDirection', direction)

    def set_axial_ratio(self, ratio: float):
        self.invoke_method('AxialRatio', ratio)

    def set_use_custom_decoupling_plane(self, flag: bool = True):
        self.invoke_method('SetUserDecouplingPlane', flag)

    def set_custom_decoupling_plane(self, direction: str, position: float):
        self.invoke_method('DecouplingPlane', direction, position)

    def get_normal_vector(self) -> tuple[float, float, float]:
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        self.invoke_method('GetNormal', x, y, z)
        return (x.value, y.value, z.value)

    def get_e_vector(self) -> tuple[float, float, float]:
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        self.invoke_method('GetEVector', x, y, z)
        return (x.value, y.value, z.value)

    def get_polarization_type(self) -> str:
        polarization_type = w32com.create_ref_str()
        self.invoke_method('GetPolarizationType', polarization_type)
        return polarization_type.value

    def get_circular_direction(self) -> str:
        dir = w32com.create_ref_str()
        self.invoke_method('GetCircularDirection', dir)
        return dir.value

    def get_reference_frequency(self) -> float:
        frequency = w32com.create_ref_double()
        self.invoke_method('GetReferenceFrequency', frequency)
        return frequency.value

    def get_phase_difference_deg(self) -> float:
        angle = w32com.create_ref_double()
        self.invoke_method('GetPhaseDifference', angle)
        return angle.value

    def get_phase_difference_rad(self) -> float:
        return np.deg2rad(self.get_phase_difference_deg())

    def get_axial_ratio(self) -> float:
        ratio = w32com.create_ref_double()
        self.invoke_method('GetAxialRatio', ratio)
        return ratio.value
