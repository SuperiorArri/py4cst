from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np

class Port(VBAObjWrapper):
    ORIENTATION_XMIN = 'xmin'
    ORIENTATION_XMAX = 'xmax'
    ORIENTATION_YMIN = 'ymin'
    ORIENTATION_YMAX = 'ymax'
    ORIENTATION_ZMIN = 'zmin'
    ORIENTATION_ZMAX = 'zmax'

    COORDINATES_FREE = 'Free'
    COORDINATES_FULL = 'Full'
    COORDINATES_PICKS = 'Picks'

    POTENTIAL_POSITIVE = 'Positive'
    POTENTIAL_NEGATIVE = 'Negative'

    BOUNDARY_POS_UMIN = 'Umin'
    BOUNDARY_POS_UMAX = 'Umax'
    BOUNDARY_POS_VMIN = 'Vmin'
    BOUNDARY_POS_VMAX = 'Vmax'

    SHIELD_NONE = 'none'
    SHIELD_PEC = 'PEC'
    SHIELD_PMC = 'PMC'

    MODE_TE = 'TE'
    MODE_TM = 'TM'
    MODE_TEM = 'TEM'
    MODE_QTEM = 'QTEM'
    MODE_UNDEF = 'UNDEF'
    MODE_DAMPED = 'DAMPED'
    MODE_PLANE_WAVE = 'PLANE WAVE'
    MODE_FLOQUET = 'FLOQUET'

    FACE_PORT_TYPE_UNKNOWN = 0
    FACE_PORT_TYPE_RECTANGULAR = 1
    FACE_PORT_TYPE_CYLINDRICAL = 2
    FACE_PORT_TYPE_COAXIAL = 3

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Port')

    def reset(self):
        self.record_method('Reset')

    def delete(self, port_number: int):
        self.record_method('Delete', port_number)

    def change_number(self, old_port_number: int, new_port_number: int):
        self.record_method('Rename', old_port_number, new_port_number)

    def change_label(self, port_number: int, label: str):
        self.record_method('RenameLabel', port_number, label)

    def start_port_number_iteration(self) -> int:
        return self.query_method_int('StartPortNumberIteration')

    def start_sparam_port_number_iteration(self) -> int:
        return self.query_method_int('StartSParaPortNumberIteration')

    def get_next_port_number(self) -> int:
        return self.query_method_int('GetNextPortNumber')

    def load_content_for_modify(self) -> int:
        # TODO: Should be recorded? Is docs correct?
        return self.query_method_int('LoadContentForModify')

    def create(self):
        self.record_method('Create')

    def modify(self):
        self.record_method('Modify')

    def set_number(self, number: int):
        self.record_method('PortNumber', number)

    def set_label(self, label: str):
        self.record_method('Label', label)

    def set_folder_name(self, folder_name: str):
        # undocumented, found in the history list
        self.record_method('Folder', folder_name)

    def set_waveguide_monitor(self, flag: bool = True):
        # undocumented, found in the history list
        self.record_method('WaveguideMonitor', flag)

    def set_number_of_modes(self, count: int):
        self.record_method('NumberOfModes', count)

    def set_orientation(self, orientation: str):
        self.record_method('Orientation', orientation)

    def set_coordinates(self, coordinates: str):
        self.record_method('Coordinates', coordinates)

    def set_x_range(self, x_min: float, x_max: float):
        self.record_method('Xrange', x_min, x_max)

    def set_y_range(self, y_min: float, y_max: float):
        self.record_method('Yrange', y_min, y_max)

    def set_z_range(self, z_min: float, z_max: float):
        self.record_method('Zrange', z_min, z_max)

    def set_x_position(self, x: float):
        self.set_x_range(x, x)

    def set_y_position(self, y: float):
        self.set_y_range(y, y)

    def set_z_position(self, z: float):
        self.set_z_range(z, z)

    def add_x_range(self, x_min: float, x_max: float):
        self.record_method('XrangeAdd', x_min, x_max)

    def add_y_range(self, y_min: float, y_max: float):
        self.record_method('YrangeAdd', y_min, y_max)

    def add_z_range(self, z_min: float, z_max: float):
        self.record_method('ZrangeAdd', z_min, z_max)

    def set_on_boundaries(self, flag: bool = True):
        self.record_method('PortOnBound', flag)

    def set_clip_picked_port_to_boundaries(self, flag: bool = True):
        self.record_method('ClipPickedPortToBound', flag)

    def set_text_size(self, size: int):
        self.record_method('TextSize', size)

    def change_text_size(self, port_number: int, size: int):
        self.record_method('ChangeTextSize', port_number, size)

    def set_text_max_limit(self, flag: bool = True):
        self.record_method('TextMaxLimit', flag)

    def set_reference_plane_distance(self, distance: float):
        self.record_method('ReferencePlaneDistance', distance)

    def add_potential_numerically(self, mode_set: int, potential: str, u_pos: float, v_pos: float):
        self.record_method('AddPotentialNumerically', mode_set, potential, u_pos, v_pos)

    def add_potential_picked(self, mode_set: int, potential: str, solid_name: str, face_id: int):
        self.record_method('AddPotentialPicked', mode_set, potential, solid_name, face_id)

    def add_potential_edge_picked(
            self, mode_set: int, potential: str, solid_name: str, edge_id: int):
        self.record_method('AddPotentialEdgePicked', mode_set, potential, solid_name, edge_id)

    def set_adjust_polarization(self, flag: bool = True):
        self.record_method('AdjustPolarization', flag)

    def set_polarization_angle_deg(self, angle_deg: float):
        self.record_method('PolarizationAngle', angle_deg)

    def set_polarization_angle_rad(self, angle_rad: float):
        self.set_polarization_angle_deg(np.rad2deg(angle_rad))

    def set_port_impedance_and_calibration_evaluation(self, flag: bool = True):
        self.record_method('PortImpedanceAndCalibration', flag)

    def add_mode_line_by_point(
            self, line_number: int,
            x_start: float, y_start: float, z_start: float,
            x_end: float, y_end: float, z_end: float):
        self.record_method(
            'AddModeLineByPoint', line_number, x_start, y_start, z_start, x_end, y_end, z_end)

    def add_mode_line_by_face(
            self, line_number: int, x_start: float, y_start: float, z_start: float,
            solid_name: str, face_id: int, reverse: bool = False):
        self.record_method(
            'AddModeLineByFace', line_number,
            x_start, y_start, z_start, solid_name, face_id, reverse)

    def add_mode_line_by_boundary(
            self, line_number: int, x_start: float, y_start: float, z_start: float,
            position: str, reverse: bool = False):
        self.record_method(
            'AddModeLineByBoundary', line_number, x_start, y_start, z_start, position, reverse)

    def add_mode_line(
            self, mode_number: int, impedance_line_number: int, calibration_line_number: int,
            polarization_line_number: int):
        self.record_method(
            'AddModeLine', mode_number, impedance_line_number, calibration_line_number,
            polarization_line_number)

    def set_estimation(self, port_number: int, value: float):
        self.record_method('SetEstimation', port_number, value)

    def set_single_ended(self, flag: bool = True):
        self.record_method('SingleEnded', flag)

    def set_shield(self, key: str):
        self.record_method('Shield', key)

    def get_frequency(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetFrequency', port_number, mode_number)

    def get_cutoff_frequency(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetFcutoff', port_number, mode_number)

    def get_mode_type(self, port_number: int, mode_number: int) -> str:
        return self.record_method('GetModeType', port_number, mode_number)

    def get_beta(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetBeta', port_number, mode_number)

    def get_alpha(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetAlpha', port_number, mode_number)

    def get_accuracy(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetAccuracy', port_number, mode_number)

    def get_wave_impedance(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetWaveImpedance', port_number, mode_number)

    def get_line_impedance(self, port_number: int, mode_number: int) -> float:
        return self.record_method('GetLineImpedance', port_number, mode_number)

    def get_line_impedance_broad_by_index(
            self, port_number: int, mode_number: int, index: int) -> float:
        return self.record_method('GetLineImpedanceBroadByIndex', port_number, mode_number, index)

    def get_line_impedance_broad_by_frequency(
            self, port_number: int, mode_number: int, frequency: float) -> float:
        return self.record_method(
            'GetLineImpedanceBroadByFreq', port_number, mode_number, frequency)

    def get_type(self, port_number: int) -> str:
        return self.record_method('GetType', port_number)

    def get_number_of_modes(self, port_number: int) -> int:
        return self.record_method('GetNumberOfModes', port_number)

    # returns: (orientation, x_min, x_max, y_min, y_max, z_min, z_max)
    def get_port_mesh_location(self, port_number: int) -> tuple[int, int, int, int, int, int, int]:
        L = VBATypeName.Long
        orientations = ['x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max']
        res = self.query_method_t('GetPortMeshLocation', None, port_number, L, L, L, L, L, L, L)
        return (orientations[res[0]], *res[1:])

    # returns: (orientation, x_min, x_max, y_min, y_max, z_min, z_max)
    def get_port_mesh_coordinates(self, port_number: int) \
            -> tuple[int, float, float, float, float, float, float]:
        L, D = VBATypeName.Long, VBATypeName.Double
        orientations = ['x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max']
        res = self.query_method_t('GetPortMeshCoordinates', None, port_number, L, D, D, D, D, D, D)
        return (orientations[res[0]], *res[1:])

    # returns: (x, y, z)
    def get_port_center_coordinates(self, port_number: int) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetPortCenterCoordinates', None, port_number, D, D, D)

    # returns: (face_port_type, size1, size2)
    def get_face_port_type_and_size(self, port_number: int) -> tuple[int, float, float]:
        L, D = VBATypeName.Long, VBATypeName.Double
        return self.query_method_t('GetFacePortTypeAndSize', None, port_number, L, D, D)

    def get_label(self, port_number: int) -> str:
        return self.query_method_str('GetLabel', port_number)