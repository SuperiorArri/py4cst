from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np
from typing import Optional

class FloquetPort(VBAObjWrapper):
    POSITION_Z_MIN = 'zmin'
    POSITION_Z_MAX = 'zmax'

    MODE_TYPE_TE = 'TE'
    MODE_TYPE_TM = 'TM'
    MODE_TYPE_LCP = 'LCP'
    MODE_TYPE_RCP = 'RCP'

    CODE_PLUS_BETA_PW = '+beta/pw'
    CODE_PLUS_BETA = '+beta'
    CODE_MINUS_BETA = '-beta'
    CODE_PLUS_ALPHA = '+alpha'
    CODE_MINUS_ALPHA = '-alpha'
    CODE_PLUS_TE = '+te'
    CODE_MINUS_TE = '-te'
    CODE_PLUS_TM = '+tm'
    CODE_MINUS_TM = '-tm'
    CODE_PLUS_ORDER_X = '+orderx'
    CODE_MINUS_ORDER_X = '-orderx'
    CODE_PLUS_ORDER_Y = '+ordery'
    CODE_MINUS_ORDER_Y = '-ordery'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'FloquetPort')

    def reset(self):
        self.record_method('Reset')

    def prepare_port(self, position: str):
        self.record_method('Port', position)

    def add_mode(self, mode_type: str, order_x: int, order_y_prime: int):
        self.record_method('AddMode', mode_type, order_x, order_y_prime)

    def set_use_circular_polarization(self, flag: bool = True):
        self.record_method('SetUseCircularPolarization', flag)

    def set_polarization_independent_of_phi_deg(self, alignment_angle: float):
        self.record_method('SetPolarizationIndependentOfScanAnglePhi', alignment_angle, True)

    def set_polarization_independent_of_phi_rad(self, alignment_angle: float):
        self.set_polarization_independent_of_phi_deg(np.rad2deg(alignment_angle))

    def set_polarization_dependent_of_phi(self):
        self.record_method('SetPolarizationIndependentOfScanAnglePhi', 0, False)

    def set_dialog_frequency(self, frequency: float):
        self.record_method('SetDialogFrequency', frequency)

    def set_dialog_media_factor(self, frequency: float):
        self.record_method('SetDialogMediaFactor', frequency)

    def set_dialog_theta_deg(self, angle: float):
        self.record_method('SetDialogTheta', angle)

    def set_dialog_theta_rad(self, angle: float):
        self.set_dialog_theta_deg(np.rad2deg(angle))

    def set_dialog_phi_deg(self, angle: float):
        self.record_method('SetDialogPhi', angle)

    def set_dialog_phi_rad(self, angle: float):
        self.set_dialog_phi_deg(np.rad2deg(angle))

    def set_dialog_max_order_x(self, order: int):
        self.record_method('SetDialogMaxOrderX', order)

    def set_dialog_max_order_y_prime(self, order: int):
        self.record_method('SetDialogMaxOrderYPrime', order)

    def set_customized_list(self, flag: bool = True):
        self.record_method('SetCustomizedListFlag', flag)

    def set_number_of_modes_considered(self, number: int):
        self.record_method('SetNumberOfModesConsidered', number)

    def set_sort_code(self, code: str):
        self.record_method('SetSortCode', code)

    def set_distance_to_reference_plane(self, distance: float):
        self.record_method('SetDistanceToReferencePlane', distance)

    def get_number_of_modes(self) -> int:
        return self.query_method_int('GetNumberOfModes')

    def reset_mode_iterator(self) -> bool:
        return self.query_method_bool('FirstMode')

    # returns: (mode_type, order_x, order_y_prime) or None
    def get_mode(self) -> Optional[tuple[str, int, int]]:
        S, I = VBATypeName.String, VBATypeName.Integer
        res = self.query_method_t('GetMode', VBATypeName.Boolean, S, I, I)
        return None if not res[0] else res[1:]

    def increment_mode_iterator(self) -> bool:
        return self.query_method_bool('NextMode')

    def get_number_of_modes_considered(self) -> int:
        return self.query_method_int('GetNumberOfModesConsidered')

    def is_port_at_z_min(self) -> bool:
        return self.query_method_bool('IsPortAtZmin')

    def is_port_at_z_max(self) -> bool:
        return self.query_method_bool('IsPortAtZmax')

    def get_mode_name_by_number(self, number: int) -> Optional[str]:
        S = VBATypeName.String
        res = self.query_method_t('GetModeNameByNumber', VBATypeName.Boolean, S, number)
        return None if not res[0] else res[1]

    def get_mode_name_by_number(self, name: str) -> int:
        L = VBATypeName.Long
        res = self.query_method_t('GetModeNameByNumber', VBATypeName.Boolean, L, name)
        return None if not res[0] else res[1]

    def set_force_legacy_phase_reference(self, flag: bool = True):
        self.record_method('ForceLegacyPhaseReference', flag)