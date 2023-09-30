from . import IVBAProvider, VBAObjWrapper

class Optimizer(VBAObjWrapper):
    GOAL_TYPE_1D_PRIMARY_RESULT = '1D Primary Result'
    GOAL_TYPE_1DC_PRIMARY_RESULT = '1DC Primary Result'
    GOAL_TYPE_0D_RESULT = '0D Result'
    GOAL_TYPE_1D_RESULT = '1D Result'
    GOAL_TYPE_1DC_RESULT = '1DC Result'

    GOAL_SUMMARY_TYPE_SUM_ALL_GOALS = 'Sum_All_Goals'
    GOAL_SUMMARY_TYPE_MAX_ALL_GOALS = 'Max_All_Goals'

    GOAL_OPERATOR_LESS_THAN = '<'
    GOAL_OPERATOR_GREATER_THAN = '>'
    GOAL_OPERATOR_EQUAL = '='
    GOAL_OPERATOR_MIN = 'min'
    GOAL_OPERATOR_MAX = 'max'
    GOAL_OPERATOR_MOVE_MIN = 'move min'
    GOAL_OPERATOR_MOVE_MAX = 'move max'

    GOAL_NORM_MAX_DIFF = 'MaxDiff'
    GOAL_NORM_MAX_DIFF_SQUARED = 'MaxDiffSq'
    GOAL_NORM_SUM_DIFF = 'SumDiff'
    GOAL_NORM_SUM_DIFF_SQUARED = 'SumDiffSq'
    GOAL_NORM_DIFF = 'Diff'
    GOAL_NORM_DIFF_SQUARED = 'DiffSq'

    GOAL_SCALAR_TYPE_MAG_LIN = 'maglin'
    GOAL_SCALAR_TYPE_MAG_DB_10 = 'magdb10'
    GOAL_SCALAR_TYPE_MAG_DB_20 = 'magdb20'
    GOAL_SCALAR_TYPE_REAL = 'real'
    GOAL_SCALAR_TYPE_IMAG = 'imag'
    GOAL_SCALAR_TYPE_PHASE = 'phase'

    GOAL_RANGE_TYPE_TOTAL = 'total'
    GOAL_RANGE_TYPE_RANGE = 'range'
    GOAL_RANGE_TYPE_SINGLE = 'single'

    OPTIMIZER_TYPE_TRUST_REGION = 'Trust_Region'
    OPTIMIZER_TYPE_NELDER_MEAD_SIMPLEX = 'Nelder_Mead_Simplex'
    OPTIMIZER_TYPE_CMAES = 'CMAES'
    OPTIMIZER_TYPE_GENETIC_ALGORITHM = 'Genetic_Algorithm'
    OPTIMIZER_TYPE_PARTICLE_SWARM = 'Particle_Swarm'
    OPTIMIZER_TYPE_INTERPOLATED_NR_VAR_METRIC = 'Interpolated_NR_VariableMetric'
    OPTIMIZER_TYPE_CLASSIC_POWELL = 'Classic Powell'

    INTERPOLATION_SECOND_ORDER = 'Second_Order'

    DISTRIBUTION_TYPE_UNIFORM_RANDOM_NUMBERS = 'Uniform_Random_Numbers'
    DISTRIBUTION_TYPE_LATIN_HYPER_CUBE = 'Latin_Hyper_Cube'
    DISTRIBUTION_TYPE_NOISY_LATIN_HYPER_CUBE = 'Noisy_Latin_Hyper_Cube'
    DISTRIBUTION_TYPE_CUBE = 'Cube_Distribution'

    DATA_STORAGE_STRATEGY_ALL = 'All'
    DATA_STORAGE_STRATEGY_AUTOMATIC = 'Automatic'
    DATA_STORAGE_STRATEGY_NONE = 'None'

    #TODO: check which methods should be recorded and which invoked

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Optimizer')

    def start(self):
        self.invoke_method('Start')

    def set_start_active_solver(self, flag: bool = True):
        self.invoke_method('StartActiveSolver', flag)

    def init_parameter_list(self):
        self.invoke_method('InitParameterList')

    def reset_parameter_list(self):
        self.invoke_method('ResetParameterList')

    def select_parameter(self, param_name: str, use_for_optimization: bool = True):
        self.invoke_method('SelectParameter', param_name, use_for_optimization)

    def set_parameter_init_value(self, value: float):
        self.invoke_method('SetParameterInit', value)

    def set_parameter_min_value(self, value: float):
        self.invoke_method('SetParameterMin', value)

    def set_parameter_max_value(self, value: float):
        self.invoke_method('SetParameterMax', value)

    def set_parameter_number_of_anchors(self, number: int):
        self.invoke_method('SetParameterAnchors', number)

    def set_min_max_auto(self, percentage: float):
        self.invoke_method('SetMinMaxAuto', percentage)

    def set_and_update_min_max_auto(self, percentage: float):
        self.invoke_method('SetAndUpdateMinMaxAuto', percentage)

    def set_always_start_from_current(self, flag: bool = True):
        self.invoke_method('SetAlwaysStartFromCurrent', flag)

    def set_use_data_of_previous_calculations(self, flag: bool = True):
        self.invoke_method('SetUseDataOfPreviousCalculations', flag)

    def get_number_of_varying_parameters(self) -> int:
        return self.query_method_int('GetNumberOfVaryingParameters')

    def get_name_of_varying_parameter(self, index: int) -> str:
        return self.query_method_str('GetNameOfVaryingParameter', index)

    def get_value_of_varying_parameter(self, index: int) -> float:
        return self.query_method_float('GetValueOfVaryingParameter', index)

    def get_param_min_of_varying_parameter(self, index: int) -> float:
        return self.query_method_float('GetParameterMinOfVaryingParameter', index)

    def get_param_max_of_varying_parameter(self, index: int) -> float:
        return self.query_method_float('GetParameterMaxOfVaryingParameter', index)

    def get_param_init_of_varying_parameter(self, index: int) -> float:
        return self.query_method_float('GetParameterInitOfVaryingParameter', index)

    def add_goal(self, goal_type: str) -> int:
        return self.query_method_int('AddGoal', goal_type)

    def select_goal(self, id: int, use_for_optimization: bool = True):
        self.invoke_method('SelectGoal', id, use_for_optimization)

    def delete_goal(self, id: int):
        self.invoke_method('DeleteGoal', id)

    def delete_all_goals(self):
        self.invoke_method('DeleteAllGoals')

    def set_gial_summary_type(self, goal_summary_type: str):
        self.invoke_method('SetGoalSummaryType', goal_summary_type)

    def set_use_goal_for_optimization(self, flag: bool = True):
        self.invoke_method('SetGoalUseFlag', flag)

    def set_goal_operator(self, operator_type: str):
        self.invoke_method('SetGoalOperator', operator_type)

    def set_goal_target(self, value: float):
        self.invoke_method('SetGoalTarget', value)

    def set_goal_norm(self, norm: str):
        self.invoke_method('SetGoalNormNew', norm)

    def set_goal_weight(self, value: float):
        self.invoke_method('SetGoalWeight', value)

    def set_goal_scalar_type(self, scalar_type: str):
        self.invoke_method('SetGoalScalarType', scalar_type)

    def set_goal_1d_result_name(self, name: str):
        self.invoke_method('SetGoal1DResultName', name)

    def set_goal_1dc_result_name(self, name: str):
        self.invoke_method('SetGoal1DCResultName', name)

    def set_goal_template_based_0d_result_name(self, name: str):
        self.invoke_method('SetGoalTemplateBased0DResultName', name)

    def set_goal_template_based_1d_result_name(self, name: str):
        self.invoke_method('SetGoalTemplateBased1DResultName', name)

    def set_goal_template_based_1dc_result_name(self, name: str):
        self.invoke_method('SetGoalTemplateBased1DCResultName', name)

    def set_goal_range(self, min_value: float, max_value: float):
        self.invoke_method('SetGoalRange', min_value, max_value)

    def set_goal_range_type(self, range_type: str):
        self.invoke_method('SetGoalRangeType', range_type)

    def set_use_slope(self, flag: bool = True):
        self.invoke_method('UseSlope', flag)

    def set_goal_target_max(self, value: float):
        self.invoke_method('SetGoalTargetMax', value)

    def set_optimizer_type(self, optimizer_type: str):
        self.invoke_method('SetOptimizerType', optimizer_type)

    def set_use_2nd_order_interpolation(self, optimizer_type: str):
        self.invoke_method('SetUseInterpolation', self.INTERPOLATION_SECOND_ORDER, optimizer_type)

    def set_generation_size(self, optimizer_type: str, size: float):
        self.invoke_method('SetGenerationSize', size, optimizer_type)

    def set_max_number_of_iterations(self, optimizer_type: str, number: int):
        self.invoke_method('SetMaxIt', number, optimizer_type)

    def set_initial_distribution(self, optimizer_type: str, distribution: str):
        self.invoke_method('SetInitialDistribution', distribution, optimizer_type)

    def set_goal_function_level(self, optimizer_type: str, level: float):
        self.invoke_method('SetGoalFunctionLevel', level, optimizer_type)

    def set_goal_function_level(self, optimizer_type: str, rate: float):
        #TODO: in the docs there is 'SetMutaionRate', check whether it is really a mistake
        self.invoke_method('SetMutationRate', rate, optimizer_type)

    def set_min_simplex_size(self, value: float):
        self.invoke_method('SetMinSimplexSize', value)

    def set_use_max_number_of_evaluations(self, optimizer_type: str, flag: bool = True):
        self.invoke_method('SetUseMaxEval', flag, optimizer_type)

    def set_max_number_of_evaluations(self, optimizer_type: str, number: int):
        self.invoke_method('SetMaxEval', number, optimizer_type)

    def set_use_pre_def_point_in_init_distribution(self, optimizer_type: str, flag: bool = True):
        self.invoke_method('SetUsePreDefPointInInitDistribution', flag, optimizer_type)

    def set_number_of_refinements(self, number: int):
        self.invoke_method('SetNumRefinements', number)

    def set_domain_accuracy(self, optimizer_type: str, accuracy: float):
        self.invoke_method('SetDomainAccuracy', accuracy, optimizer_type)

    def set_sigma(self, optimizer_type: str, sigma: float):
        self.invoke_method('SetSigma', sigma, optimizer_type)

    def set_accuracy(self, optimizer_type: str, accuracy: float):
        self.invoke_method('SetAccuracy', accuracy, optimizer_type)

    def set_data_storage_strategy(self, strategy: str):
        self.invoke_method('SetDataStorageStrategy', strategy)

    def set_move_mesh(self, flag: bool = True):
        self.invoke_method('SetOptionMoveMesh', flag)