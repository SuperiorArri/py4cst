from . import IVBAProvider, VBAObjWrapper, VBATypeName
from typing import Union

class FDSolver(VBAObjWrapper):
    OBC_HEX_DEFAULT = 'Default'
    OBC_HEX_PML = 'PML'
    OBC_HEX_FREESPACE_SIBC = 'FreespaceSIBC'

    OBC_TET_DEFAULT = 'Default'
    OBC_TET_PML = 'PML'
    OBC_TET_SIBC = 'SIBC'

    RESET_SAMPLE_INTERVALS_ALL = 'all'
    RESET_SAMPLE_INTERVALS_ADAPTATION = 'adaptation'
    RESET_SAMPLE_INTERVALS_SINGLE = 'single'
    RESET_SAMPLE_INTERVALS_INACTIVE = 'inactive'
    RESET_SAMPLE_INTERVALS_INFINITE = 'infinite'

    SAMPLE_INTERVAL_AUTOMATIC = 'Automatic'
    SAMPLE_INTERVAL_SINGLE = 'Single'
    SAMPLE_INTERVAL_EQUIDISTANT = 'Equidistant'
    SAMPLE_INTERVAL_LOGARITHMIC = 'Logarithmic'

    FREQ_DIST_ADAPT_MODE_LOCAL = 'Local'
    FREQ_DIST_ADAPT_MODE_AS_A_WHOLE = 'As_A_Whole'
    FREQ_DIST_ADAPT_MODE_DISTRIBUTED = 'Distributed'

    TYPE_AUTO = 'Auto'
    TYPE_ITERATIVE = 'Iterative'
    TYPE_DIRECT = 'Direct'

    METHOD_MESH_HEXAHEDRAL = 'Hexahedral'
    METHOD_MESH_TETRAHEDRAL = 'Tetrahedral'
    METHOD_MESH_SURFACE = 'Surface'

    METHOD_SWEEP_GENERAL_PURPOSE = 'General purpose'
    METHOD_SWEEP_FAST_REDUCED_ORDER_MODEL = 'Fast reduced order model'
    METHOD_SWEEP_DISCRETE_SAMPLES_ONLY = 'Discrete samples only'

    STIMULATION_ALL = 'All'
    STIMULATION_ALL_PLUS_FLOQUET = 'All+Floquet'
    STIMULATION_PLANE_WAVE = 'Plane Wave'
    STIMULATION_LIST = 'List'
    STIMULATION_CMA = 'CMA'

    RESULT_DATA_SAMPLING_AUTO = 'Automatic'
    RESULT_DATA_SAMPLING_FREQ_LIN = 'Frequency (linear)'
    RESULT_DATA_SAMPLING_FREQ_LOG = 'Frequency (logarithmic)'
    RESULT_DATA_SAMPLING_FREQ_LOG_LIN = 'Frequency (log-linear)'

    EXCITATION_PORT_ZMIN = 'zmin'
    EXCITATION_PORT_ZMAX = 'zmax'

    EXCITATION_MODE_1 = '1'
    EXCITATION_MODE_1_3_4 = '1;3;4'
    EXCITATION_MODE_TE00 = 'TE(0,0)'
    EXCITATION_MODE_TM00 = 'TM(0,0)'
    EXCITATION_MODE_LCP = 'LCP'
    EXCITATION_MODE_RCP = 'RCP'

    ORDER_TET_FIRST = 'First'
    ORDER_TET_SECOND = 'Second'
    ORDER_TET_THIRD = 'Third'

    ORDER_SRF_FIRST = 'First'
    ORDER_SRF_SECOND = 'Second'
    ORDER_SRF_THIRD = 'Third'

    NETWORK_COMPUTING_STRATEGY_RUN_REMOTE = 'RunRemote'
    NETWORK_COMPUTING_STRATEGY_SAMPLES = 'Samples'

    MLFFM_ACCURACY_VERY_LOW_MEM = 'VeryLowMem'
    MLFFM_ACCURACY_LOW_MEM = 'LowMem'
    MLFFM_ACCURACY_DEFAULT = 'Default'
    MLFFM_ACCURACY_HIGH_ACC = 'HighAcc'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'FDSolver')

    def reset(self):
        self.record_method('Reset')

    def start(self):
        self.invoke_method('Start')

    def set_accelerated_restart(self, flag: bool = True):
        self.record_method('AcceleratedRestart', flag)

    def set_accuracy_tet(self, value: float):
        self.record_method('AccuracyTet', value)

    def set_accuracy_srf(self, value: float):
        self.record_method('AccuracySrf', value)

    def set_accuracy_hex(self, value: float):
        self.record_method('AccuracyHex', value)

    def set_accuracy_rom(self, value: float):
        self.record_method('AccuracyROM', value)

    def set_store_all_results(self, flag: bool = True):
        self.record_method('StoreAllResults', flag)

    def set_store_solution_coefficients(self, flag: bool = True):
        self.record_method('StoreSolutionCoefficients', flag)

    def set_create_legacy_1d_signals(self, flag: bool = True):
        self.record_method('CreateLegacy1DSignals', flag)

    def set_obc_type_hex(self, obc_type: str):
        self.record_method('SetOpenBCTypeHex', obc_type)

    def set_obc_type_tet(self, obc_type: str):
        self.record_method('SetOpenBCTypeTet', obc_type)

    def set_add_monitor_samples(self, flag: bool = True):
        self.record_method('AddMonitorSamples', flag)

    def set_max_number_of_frequency_samples(self, number: int):
        self.record_method('FrequencySamples', number)

    def set_mesh_adaptation_hex(self, flag: bool = True):
        self.record_method('MeshAdaptionHex', flag)

    def set_mesh_adaption_tet(self, flag: bool = True):
        self.record_method('MeshAdaptionTet', flag)

    def reset_sample_intervals(self, key: str):
        self.record_method('ResetSampleIntervals', key)

    def set_use_helmholtz_equation(self, flag: bool = True):
        self.record_method('UseHelmholtzEquation', flag)

    def add_sample_interval(self, min: float, max: float, num_samples: int, key: str):
        self.record_method('AddSampleInterval', min, max, num_samples, key, False)

    def add_sample_interval_with_adaptation(
            self, min: float, max: float, num_samples: int, key: str):
        self.record_method('AddSampleInterval', min, max, num_samples, key, True)

    def add_inactive_sample_interval(self, min: float, max: float, num_samples: int, key: str):
        self.record_method('AddInactiveSampleInterval', min, max, num_samples, key, False)

    def add_inactive_sample_interval_with_adaptation(
            self, min: float, max: float, num_samples: int, key: str):
        self.record_method('AddInactiveSampleInterval', min, max, num_samples, key, True)

    def set_max_number_of_iterations(self, count: int):
        self.record_method('MaxIterations', count)

    def set_limit_iterations(self, flag: bool = True):
        self.record_method('LimitIterations', flag)

    def set_modes_only(self, flag: bool = True):
        self.record_method('ModesOnly', flag)

    def set_shield_all_ports(self, flag: bool = True):
        self.record_method('SetShieldAllPorts', flag)

    def set_port_mesh_matches_3d_mesh_tet(self, flag: bool = True):
        self.record_method('SetPortMeshMatches3DMeshTet', flag)

    def set_allow_rom_port_mode_solver(self, flag: bool = True):
        self.record_method('SetAllowROMPortModeSolver', flag)

    def set_allow_discrete_port_solver(self, flag: bool = True):
        self.record_method('SetAllowDiscretePortSolver', flag)

    def set_use_rom_port_mode_solver_tet(
            self, general_purpose: bool = True, fast_reduced_order_model : bool = True):
        self.record_method('SetUseROMPortModeSolverTet', general_purpose, fast_reduced_order_model)

    def set_enable_native_single_ended(self, flag: bool = True):
        self.record_method('EnableNativeSingleEnded', flag)

    def set_use_deembedded_fields(self, flag: bool = True):
        self.record_method('UseDeembeddedFields', flag)

    def set_freq_dist_adapt_mode(self, mode: str):
        self.record_method('FreqDistAdaptMode', mode)

    def set_prefer_lean_output(self, flag: bool = True):
        self.record_method('SetPreferLeanOutput', flag)

    def set_use_imp_line_impedance_as_reference(self, flag: bool = True):
        self.record_method('SetUseImpLineImpedanceAsReference', flag)

    def set_use_orient_port_with_mask(self, flag: bool = True):
        self.record_method('SetUseOrientPortWithMask', flag)

    def set_consider_port_losses_tet(self, flag: bool = True):
        self.record_method('ConsiderPortLossesTet', flag)

    def set_stop_sweep_if_criterion_met(self, flag: bool = True):
        self.record_method('SetStopSweepIfCriterionMet', flag)

    def set_s_params_sweep_threshold(self, threshold: float):
        self.record_method('SetSweepThreshold', 'S-Parameters', threshold)

    def set_probes_sweep_threshold(self, threshold: float):
        self.record_method('SetSweepThreshold', 'Probes', threshold)

    def set_use_s_params_sweep_threshold(self, flag: bool = True):
        self.record_method('UseSweepThreshold', 'S-Parameters', flag)

    def set_use_probes_sweep_threshold(self, flag: bool = True):
        self.record_method('UseSweepThreshold', 'Probes', flag)

    def set_type(self, solver_type: str):
        self.record_method('Type', solver_type)

    def set_store_results_in_cache(self, flag: bool = True):
        self.record_method('StoreResultsInCache', flag)

    def set_method(self, mesh_method: str, sweep_method: str):
        self.record_method('SetMethod', mesh_method, sweep_method)

    def set_auto_norm_impedance(self, flag: bool = True):
        self.record_method('AutoNormImpedance', flag)

    def set_norming_impedance(self, impedance: float):
        self.record_method('NormingImpedance', impedance)

    def set_stimulation(self, port: Union[str, int], mode: Union[str, int]):
        self.record_method('Stimulation', port, mode)

    def set_number_of_sweep_error_checks(self, number: int):
        self.record_method('SweepErrorChecks', number)

    def set_minimum_number_of_sweep_samples(self, number: int):
        self.record_method('SweepMinimumSamples', number)

    def set_sweep_consider_all(self, flag: bool = True):
        self.record_method('SweepConsiderAll', flag)

    def reset_sweep_consider_list(self):
        self.record_method('SweepConsiderReset')

    def consider_sweep_s_param(self, port_out: int, mode_out: int, mode_in: int):
        self.record_method('SweepConsiderSPar', port_out, mode_out, mode_in)

    def set_minimum_number_of_result_data_samples(self, number: int):
        self.record_method('SetNumberOfResultDataSamples', number)

    def set_result_data_sampling_mode(self, mode: str):
        self.record_method('SetResultDataSamplingMode', mode)

    def set_extrude_open_boundary_condition(self, flag: bool = True):
        self.record_method('ExtrudeOpenBC', flag)

    def set_td_compatible_materials(self, flag: bool = True):
        self.record_method('TDCompatibleMaterials', flag)

    def set_calculate_static_b_field(self, flag: bool = True):
        self.record_method('CalcStatBField', flag)

    def set_calculate_power_loss(self, flag: bool = True):
        self.record_method('CalcPowerLoss', flag)

    def set_calculate_power_loss_per_component(self, flag: bool = True):
        self.record_method('CalcPowerLossPerComponent', flag)

    def set_use_green_sandy_ferrite_model(self, flag: bool = True):
        self.record_method('SetUseGreenSandyFerriteModel', flag)

    def set_green_sandy_threshold_h_field(self, threshold: float = True):
        self.record_method('SetGreenSandyThresholdH', threshold)

    def reset_excitation_list(self):
        self.record_method('ResetExcitationList')

    def add_item_to_excitation_list(self, port: Union[str, int], mode: str):
        self.record_method('AddToExcitationList', port, mode)

    def set_use_parallelization(self, flag: bool = True):
        self.record_method('UseParallelization', flag)

    def set_max_number_of_cpu_threads(self, number: int):
        self.record_method('MaxCPUs', number)

    def set_max_number_of_cpu_devices(self, number: int):
        self.record_method('MaximumNumberOfCPUDevices', number)

    def set_sweep_weight_evanescent(self, weight: float):
        self.record_method('SweepWeightEvanescent', weight)

    def set_low_frequency_stabilization(self, flag: bool = True):
        self.record_method('LowFrequencyStabilization', flag)

    def set_order_tet(self, order: str):
        self.record_method('OrderTet', order)

    def set_mixed_order_tet(self, flag: bool = True):
        self.record_method('MixedOrderTet', flag)

    def set_order_srf(self, order: str):
        self.record_method('OrderSrf', order)

    def set_mixed_order_srf(self, flag: bool = True):
        self.record_method('MixedOrderSrf', flag)

    def set_use_distributed_computing(self, flag: bool = True):
        self.record_method('UseDistributedComputing', flag)

    def set_network_computing_strategy(self, strategy: str):
        self.record_method('NetworkComputingStrategy', strategy)

    def set_network_computing_job_count(self, count: int):
        self.record_method('NetworkComputingJobCount', count)

    def set_use_sensitivity_analysis(self, flag: bool = True):
        self.record_method('UseSensitivityAnalysis', flag)

    def set_use_double_precision(self, flag: bool = True):
        self.record_method('UseDoublePrecision', flag)

    def set_preconditioner_accuracy_int_eq(self, tolerance: float):
        self.record_method('PreconditionerAccuracyIntEq', tolerance)

    def set_min_mlffm_box_size(self, tolerance: float):
        self.record_method('MinMLFMMBoxSize', tolerance)

    def set_mlffm_accuracy(self, accuracy: str):
        self.record_method('MLFMMAccuracy', accuracy)

    def set_use_cfie_for_cpec_int_eq(self, flag: bool = True):
        self.record_method('UseCFIEForCPECIntEq', flag)

    def set_use_fast_rcs_sweep_int_eq(self, flag: bool = True):
        self.record_method('UseFastRCSSweepIntEq', flag)

    def set_mrcs_sweep_properties(
            self,
            phi_start: float, phi_end: float, num_phi_steps: int,
            theta_start: float, theta_end: float, num_theta_steps: int,
            e_inc_theta: float, e_inc_phi: float):
        self.record_method(
            'SetMRCSSweepProperties', phi_start, phi_end, num_phi_steps,
            theta_start, theta_end, num_theta_steps, e_inc_theta, e_inc_phi)

    # returns: (
        # phi_start, phi_end, num_phi_steps,
        # theta_start, theta_end, num_theta_steps
        # e_inc_theta, e_inc_phi, activation
        # )
    def get_mrcs_sweep_properties(self) \
            -> tuple[float, float, int, float, float, int, float, float, bool]:
        D, I, B = VBATypeName.Double, VBATypeName.Integer, VBATypeName.Boolean
        return self.query_method_t('GetRCSSweepProperties', D, D, I, D, D, I, D, D, B)

    def set_calc_block_excitation_in_parallel(
            self, enable: bool, use_block: bool, max_parallel: int):
        self.record_method('SetCalcBlockExcitationsInParallel', enable, use_block, max_parallel)

    def set_write_3d_fields_for_farfield_calc(self, flag: bool = True):
        self.record_method('SetWrite3DFieldsForFarfieldCalc', flag)

    def set_record_unit_cell_scan_farfield_on(self):
        self.record_method('SetRecordUnitCellScanFarfield', 'on')

    def set_record_unit_cell_scan_farfield_off(self):
        self.record_method('SetRecordUnitCellScanFarfield', 'off')

    def set_record_unit_cell_scan_farfield_auto(self):
        self.record_method('SetRecordUnitCellScanFarfield', 'auto')

    def set_record_unit_cell_scan_farfield(self, flag: bool = True):
        self.record_method('SetRecordUnitCellScanFarfield', 'on' if flag else 'off')

    def set_write_3d_fields_for_farfield_calc(self, flag_theta: bool = True, flag_phi: bool = True):
        self.record_method('SetConsiderUnitCellScanFarfieldSymmetry', flag_theta, flag_phi)

    def set_disable_result_templates_during_unit_cell_scan_angle_sweep(self, flag: bool = True):
        self.record_method('SetDisableResultTemplatesDuringUnitCellScanAngleSweep', flag)

    def extract_unit_cell_scan_farfield(
            self, frequencies: list[float], names: list[str], anchor: int):
        freq_str = ';'.join(str(s) for s in frequencies)
        names_str = ';'.join(str(s) for s in names)
        self.record_method('ExtractUnitCellScanFarfield', freq_str, names_str, anchor)

    def update_interpolation_settings(self, navigation_tree_path: str):
        self.record_method('UpdateInterpolationSettings', navigation_tree_path)

    def export_mor_solution(self, frequency: float):
        self.record_method('ExportMORSolution', frequency)

    def set_force_recalculate_old_samples(self, flag: bool = True):
        self.record_method('ForceRecalculateOldSamples', flag)

    def set_allow_float_direct_solver(self, flag: bool = True):
        self.record_method('SetAllowFloatDirectSolver', flag)

    def set_allow_change_settings_for_schematic(self, flag: bool = True):
        self.record_method('SetAllowChangeSettingsForSchematic', flag)