from . import IVBAProvider, VBAObjWrapper

class MeshAdaption3D(VBAObjWrapper):
    TYPE_E_STATIC = 'EStatic'
    TYPE_M_STATIC = 'MStatic'
    TYPE_J_STATIC = 'JStatic'
    TYPE_LOW_FREQ = 'LowFrequency'
    TYPE_HIGH_FREQ_HEX = 'HighFrequencyHex'
    TYPE_HIGH_FREQ_TET = 'HighFrequencyTet'
    TYPE_TIME = 'Time'

    STRATEGY_EXPERT_SYSTEM = 'ExpertSystem'
    STRATEGY_ENERGY = 'Energy'

    REFINEMENT_TYPE_AUTOMATIC = 'Automatic'
    REFINEMENT_TYPE_BISECTION = 'Bisection'

    ERROR_ESTIMATOR_TYPE_AUTOMATIC = 'Automatic'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'MeshAdaption3D')

    def set_error_limit(self, value: float):
        self.record_method('Errorlimit', value)

    def set_accuracy_factor(self, value: float):
        self.record_method('AccuracyFactor', value)

    def set_type(self, value: str):
        self.record_method('SetType', value)

    def set_adaptation_strategy(self, value: str):
        self.record_method('SetAdaptionStrategy', value)

    def set_refinement_type(self, value: str):
        self.record_method('RefinementType', value)

    def set_error_estimator_type(self, value: str):
        self.record_method('ErrorEstimatorType', value)

    def set_min_number_of_passes(self, value: int):
        self.record_method('MinPasses', value)

    def set_max_number_of_passes(self, value: int):
        self.record_method('MaxPasses', value)

    def set_cell_increase_factor(self, value: float):
        self.record_method('CellIncreaseFactor', value)

    def set_weight_e(self, value: float):
        self.record_method('WeightE', value)

    def set_weight_b(self, value: float):
        self.record_method('WeightB', value)

    def set_refine_x(self, flag: bool = True):
        self.record_method('RefineX', flag)

    def set_refine_y(self, flag: bool = True):
        self.record_method('RefineY', flag)

    def set_refine_z(self, flag: bool = True):
        self.record_method('RefineZ', flag)

    def set_refine_xyz(self, refine_x: bool, refine_y: bool, refine_z: bool):
        self.set_refine_x(refine_x)
        self.set_refine_y(refine_y)
        self.set_refine_z(refine_z)

    def set_max_delta_s(self, value: float):
        self.record_method('MaxDeltaS', value)

    def clear_stop_criteria(self):
        self.record_method('ClearStopCriteria')

    def add_s_param_stop_criterion(
            self, auto_freq: bool, f_min: float, f_max: float, max_delta: float,
            num_checks: int, active: bool = True):
        #TODO: split into multiple functions
        self.record_method(
            'AddSParameterStopCriterion', auto_freq, f_min, f_max, max_delta, num_checks, active)

    def add_0d_result_stop_criterion(
            self, result_name: str, max_delta: float, num_checks: int, active: bool = True):
        #TODO: split into multiple functions
        self.record_method('Add0DResultStopCriterion', result_name, max_delta, num_checks, active)

    def add_1d_result_stop_criterion(
            self, result_name: str, max_delta: float, num_checks: int, active: bool = True,
            is_complex: bool = True):
        #TODO: split into multiple functions
        self.record_method(
            'Add1DResultStopCriterion', result_name, max_delta, num_checks, active, is_complex)

    def add_stop_criterion(
            self, group_name: str, threshold: float, num_checks: int, active: bool = True):
        #TODO: split into multiple functions
        self.record_method('AddStopCriterion', group_name, threshold, num_checks, active)

    def remove_all_custom_stop_criteria(self):
        self.record_method('RemoveAllUserDefinedStopCriteria')

    def set_mesh_increment(self, value: float):
        self.record_method('MeshIncrement', value)

    def set_frequency_range(self, f_min: float, f_max: float):
        self.record_method('SetFrequencyRange', False, f_min, f_max)

    def set_frequency_range_auto(self):
        self.record_method('SetFrequencyRange', True, 0, 0)

    def set_number_of_skipped_pulses(self, value: float):
        self.record_method('SkipPulses', value)

    def set_number_of_delta_s_checks(self, value: int):
        self.record_method('NumberOfDeltaSChecks', value)

    def set_number_of_prop_const_checks(self, value: int):
        self.record_method('NumberOfPropConstChecks', value)

    def set_propagation_constant_accuracy(self, value: float):
        self.record_method('PropagationConstantAccuracy', value)

    def set_subsequent_checks_only_once(self, flag: bool = True):
        self.record_method('SubsequentChecksOnlyOnce', flag)

    def set_wavelength_based_refinement(self, flag: bool = True):
        self.record_method('WavelengthBasedRefinement', flag)

    def set_min_accepted_cell_growth(self, value: float):
        self.record_method('MinimumAcceptedCellGrowth', value)

    def set_ref_theta_factor(self, value: float):
        self.record_method('RefThetaFactor', value)

    def set_min_mesh_cell_growth(self, value: float):
        self.record_method('SetMinimumMeshCellGrowth', value)

    def set_linear_growth_limitation(self, value: float):
        self.record_method('SetLinearGrowthLimitation', value)

    def set_linear_growth_limitation_enabled(self, flag: bool = True):
        self.record_method('EnableLinearGrowthLimitation', flag)

    def set_singular_edge_refinement(self, value: int):
        self.record_method('SingularEdgeRefinement', value)

    def set_snap_to_geometry(self, flag: bool = True):
        self.record_method('SnapToGeometry', flag)

    def set_inner_s_param_adaptation_enabled(self, flag: bool = True):
        self.record_method('EnableInnerSParameterAdaptation', flag)

    def set_port_propagation_const_adaptation_enabled(self, flag: bool = True):
        self.record_method('EnablePortPropagationConstantAdaptation', flag)