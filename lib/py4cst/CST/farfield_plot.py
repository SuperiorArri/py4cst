from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np

class FarfieldPlot(VBAObjWrapper):
    PLOT_TYPE_POLAR = 'polar'
    PLOT_TYPE_CARTESIAN = 'cartesian'
    PLOT_TYPE_2D = '2d'
    PLOT_TYPE_2D_ORTHOGRAPHIC = '2dortho'
    PLOT_TYPE_3D = '3d'

    ASCII_VERSION_2009 = '2009'
    ASCII_VERSION_2010 = '2010'

    COORD_SYSTEM_SPHERICAL = 'spherical'
    COORD_SYSTEM_LUDWIG2AE = 'ludwig2ae'
    COORD_SYSTEM_LUDWIG2EA = 'ludwig2ea'
    COORD_SYSTEM_LUDWIG3 = 'ludwig3'

    POLARIZATION_LINEAR = 'linear'
    POLARIZATION_CIRCULAR = 'circular'
    POLARIZATION_SLANT = 'slant'
    POLARIZATION_ABS = 'abs'

    COMPONENT_RADIAL = 'radial'
    COMPONENT_COMP1 = 'comp1'
    COMPONENT_THETA = 'theta'
    COMPONENT_AZIMUTH = 'azimuth'
    COMPONENT_LEFT = 'left'
    COMPONENT_ALPHA = 'alpha'
    COMPONENT_HORIZONTAL = 'horizontal'
    COMPONENT_CROSSPOLAR = 'crosspolar'
    COMPONENT_COMP2 = 'comp2'
    COMPONENT_PHI = 'phi'
    COMPONENT_ELEVATION = 'elevation'
    COMPONENT_RIGHT = 'right'
    COMPONENT_EPSILON = 'epsilon'
    COMPONENT_VERTICAL = 'vertical'
    COMPONENT_COPOLAR = 'copolar'

    COMPLEX_COMP_ABS = 'abs'
    COMPLEX_COMP_PHASE = 'phase'
    COMPLEX_COMP_RE = 're'
    COMPLEX_COMP_IM = 'im'

    TF_TYPE_TIME = 'time'
    TF_TYPE_FREQUENCY = 'frequency'
    TF_TYPE_DEFAULT = ''

    LIST_COMPONENT_THETA = 'Point_T'
    LIST_COMPONENT_PHI = 'Point_P'
    LIST_COMPONENT_RADIUS = 'Point_R'

    CUT_TYPE_POLAR = 'polar'
    CUT_TYPE_LATERAL = 'lateral'

    PLOT_MODE_DIRECTIVITY = 'directivity'
    PLOT_MODE_GAIN = 'gain'
    PLOT_MODE_REALIZED_GAIN = 'realized gain'
    PLOT_MODE_EFIELD = 'efield'
    PLOT_MODE_EPATTERN = 'epattern'
    PLOT_MODE_HFIELD = 'hfield'
    PLOT_MODE_PFIELD = 'pfield'
    PLOT_MODE_RCS = 'rcs'
    PLOT_MODE_RCS_UNITS = 'rcsunits'
    PLOT_MODE_RCS_SW = 'rcssw'

    SEL_COMPONENT_ABS = 'Abs'
    SEL_COMPONENT_AXIAL_RATIO = 'Axial Ratio'
    SEL_COMPONENT_THETA = 'Theta'
    SEL_COMPONENT_THETA_PHASE = 'Theta Phase'
    SEL_COMPONENT_PHI = 'Phi'
    SEL_COMPONENT_PHI_PHASE = 'Phi Phase'
    SEL_COMPONENT_THETA_DIV_PHI = 'Theta/Phi'
    SEL_COMPONENT_PHI_DIV_THETA = 'Phi/Theta'

    # unit codes documented in CST Studio Suite Online Help
    #  (Automation and Scription -> Visual Basic (VBA) -> 3D Simulation VBA -> VBA Objects ->
    #  -> Post Processing -> FarfieldPlot -> function DBUnit
    UNIT_CODE_MINUS_1 = '-1'
    UNIT_CODE_0 = '0'
    UNIT_CODE_60 = '60'
    UNIT_CODE_120 = '120'
    UNIT_CODE_MINUS_60 = '-60'

    MAX_REF_MODE_ABS = 'abs'
    MAX_REF_MODE_PLOT = 'plot'

    AXES_TYPE_XYZ = 'xyz'
    AXES_TYPE_USER = 'user'
    AXES_TYPE_MAIN_LOBE = 'mainlobe'
    AXES_TYPE_CURRENT_WCS = 'currentwcs'

    ANTENNA_TYPE_UNKNOWN = 'unknown'
    ANTENNA_TYPE_ISOTROPIC = 'isotropic'
    ANTENNA_TYPE_ISOTROPIC_LINEAR = 'isotropic_linear'
    ANTENNA_TYPE_DIRECTIONAL_LINEAR = 'directional_linear'
    ANTENNA_TYPE_DIRECTIONAL_CIRCULAR = 'directional_circular'

    PHASE_CENTER_COMPONENT_THETA = 'theta'
    PHASE_CENTER_COMPONENT_PHI = 'phi'
    PHASE_CENTER_COMPONENT_BORESIGHT = 'boresight'

    PHASE_CENTER_PLANE_BOTH = 'both'
    PHASE_CENTER_PLANE_E = 'e-plane'
    PHASE_CENTER_PLANE_H = 'h-plane'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'FarfieldPlot')

    def reset(self):
        self.record_method('Reset')

    def reset_plot(self):
        self.record_method('ResetPlot')

    def set_plot_type(self, plot_type: str):
        self.record_method('Plottype', plot_type)

    def vary_coord(self, angle_variant: int):
        # angle depends on active coordinate system:
        #   Coord system -> variant 1 | variant 2
        #   Spherical -> Theta | Phi
        #   Ludwig 2 AE -> Elevation | Azimuth
        #   Ludwig 2 EA -> Alpha | Epsilon
        #   Ludwig 3 -> Theta | Phi
        self.record_method('Vary', 'angle' + str(angle_variant))

    def set_phi_deg(self, angle_deg: float):
        self.record_method('Phi', angle_deg)

    def set_phi_rad(self, angle_rad: float):
        self.set_phi_deg(np.rad2deg(angle_rad))

    def set_theta_deg(self, angle_deg: float):
        self.record_method('Theta', angle_deg)

    def set_theta_rad(self, angle_rad: float):
        self.set_theta_deg(np.rad2deg(angle_rad))

    def set_theta_step_deg(self, angle_deg: float):
        self.record_method('Step', angle_deg)

    def set_theta_step_rad(self, angle_rad: float):
        self.set_theta_step_deg(np.rad2deg(angle_rad))

    def set_phi_step_deg(self, angle_deg: float):
        self.record_method('Step2', angle_deg)

    def set_phi_step_rad(self, angle_rad: float):
        self.set_phi_step_deg(np.rad2deg(angle_rad))

    def set_lock_steps(self, flag: bool = True):
        self.record_method('SetLockSteps', flag)

    def set_plot_range_only(self, flag: bool = True):
        self.record_method('SetPlotRangeOnly', flag)

    def set_theta_start_deg(self, angle_deg: float):
        self.record_method('SetThetaStart', angle_deg)

    def set_theta_start_rad(self, angle_rad: float):
        self.set_theta_start_deg(np.rad2deg(angle_rad))

    def set_theta_end_deg(self, angle_deg: float):
        self.record_method('SetThetaEnd', angle_deg)

    def set_theta_end_rad(self, angle_rad: float):
        self.set_theta_end_deg(np.rad2deg(angle_rad))

    def set_phi_start_deg(self, angle_deg: float):
        self.record_method('SetPhiStart', angle_deg)

    def set_phi_start_rad(self, angle_rad: float):
        self.set_phi_start_deg(np.rad2deg(angle_rad))

    def set_phi_end_deg(self, angle_deg: float):
        self.record_method('SetPhiEnd', angle_deg)

    def set_phi_end_rad(self, angle_rad: float):
        self.set_phi_end_deg(np.rad2deg(angle_rad))

    def use_farfield_approximation(self, flag: bool = True):
        self.record_method('UseFarfieldApproximation', flag)

    def set_multipoles_max_number(self, max_num: int):
        self.record_method('SetMultipolNumber', max_num)

    def set_frequency(self, freq: float):
        self.record_method('SetFrequency', freq)

    def set_time(self, time: float):
        self.record_method('SetTime', time)

    def set_time_domain_farfield(self, flag: bool = True):
        self.record_method('SetTimeDomainFF', flag)

    def set_num_movie_samples(self, num: int):
        self.record_method('SetMovieSamples', num)

    def plot(self):
        self.record_method('Plot')

    def store_settings(self):
        self.record_method('StoreSettings')

    def export_summary_as_ascii(self, file_name: str):
        self.record_method('ASCIIExportSummary', file_name)

    def set_ascii_export_version(self, version: str):
        self.record_method('ASCIIExportVersion', version)

    def export_source_as_ascii(self, file_name: str):
        self.record_method('ASCIIExportAsSource', file_name)

    def export_broadband_source_as_ascii(self, file_name: str):
        self.record_method('ASCIIExportAsBroadbandSource', file_name)

    def copy_farfield_to_1d_results(self, result_folder: str, result_name: str):
        self.record_method('CopyFarfieldTo1DResults', result_folder, result_name)

    def include_unit_cell_sidewalls(self, flag: bool = True):
        self.record_method('IncludeUnitCellSidewalls', flag)

    def calculate_point_deg(
            self, theta_deg: float, phi_deg: float, field_component: str,
            farfield_name: str = '') -> float:
        return self.query_method_float(
            'CalculatePoint', theta_deg, phi_deg, field_component, farfield_name)

    def calculate_point_rad(
            self, theta_rad: float, phi_rad: float, field_component: str,
            farfield_name: str = '') -> float:
        return self.calculate_point_deg(
            np.rad2deg(theta_rad), np.rad2deg(phi_rad), field_component, farfield_name)

    def calculate_point_no_approx_deg(
            self, theta_deg: float, phi_deg: float, radius: float, field_component: str,
            farfield_name: str = '') -> float:
        return self.query_method_float(
            'CalculatePointNoApprox', theta_deg, phi_deg, radius, field_component, farfield_name)

    def calculate_point_no_approx_rad(
            self, theta_rad: float, phi_rad: float, radius: float, field_component: str,
            farfield_name: str = ''):
        return self.calculate_point_no_approx_deg(
            np.rad2deg(theta_rad), np.rad2deg(phi_rad), radius, field_component, farfield_name)

    def add_list_eval_point_deg(
            self, polar_angle_deg: float, lateral_angle_deg: float, radius: float,
            coord_system: str, tf_type: str, freq_or_time: float):
        self.record_method(
            'AddListEvaluationPoint', polar_angle_deg, lateral_angle_deg, radius,
            coord_system, tf_type, freq_or_time)

    def add_list_eval_point_rad(
            self, polar_angle_rad: float, lateral_angle_rad: float, radius: float,
            coord_system: str, tf_type: str, freq_or_time: float):
        self.add_list_eval_point_deg(
            np.rad2deg(polar_angle_rad), np.rad2deg(lateral_angle_rad),
            radius, coord_system, tf_type, freq_or_time)

    def calculate_list(self, name: str = ''):
        self.record_method('CalculateList', name)

    def get_list(self, field_component: str) -> str:
        return self.query_method_str('GetList', field_component)

    def get_list_item(self, index: int, field_component: str) -> float:
        return self.query_method_float('GetListItem', index, field_component)

    def clear_cuts(self):
        self.record_method('ClearCuts')

    def add_cut_deg(self, cut_type: str, const_angle_deg: float, step_deg: float):
        self.record_method('AddCut', cut_type, const_angle_deg, step_deg)

    def add_cut_rad(self, cut_type: str, const_angle_rad: float, step_rad: float):
        self.add_cut_deg(cut_type, np.rad2deg(const_angle_rad), np.rad2deg(step_rad))

    def set_color_by_value(self, flag: bool = True):
        self.record_method('SetColorByValue', flag)

    def set_theta_360_deg(self, flag: bool = True):
        self.record_method('SetTheta360', flag)

    def draw_step_lines(self, flag: bool = True):
        self.record_method('DrawStepLines', flag)

    def enable_symmetric_range(self, flag: bool = True):
        self.record_method('SymmetricRange', flag)

    def draw_iso_long_lat_lines(self, flag: bool = True):
        self.record_method('DrawIsoLongitudeLatitudeLines', flag)

    def show_structure(self, flag: bool = True):
        self.record_method('ShowStructure', flag)

    def show_structure_profile(self, flag: bool = True):
        self.record_method('ShowStructureProfile', flag)

    def set_structure_transparent(self, flag: bool = True):
        self.record_method('SetStructureTransparent', flag)

    def set_farfield_transparent(self, flag: bool = True):
        self.record_method('SetFarfieldTransparent', flag)

    def set_farfield_size(self, size: int):
        self.record_method('FarfieldSize', size)

    def set_plot_mode(self, plot_mode: str):
        self.record_method('SetPlotMode', plot_mode)

    def get_plot_mode(self) -> str:
        return self.query_method_str('GetPlotMode')

    def select_component(self, sel_component: str):
        self.record_method('SelectComponent', sel_component)

    def enable_polar_extra_lines(self):
        self.record_method('SetSpecials', 'enablepolarextralines')

    def disable_polar_extra_lines(self):
        self.record_method('SetSpecials', 'disablepolarextralines')

    def show_total_radiated_power_linear(self):
        self.record_method('SetSpecials', 'showtrp')

    def show_total_radiated_power_logarithmic(self):
        self.record_method('SetSpecials', 'showtrpdb')

    def hide_total_radiated_power(self):
        self.record_method('SetSpecials', 'showtrpoff')

    def show_total_isotropic_sensitivity_linear(self):
        self.record_method('SetSpecials', 'showtis')

    def show_total_isotropic_sensitivity_logarithmic(self):
        self.record_method('SetSpecials', 'showtisdb')

    def hide_total_isotropic_sensitivity(self):
        self.record_method('SetSpecials', 'showtisoff')

    def set_virtual_sphere_radius(self, radius: float):
        self.record_method('Distance', radius)

    def set_scale_linear(self):
        self.record_method('SetScaleLinear', True)

    def set_scale_logarithmic(self):
        self.record_method('SetScaleLinear', False)

    def is_scale_linear(self) -> bool:
        return self.query_method_bool('IsScaleLinear')

    def is_scale_logarithmic(self) -> bool:
        return not self.is_scale_linear()

    def set_inverse_axial_ratio(self, flag: bool = True):
        self.record_method('SetInverseAxialRatio', flag)

    def has_inverse_axial_ratio(self) -> bool:
        return self.query_method_bool('IsInverseAxialRatio')

    def set_log_plot_range(self, range_db: float):
        self.record_method('SetLogRange', range_db)

    def set_log_plot_normalization(self, norm_db: float):
        self.record_method('SetLogNorm', norm_db)

    def get_log_plot_range(self) -> float:
        return self.query_method_float('GetLogRange')

    def set_main_lobe_threshold(self, threshold_db: float):
        self.record_method('SetMainLobeThreshold', threshold_db)

    def set_db_unit(self, unit_code: str):
        self.record_method('DBUnit', unit_code)

    def set_max_reference_mode(self, max_ref_mode: str):
        self.record_method('SetMaxReferenceMode', max_ref_mode)

    def enable_fixed_plot_maximum(self, flag: bool = True):
        self.record_method('EnableFixPlotMaximum', flag)

    def is_plot_maximum_fixed(self) -> bool:
        return self.query_method_bool('IsPlotMaximumFixed')

    def set_fixed_plot_maximum(self, maximum: float):
        self.record_method('SetFixPlotMaximumValue', maximum)

    def get_fixed_plot_maximum(self) -> float:
        return self.query_method_float('GetFixPlotMaximumValue')

    def set_num_contour_values(self, num: int):
        self.record_method('SetNumberOfContourValues', num)

    def draw_countour_lines(self, flag: bool = True):
        self.record_method('DrawContourLines', flag)

    def set_origin_by_bounding_box(self):
        self.record_method('Origin', 'bbox')

    def set_origin_to_zero(self):
        self.record_method('Origin', 'zero')

    def set_origin(self, x: float, y: float, z: float):
        self.record_method('Origin', 'free')
        self.record_method('Userorigin', x, y, z)

    def set_phi_start_axis(self, x: float, y: float, z: float):
        self.record_method('Phistart', x, y, z)

    def set_theta_start_axis(self, x: float, y: float, z: float):
        self.record_method('Thetastart', x, y, z)

    def set_axes_type(self, axes_type: str):
        self.record_method('SetAxesType', axes_type)

    def set_antenna_type(self, antenna_type: str):
        self.record_method('SetAntennaType', antenna_type)

    def set_polarization_vector(self, x: float, y: float, z: float):
        self.record_method('PolarizationVector', x, y, z)

    def set_coord_system(self, coord_system: str):
        self.record_method('SetCoordinateSystemType', coord_system)

    def set_automatic_coord_system(self, flag: bool = True):
        self.record_method('SetAutomaticCoordinateSystem', flag)

    def set_polarization_linear(self):
        self.record_method('SetPolarizationType', 'linear')

    def set_polarization_circular(self):
        self.record_method('SetPolarizationType', 'circular')

    def set_polarization_slant_deg(self, angle_deg: float):
        self.record_method('SetPolarizationType', 'slant')
        self.record_method('SlantAngle', angle_deg)

    def set_polarization_slant_rad(self, angle_rad: float):
        self.set_polarization_slant_deg(np.rad2deg(angle_rad))

    def use_decoupling_plane(self, flag: bool = True):
        self.record_method('UseDecouplingPlane', flag)

    def set_decoupling_plane_axis(self, axis: str):
        # axis: 'x' or 'y' or 'z'
        self.record_method('DecouplingPlaneAxis', axis)

    def set_decoupling_plane_position(self, position: float):
        self.record_method('DecouplingPlanePosition', position)

    def use_user_defined_decoupling_plane(self, flag: bool = True):
        self.record_method('SetUserDecouplingPlane', flag)

    def get_max_value(self) -> float:
        return self.query_method_float('Getmax')

    def get_min_value(self) -> float:
        return self.query_method_float('Getmin')

    def get_mean_value(self) -> float:
        return self.query_method_float('GetMean')

    def get_radiation_efficiency(self) -> float:
        return self.query_method_float('GetRadiationEfficiency')

    def get_total_efficiency(self) -> float:
        return self.query_method_float('GetTotalEfficiency')

    def get_system_radiation_efficiency(self) -> float:
        return self.query_method_float('GetSystemRadiationEfficiency')

    def get_system_total_efficiency(self) -> float:
        return self.query_method_float('GetSystemTotalEfficiency')

    def get_total_radiated_power(self) -> float: # in watts
        return self.query_method_float('GetTRP')

    def get_total_rcs(self) -> float:
        return self.query_method_float('GetTotalRCS')

    def get_total_acs(self) -> float:
        return self.query_method_float('GetTotalACS')

    def get_main_lobe_angle_deg(self) -> float:
        return self.query_method_float('GetMainLobeDirection')

    def get_main_lobe_angle_rad(self) -> float:
        return np.deg2rad(self.get_main_lobe_angle_deg())

    # returns (x, y, z)
    def get_main_lobe_vector(self) -> tuple[float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetMainLobeVector', D, D, D)

    def get_main_lobe_width_deg(self) -> float:
        return self.query_method_float('GetAngularWidthXdB')

    def get_main_lobe_width_rad(self) -> float:
        return np.deg2rad(self.get_main_lobe_width_deg())

    def get_side_lobe_suppression(self) -> float:
        return self.query_method_float('GetSideLobeSuppression')

    def get_side_lobe_level(self) -> float:
        return self.query_method_float('GetSideLobeLevel')

    def get_front_to_back_ratio(self) -> float:
        return self.query_method_float('GetFrontToBackRatio')

    def enable_phase_center_calculation(self, flag: bool = True):
        self.record_method('EnablePhaseCenterCalculation', flag)

    def set_phase_center_component(self, phase_center_component: str):
        self.record_method('SetPhaseCenterComponent', phase_center_component)

    def set_phase_center_plane(self, phase_center_plane: str):
        self.record_method('SetPhaseCenterPlane', phase_center_plane)

    def set_phase_center_angular_limit_deg(self, limit_deg: float):
        self.record_method('SetPhaseCenterAngularLimit', limit_deg)

    def set_phase_center_angular_limit_rad(self, limit_rad: float):
        self.set_phase_center_angular_limit_deg(np.rad2deg(limit_rad))

    def show_phase_center(self, flag: bool = True):
        self.record_method('ShowPhaseCenter', flag)

    def get_phase_center_avg(self) -> tuple[float, float, float]:
        return self.__get_phase_center('avg')

    def get_phase_center_e_plane(self) -> tuple[float, float, float]:
        return self.__get_phase_center('eplane')

    def get_phase_center_h_plane(self) -> tuple[float, float, float]:
        return self.__get_phase_center('hplane')

    def get_phase_center_expr(self) -> str:
        return self.query_method_str('GetPhaseCenterResultExpr')

    def get_phase_center_expr_avg(self) -> str:
        return self.query_method_str('GetPhaseCenterResultExprAvg')

    def get_phase_center_expr_e_plane(self) -> str:
        return self.query_method_str('GetPhaseCenterResultExprEPlane')

    def get_phase_center_expr_h_plane(self) -> str:
        return self.query_method_str('GetPhaseCenterResultExprHPlane')

    def __get_phase_center(self, mode: str) -> tuple[float, float, float]:
        x = self.query_method_float('GetPhaseCenterResult', 'x', mode)
        y = self.query_method_float('GetPhaseCenterResult', 'y', mode)
        z = self.query_method_float('GetPhaseCenterResult', 'z', mode)
        return (x, y, z)