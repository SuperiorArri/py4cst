from . import Project
from . import ComObjectWrapper
from . import FrequencyRangeList

class HFSolver(ComObjectWrapper):
    PML_TYPE_CONVOLUTION = 'ConvPML'
    PML_TYPE_GENERALIZED = 'GTPML'

    UPDATE_SCHEMA_GAP = 'Gap'
    UPDATE_SCHEMA_DISTRIBUTED = 'Distributed'

    SURPRESS_TSS_TRUE = 'True'
    SURPRESS_TSS_ALL = 'All'
    SURPRESS_TSS_FALSE = 'False'
    SURPRESS_TSS_NONE = 'None'
    SURPRESS_TSS_RESET = 'Reset'
    SURPRESS_TSS_PORTS = 'Ports'
    SURPRESS_TSS_LUMPED_ELEMENTS = 'LumpedElements'
    SURPRESS_TSS_PROBES = 'Probes'
    SURPRESS_TSS_UI_MONITORS = 'UIMonitors'

    EXCITATION_PORT_MODE = 'portmode'
    EXCITATION_PLANE_WAVE = 'planewave'
    EXCITATION_FIELD_SOURCE = 'fieldsource'
    EXCITATION_FARFIELD_SOURCE = 'farfieldsource'

    SIMULT_EXCIT_OFFSET_TIMESHIFT = 'Timeshift'
    SIMULT_EXCIT_OFFSET_PHASESHIFT = 'Phaseshift'

    ABSORB_AUTOMATIC = 'Automatic'
    ABSORB_ACTIVATE = 'Activate'
    ABSORB_DEACTIVATE = 'Deactivate'

    EXCITATION_TYPE_AUTOMATIC = 'Automatic'
    EXCITATION_TYPE_STANDARD = 'Standard'
    EXCITATION_TYPE_BROADBAND = 'Broadband'

    DECOMPOSITION_TYPE_AUTOMATIC = 'Automatic'
    DECOMPOSITION_TYPE_STANDARD = 'Standard'
    DECOMPOSITION_TYPE_BROADBAND = 'Broadband'

    WINDOW_RECTANGULAR = 'Rectangular'
    WINDOW_COSINE = 'Cosine'

    HFTD_DISP_UPDATE_SCHEME_STANDARD = 'Standard'
    HFTD_DISP_UPDATE_SCHEME_GENERALIZED = 'Generalized'
    HFTD_DISP_UPDATE_SCHEME_AUTOMATIC = 'Automatic'

    SUBCYCLE_STATE_AUTOMATIC = 'Automatic'
    SUBCYCLE_STATE_ACTIVATE = 'Activate'
    SUBCYCLE_STATE_DEACTIVATE = 'Deactivate'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Solver

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_time_between_updates(self, value: int):
        self.invoke_method('TimeBetweenUpdates', value)

    def set_frequency_range(self, min_freq: float, max_freq: float):
        self.invoke_method('FrequencyRange', min_freq, max_freq)

    def calculate_zy_matrices(self):
        self.invoke_method('CalculateZandYMatrices')

    def calculate_vswr(self):
        self.invoke_method('CalculateVSWR')

    def set_pba_fill_limit(self, percentage: float):
        self.invoke_method('PBAFillLimit', percentage)

    def use_split_components(self, flag: bool = True):
        self.invoke_method('UseSplitComponents', flag)

    def always_exclude_pec(self, flag: bool = True):
        self.invoke_method('AlwaysExcludePec', flag)

    def set_mpi_parallelization(self, flag: bool = True):
        self.invoke_method('MPIParallelization', flag)

    def get_min_frequency(self) -> float:
        return self.invoke_attribute('GetFmin')

    def get_max_frequency(self) -> float:
        return self.invoke_attribute('GetFmax')

    def get_number_of_frequency_samples(self) -> int:
        return self.invoke_attribute('GetNFsamples')

    def get_number_of_ports(self) -> int:
        return self.invoke_attribute('GetNumberOfPorts')

    def are_ports_subsequently_named(self) -> bool:
        return self.invoke_attribute('ArePortsSubsequentlyNamed')

    def get_stimulation_port(self) -> int:
        return self.invoke_attribute('GetStimulationPort')

    def get_stimulation_mode(self) -> int:
        return self.invoke_attribute('GetStimulationMode')

    def get_total_simulation_time(self) -> int:
        return self.invoke_attribute('GetTotalSimulationTime')

    def get_matrix_calculation_time(self) -> int:
        return self.invoke_attribute('GetMatrixCalculationTime')

    def get_last_solver_time(self) -> int:
        return self.invoke_attribute('GetLastSolverTime')

    def start(self):
        self.invoke_method('Start')

    def set_normalize_impedances_automatically(self, flag: bool = True):
        self.invoke_method('AutoNormImpedance', flag)

    def set_norming_impedance(self, impedance: float):
        self.invoke_method('NormingImpedance', impedance)

    def set_mesh_adaptation(self, flag: bool = True):
        self.invoke_method('MeshAdaption', flag)

    def set_use_distributed_computing(self, flag: bool = True):
        self.invoke_method('UseDistributedComputing', flag)

    def set_distribute_matrix_calculation(self, flag: bool = True):
        self.invoke_method('DistributeMatrixCalculation', flag)

    def set_use_hardware_acceleration(self, flag: bool = True):
        self.invoke_method('HardwareAcceleration', flag)

    def set_store_td_results_in_cache(self, flag: bool = True):
        self.invoke_method('StoreTDResultsInCache', flag)

    def set_number_of_frequency_samples(self, num_samples: int):
        self.invoke_method('FrequencySamples', num_samples)

    def set_number_of_log_frequency_samples(self, num_samples: int):
        self.invoke_method('FrequencyLogSamples', num_samples)

    def set_consider_two_port_reciprocity(self, flag: bool = True):
        self.invoke_method('ConsiderTwoPortReciprocity', flag)

    def set_energy_balance_limit(self, limit: float):
        self.invoke_method('EnergyBalanceLimit', limit)

    def set_time_step_stability_factor(self, factor: float):
        self.invoke_method('TimeStepStabilityFactor', factor)

    def set_normalize_to_reference_signal(self, flag: bool = True):
        self.invoke_method('NormalizeToReferenceSignal', flag)

    def set_normalize_to_default_signal_when_in_use(self, flag: bool = True):
        self.invoke_method('NormalizeToDefaultSignalWhenInUse', flag)

    def set_detect_identical_ports_automatically(self, flag: bool = True):
        self.invoke_method('AutoDetectIdenticalPorts', flag)

    def set_sample_time_signal_automatically(self, flag: bool = True):
        self.invoke_method('AutomaticTimeSignalSampling', flag)

    def set_consider_excitation_for_freq_sampling_rate(self, flag: bool = True):
        self.invoke_method('ConsiderExcitationForFreqSamplingRate', flag)

    def set_perform_tdr_computation(self, flag: bool = True):
        self.invoke_method('TDRComputation', flag)

    def set_shift_tdr_50_percent(self, flag: bool = True):
        self.invoke_method('TDRShift50Percent', flag)

    def set_perform_tdr_reflection_computation(self, flag: bool = True):
        self.invoke_method('TDRReflection', flag)

    def set_use_broadband_phase_shift(self, flag: bool = True):
        self.invoke_method('UseBroadBandPhaseShift', flag)

    def set_broadband_phase_shift_lower_bound_factor(self, value: float):
        self.invoke_method('SetBroadBandPhaseShiftLowerBoundFac', value)

    def set_sparam_adjustment(self, flag: bool = True):
        self.invoke_method('SParaAdjustment', flag)

    def set_prepare_farfields(self, flag: bool = True):
        self.invoke_method('PrepareFarfields', flag)

    def set_monitor_farfields_near_to_model(self, flag: bool = True):
        self.invoke_method('MonitorFarFieldsNearToModel', flag)

    def set_dump_solver_matrices(self, flag: bool = True):
        self.invoke_method('MatrixDump', flag)

    def set_restart_after_instability_abort(self, flag: bool = True):
        self.invoke_method('RestartAfterInstabilityAbort', flag)

    def set_max_number_of_threads(self, num_threads: int):
        self.invoke_method('MaximumNumberOfThreads', num_threads)

    def set_pml_type(self, pml_type: str):
        self.invoke_method('SetPMLType', pml_type)

    def set_update_schema_discrete_items(self, schema: str):
        self.invoke_method('DiscreteItemUpdate', schema)

    def set_update_schema_discrete_items_edge(self, schema: str):
        self.invoke_method('DiscreteItemEdgeUpdate', schema)

    def set_update_schema_discrete_items_face(self, schema: str):
        self.invoke_method('DiscreteItemFaceUpdate', schema)

    def get_update_schema_discrete_items(self):
        return self.invoke_attribute('GetDiscreteItemUpdate')

    def get_update_schema_discrete_items_edge(self):
        return self.invoke_attribute('GetDiscreteItemEdgeUpdate')

    def get_update_schema_discrete_items_face(self):
        return self.invoke_attribute('GetDiscreteItemFaceUpdate')

    def surpress_time_signal_storage(self, key: str):
        self.invoke_method('SuppressTimeSignalStorage', key)

    def set_calculate_modes_only(self, flag: bool = True):
        self.invoke_method('CalculateModesOnly', flag)

    def set_stimulation_mode(self, mode_number: int):
        self.invoke_method('StimulationMode', mode_number)

    def set_stimulation_by_all_ports(self):
        self.invoke_method('StimulationPort', 'All')

    def set_stimulation_by_selected_port(self):
        self.invoke_method('StimulationPort', 'Selected')

    def set_stimulation_by_plane_wave(self):
        self.invoke_method('StimulationPort', 'Plane Wave')

    def set_stimulation_by_port(self, port_number: int):
        self.invoke_method('StimulationPort', port_number)

    def reset_excitation_modes(self):
        self.invoke_method('ResetExcitationModes')

    def set_excitation_port_mode(
            self, port: int, mode: int, amplitude: float, phase: float,
            signal: str = "default", active: bool = True):
        self.invoke_method('ExcitationPortMode', port, mode, amplitude, phase, signal, active)

    def set_excitation_field_source(
            self, name: str, amplitude: float, phase: float,
            signal: str = "default", active: bool = True):
        self.invoke_method('ExcitationFieldSource', name, amplitude, phase, signal, active)

    def define_excitation(
            self, excitation: str, name: int, mode: int, amplitude: float, phase_or_time:
            float, signal_name: str, active: bool = True):
        self.invoke_method(
            'DefineExcitation', excitation, name, mode, amplitude, phase_or_time,
            signal_name, active)

    def define_excitation_settings(
            self, excitation: str, name: int, mode: int, amplitude: float, phase_or_time:
            float, signal_name: str, accuracy: float, f_min: float, f_max: float,
            active: bool = True):
        self.invoke_method(
            'DefineExcitationSettings', excitation, name, mode, amplitude, phase_or_time,
            signal_name, accuracy, f_min, f_max, active)

    def set_phase_ref_frequency(self, frequency: float):
        self.invoke_method('PhaseRefFrequency', frequency)

    def set_s_param_port_excitation(self, flag: bool = True):
        self.invoke_method('SParameterPortExcitation', flag)

    def set_simultaneous_excitation(self, flag: bool = True):
        self.invoke_method('SimultaneousExcitation', flag)

    def set_simultaneous_excitation_auto_label(self, flag: bool = True):
        self.invoke_method('SetSimultaneousExcitAutoLabel', flag)

    def set_simultaneous_excitation_label(self, label: str):
        self.invoke_method('SetSimultaneousExcitationLabel', label)

    def set_simultaneous_excitation_offset(self, offset: str):
        self.invoke_method('SetSimultaneousExcitationOffset', offset)

    def set_excitation_selection_show_additional_settings(self, flag: bool = True):
        self.invoke_method('ExcitationSelectionShowAdditionalSettings', flag)

    def set_superimpose_plw_excitation(self, flag: bool = True):
        self.invoke_method('SuperimposePLWExcitation', flag)

    def set_show_excitation_list_accuracy(self, flag: bool = True):
        self.invoke_method('ShowExcitationListAccuracy', flag)

    def set_show_excitation_list_monitor_freq_interval(self, flag: bool = True):
        self.invoke_method('ShowExcitationListMonitorFreqInterval', flag)

    def set_use_s_param_symmetries(self, flag: bool = True):
        self.invoke_method('SParaSymmetry', flag)

    def reset_s_param_symmetries(self):
        self.invoke_method('ResetSParaSymm')

    def define_new_s_param_symmetries(self):
        self.invoke_method('DefSParaSymm')

    def add_s_param(self, port_num1: int, port_num2: int):
        self.invoke_method('SPara', port_num1, port_num2)

    def set_waveguide_port_generalized(self, flag: bool = True):
        self.invoke_method('WaveguidePortGeneralized', flag)

    def set_waveguide_port_mode_tracking(self, flag: bool = True):
        self.invoke_method('WaveguidePortModeTracking', flag)

    def set_absorb_unconsidered_mode_fields(self, key: str):
        self.invoke_method('AbsorbUnconsideredModeFields', key)

    def set_absorb_unconsidered_mode_fields(self, flag: bool = True):
        key = self.ABSORB_ACTIVATE if flag else self.ABSORB_DEACTIVATE
        self.invoke_method('AbsorbUnconsideredModeFields', key)

    def set_absorb_unconsidered_mode_fields_auto(self):
        self.invoke_method('AbsorbUnconsideredModeFields', self.ABSORB_AUTOMATIC)

    def set_full_deembedding(self, flag: bool = True):
        self.invoke_method('FullDeembedding', flag)

    def set_number_of_samples_full_deembedding(self, number: int):
        self.invoke_method('SetSamplesFullDeembedding', number)

    def set_consider_dispersive_behavior_full_deembedding(self, flag: bool = True):
        self.invoke_method('DispEpsFullDeembedding', flag)

    def set_waveguide_port_broadband(self, flag: bool = True):
        self.invoke_method('WaveguidePortBroadband', flag)

    def set_mode_freq_factor(self, factor: float):
        self.invoke_method('SetModeFreqFactor', factor)

    def set_scale_te_tm_mode_to_center_frequency(self, flag: bool = True):
        self.invoke_method('ScaleTETMModeToCenterFrequency', flag)

    def set_waveguide_port_excitation_type(self, excitation_type: str):
        self.invoke_method('WaveguidePortExcitationType', excitation_type)

    def set_waveguide_port_decomposition_type(self, decomposition_type: str):
        self.invoke_method('WaveguidePortDecompositionType', decomposition_type)

    def set_voltage_waveguide_port(self, port_name: int, value: float):
        self.invoke_method('SetVoltageWaveguidePort', port_name, value, True)

    def unset_voltage_waveguide_port(self, port_name: int):
        self.invoke_method('SetVoltageWaveguidePort', port_name, 0.0, False)

    def set_adaptive_port_meshing(self, flag: bool = True):
        self.invoke_method('AdaptivePortMeshing', flag)

    def set_adaptive_port_meshing_accuracy(self, accuracy_percent: int):
        self.invoke_method('AccuracyAdaptivePortMeshing', accuracy_percent)

    def set_adaptive_port_meshing_number_of_passes(self, number: int):
        self.invoke_method('PassesAdaptivePortMeshing', number)

    def set_number_of_pulse_widths(self, number: int):
        self.invoke_method('NumberOfPulseWidths', number)

    def enable_steady_state_monitor(self, accuracy_dB: float):
        self.invoke_method('SteadyStateLimit', accuracy_dB)

    def disable_steady_state_monitor(self):
        self.invoke_method('SteadyStateLimit', 'No Check')

    def add_stop_criterion(
            self, group_name: str, threshold: float, num_checks: int, active: bool = True):
        self.invoke_method('AddStopCriterion', group_name, threshold, num_checks, active)

    def add_stop_criterion_with_target_frequency(
            self, group_name: str, threshold: float, num_checks: int,
            target_frequency_ranges: FrequencyRangeList, active: bool = True):
        self.invoke_method(
            'AddStopCriterionWithTargetFrequency', group_name, threshold, num_checks,
            active, str(target_frequency_ranges))

    def set_stop_criteria_show_excitation(self, flag: bool = True):
        self.invoke_method('StopCriteriaShowExcitation', flag)

    def set_use_ar_filter(self, flag: bool = True):
        self.invoke_method('UseArfilter', flag)

    def set_ar_max_energy_deviation(self, limit: float):
        self.invoke_method('ArMaxEnergyDeviation', limit)

    def set_ar_number_of_pulses_to_skip(self, number: int):
        self.invoke_method('ArPulseSkip', number)

    def start_ar_filter(self):
        self.invoke_method('StartArFilter')

    def set_time_window(
            self, window: str, smoothness_percent: int, enabled_on_transient_sim: bool = True):
        self.invoke_method('SetTimeWindow', window, smoothness_percent, enabled_on_transient_sim)

    def set_surface_impedance_order(self, order: int):
        self.invoke_method('SurfaceImpedanceOrder', order)

    def set_activate_power_loss_1d_monitor(self, flag: bool = True):
        self.invoke_method('ActivatePowerLoss1DMonitor', flag)

    def set_power_loss_1d_monitor_per_solid(self, flag: bool = True):
        self.invoke_method('PowerLoss1DMonitorPerSolid', flag)

    def set_use_3d_field_monitor_for_power_loss_1d_monitor(self, flag: bool = True):
        self.invoke_method('Use3DFieldMonitorForPowerLoss1DMonitor', flag)

    def set_use_farfield_monitor_for_power_loss_1d_monitor(self, flag: bool = True):
        self.invoke_method('UseFarFieldMonitorForPowerLoss1DMonitor', flag)

    def set_use_extra_freq_for_power_loss_1d_monitor(self, flag: bool = True):
        self.invoke_method('UseExtraFreqForPowerLoss1DMonitor', flag)

    def reset_power_loss_1d_monitor_extra_freqs(self):
        self.invoke_method('ResetPowerLoss1DMonitorExtraFreq')

    def add_power_loss_1d_monitor_extra_freq(self, freq: float):
        self.invoke_method('AddPowerLoss1DMonitorExtraFreq', freq)

    def set_time_power_loss_si_material_monitor(self, flag: bool = True):
        self.invoke_method('SetTimePowerLossSIMaterialMonitor', flag)

    def activate_timer_power_loss_si_material_monitor(self, t_start: float, t_step: float):
        self.invoke_method('ActivateTimePowerLossSIMaterialMonitor', t_start, t_step, 0.0, False)

    def activate_timer_power_loss_si_material_monitor_lim(
            self, t_start: float, t_step: float, t_end: float):
        self.invoke_method('ActivateTimePowerLossSIMaterialMonitor', t_start, t_step, t_end, True)

    def set_time_power_loss_si_material_monitor_average(self, flag: bool = True):
        self.invoke_method('SetTimePowerLossSIMaterialMonitorAverage', flag)

    def set_time_power_loss_si_material_monitor_average_rep_period(self, period: float):
        self.invoke_method('SetTimePowerLossSIMaterialMonitorAverageRepPeriod', period)

    def set_time_power_loss_si_material_monitor_per_solid(self, flag: bool = True):
        self.invoke_method('TimePowerLossSIMaterialMonitorPerSolid', flag)

    def set_disp_non_linear_material_monitor(self, flag: bool = True):
        self.invoke_method('SetDispNonLinearMaterialMonitor', flag)

    def activate_disp_non_linear_material_monitor(self, t_start: float, t_step: float):
        self.invoke_method('ActivateDispNonLinearMaterialMonitor', t_start, t_step, 0.0, False)

    def activate_disp_non_linear_material_monitor_lim(
            self, t_start: float, t_step: float, t_end: float):
        self.invoke_method('ActivateDispNonLinearMaterialMonitor', t_start, t_step, t_end, True)

    def set_activate_space_material_3d_monitor(self, flag: bool = True):
        self.invoke_method('ActivateSpaceMaterial3DMonitor', flag)

    def set_use_3d_field_monitor_for_space_material_3d_monitor(self, flag: bool = True):
        self.invoke_method('Use3DFieldMonitorForSpaceMaterial3DMonitor', flag)

    def set_use_extra_freq_for_space_material_3d_monitor(self, flag: bool = True):
        self.invoke_method('UseExtraFreqForSpaceMaterial3DMonitor', flag)

    def reset_space_material_3d_monitor_extra_freqs(self):
        self.invoke_method('ResetSpaceMaterial3DMonitorExtraFreq')

    def add_space_material_3d_monitor_extra_freq(self, freq: float):
        self.invoke_method('AddSpaceMaterial3DMonitorExtraFreq', freq)

    def set_hftd_disp_update_scheme(self, scheme: str):
        self.invoke_method('SetHFTDDispUpdateScheme', scheme)

    def set_use_tst_at_port(self, flag: bool = True):
        self.invoke_method('UseTSTAtPort', flag)

    def set_sybcycle_state(self, state: str):
        self.invoke_method('SetSubcycleState', state)

    def set_simplified_pba_method(self, flag: bool = True):
        self.invoke_method('SimplifiedPBAMethod', flag)

    def set_aks_penalty_factor(self, factor: float):
        self.invoke_method('AKSPenaltyFactor', factor)

    def set_aks_estimation(self, factor: float):
        self.invoke_method('AKSEstimation', factor)

    def set_aks_number_of_iterations(self, number: int):
        self.invoke_method('AKSIterations', number)

    def set_aks_accuracy(self, accuracy: float):
        self.invoke_method('AKSAccuracy', accuracy)

    def reset_aks(self):
        self.invoke_method('AKSReset')

    def start_aks(self):
        self.invoke_method('AKSStart')

    def set_aks_number_of_estimation_cycles(self, number: int):
        self.invoke_method('AKSEstimationCycles', number)

    def set_aks_automatic_estimation(self, flag: bool = True):
        self.invoke_method('AKSAutomaticEstimation', flag)

    def set_aks_number_of_check_modes(self, number: int):
        self.invoke_method('AKSCheckModes', number)

    def set_aks_maximum_df(self, delta_frequency: float):
        self.invoke_method('AKSMaximumDF', delta_frequency)

    def set_aks_max_number_of_passes(self, number: int):
        self.invoke_method('AKSMaximumPasses', number)

    def set_aks_mesh_increment(self, inc: int):
        self.invoke_method('AKSMeshIncrement', inc)

    def set_aks_min_number_of_passes(self, number: int):
        self.invoke_method('AKSMinimumPasses', number)

    def get_aks_number_of_modes(self) -> int:
        return self.invoke_method('AKSGetNumberOfModes')