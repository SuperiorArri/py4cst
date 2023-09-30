from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np

class PlaneWave(VBAObjWrapper):
    POLARIZATION_LINEAR = 'Linear'
    POLARIZATION_CIRCULAR = 'Circular'
    POLARIZATION_ELLIPTICAL = 'Elliptical'

    CIRCULAR_DIRECTION_LEFT = 'Left'
    CIRCULAR_DIRECTION_RIGHT = 'Right'

    DIRECTION_X = 'x'
    DIRECTION_Y = 'y'
    DIRECTION_Z = 'z'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'PlaneWave')

    def reset(self):
        self.record_method('Reset')

    def store(self):
        self.record_method('Store')

    def delete(self):
        self.record_method('Delete')

    def set_normal_vector(self, x: float, y: float, z: float):
        self.record_method('Normal', x, y, z)

    def set_e_vector(self, x: float, y: float, z: float):
        self.record_method('EVector', x, y, z)

    def set_polarization(self, polarization_type: str):
        self.record_method('Polarization', polarization_type)

    def set_reference_frequency(self, frequency: float):
        self.record_method('ReferenceFrequency', frequency)

    def set_phase_difference_deg(self, angle: float):
        self.record_method('PhaseDifference', angle)

    def set_phase_difference_rad(self, angle: float):
        self.set_phase_difference_deg(np.rad2deg(angle))

    def set_circular_direction(self, direction: str):
        self.record_method('CircularDirection', direction)

    def set_axial_ratio(self, ratio: float):
        self.record_method('AxialRatio', ratio)

    def set_use_custom_decoupling_plane(self, flag: bool = True):
        self.record_method('SetUserDecouplingPlane', flag)

    def set_custom_decoupling_plane(self, direction: str, position: float):
        self.record_method('DecouplingPlane', direction, position)

    # returns: (x, y, z)
    def get_normal_vector(self) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetNormal', None, D, D, D)

    # returns: (x, y, z)
    def get_e_vector(self) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetEVector', None, D, D, D)

    def get_polarization_type(self) -> str:
        S = VBATypeName.String
        return self.query_method_t('GetPolarizationType', None, S)[0]

    def get_circular_direction(self) -> str:
        S = VBATypeName.String
        return self.query_method_t('GetCircularDirection', None, S)[0]

    def get_reference_frequency(self) -> float:
        D = VBATypeName.Double
        return self.query_method_t('GetReferenceFrequency', None, D)[0]

    def get_phase_difference_deg(self) -> float:
        D = VBATypeName.Double
        return self.query_method_t('GetPhaseDifference', None, D)[0]

    def get_phase_difference_rad(self) -> float:
        return np.deg2rad(self.get_phase_difference_deg())

    def get_axial_ratio(self) -> float:
        D = VBATypeName.Double
        return self.query_method_t('GetAxialRatio', None, D)[0]
