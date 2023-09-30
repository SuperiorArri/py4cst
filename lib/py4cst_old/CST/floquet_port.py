from . import Project
from . import ComObjectWrapper
from . import w32com
import numpy as np

class FloquetPort(ComObjectWrapper):
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

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.FloquetPort

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def prepare_port(self, position: str):
        self.invoke_method('Port', position)

    def add_mode(self, mode_type: str, order_x: int, order_y_prime: int):
        self.invoke_method('AddMode', mode_type, order_x, order_y_prime)

    def set_use_circular_polarization(self, flag: bool = True):
        self.invoke_method('SetUseCircularPolarization', flag)

    def set_polarization_independent_of_phi_deg(self, alignment_angle: float):
        self.invoke_method('SetPolarizationIndependentOfScanAnglePhi', alignment_angle, True)

    def set_polarization_independent_of_phi_rad(self, alignment_angle: float):
        self.set_polarization_independent_of_phi_deg(np.rad2deg(alignment_angle))

    def set_polarization_dependent_of_phi(self):
        self.invoke_method('SetPolarizationIndependentOfScanAnglePhi', 0, False)

    def set_dialog_frequency(self, frequency: float):
        self.invoke_method('SetDialogFrequency', frequency)

    def set_dialog_media_factor(self, frequency: float):
        self.invoke_method('SetDialogMediaFactor', frequency)

    def set_dialog_theta_deg(self, angle: float):
        self.invoke_method('SetDialogTheta', angle)

    def set_dialog_theta_rad(self, angle: float):
        self.set_dialog_theta_deg(np.rad2deg(angle))

    def set_dialog_phi_deg(self, angle: float):
        self.invoke_method('SetDialogPhi', angle)

    def set_dialog_phi_rad(self, angle: float):
        self.set_dialog_phi_deg(np.rad2deg(angle))

    def set_dialog_max_order_x(self, order: int):
        self.invoke_method('SetDialogMaxOrderX', order)

    def set_dialog_max_order_y_prime(self, order: int):
        self.invoke_method('SetDialogMaxOrderYPrime', order)

    def set_customized_list(self, flag: bool = True):
        self.invoke_method('SetCustomizedListFlag', flag)

    def set_number_of_modes_considered(self, number: int):
        self.invoke_method('SetNumberOfModesConsidered', number)

    def set_sort_code(self, code: str):
        self.invoke_method('SetSortCode', code)

    def set_distance_to_reference_plane(self, distance: float):
        self.invoke_method('SetDistanceToReferencePlane', distance)

    def get_number_of_modes(self) -> int:
        return self.invoke_method('GetNumberOfModes')

    def reset_mode_iterator(self) -> bool:
        return self.invoke_method('FirstMode')

    def get_mode(self):
        mode_type = w32com.create_ref_str()
        order_x = w32com.create_ref_int()
        order_y_prime = w32com.create_ref_int()
        success = self.invoke_method('GetMode', mode_type, order_x, order_y_prime)
        return (mode_type.value, order_x.value, order_y_prime.value) if success else None

    def increment_mode_iterator(self) -> bool:
        return self.invoke_method('NextMode')

    def get_number_of_modes_considered(self) -> int:
        return self.invoke_method('GetNumberOfModesConsidered')

    def is_port_at_z_min(self) -> bool:
        return self.invoke_method('IsPortAtZmin')

    def is_port_at_z_max(self) -> bool:
        return self.invoke_method('IsPortAtZmax')

    def get_mode_name_by_number(self, number: int) -> str:
        name = w32com.create_ref_str()
        success = self.invoke_method('GetModeNameByNumber', name, number)
        return name.value if success else None

    def get_mode_name_by_number(self, name: str) -> int:
        number = w32com.create_ref_long()
        success = self.invoke_method('GetModeNumberByName', number, name)
        return number.value if success else None

    def set_force_legacy_phase_reference(self, flag: bool = True):
        self.invoke_method('ForceLegacyPhaseReference', flag)