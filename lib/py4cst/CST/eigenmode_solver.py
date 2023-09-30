from . import IVBAProvider, VBAObjWrapper

class EigenmodeSolver(VBAObjWrapper):
    METHOD_TYPE_AKS = 'AKS'
    METHOD_TYPE_JDM = 'JDM'
    METHOD_TYPE_JDM_LOW_MEM = 'JDM (low memory)'
    METHOD_TYPE_AUTOMATIC = 'Automatic'
    METHOD_TYPE_CLASSICAL = 'Classical (Lossless)'
    METHOD_TYPE_GENERAL = 'General (Lossy)'

    METHOD_TYPE_MESH_HEX = 'Hex'
    METHOD_TYPE_MESH_TET = 'Tet'

    MESH_TYPE_HEXAHEDRAL = 'Hexahedral Mesh'
    MESH_TYPE_TETRAHEDRAL = 'Tetrahedral Mesh'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'EigenmodeSolver')

    def reset(self):
        self.record_method('Reset')

    def start(self):
        return self.query_method_bool('Start')

    def set_mesh_adaptation_hex(self, flag: bool = True):
        self.record_method('SetMeshAdaptationHex', flag)

    def set_mesh_adaptation_tet(self, flag: bool = True):
        self.record_method('SetMeshAdaptationTet', flag)

    def set_number_of_modes(self, number: int):
        self.record_method('SetNumberOfModes', number)

    def set_calculate_modes_in_frequency_range(self, flag: bool = True):
        self.record_method('SetModesInFrequencyRange', flag)

    def set_consider_static_modes(self, flag: bool = True):
        self.record_method('SetConsiderStaticModes', flag)

    def set_use_remote_calculation(self, flag: bool = True):
        self.record_method('SetRemoteCalculation', flag)

    def set_method_type(self, method_type: str, mesh: str):
        self.record_method('SetMethodType', method_type, mesh)

    def set_mesh_type(self, mesh_type: str):
        self.record_method('SetMeshType', mesh_type)

    def set_material_eval_frequency(self, freq: float):
        if freq is None:
            self.record_method('SetMaterialEvaluationFrequency', False, 0.0)
        else:
            self.record_method('SetMaterialEvaluationFrequency', True, freq)

    def set_frequency_target(self, freq: float):
        if freq is None:
            self.record_method('SetFrequencyTarget', False, 0.0)
        else:
            self.record_method('SetFrequencyTarget', True, freq)

    def set_lower_bound_for_q(self, q_min: float):
        if q_min is None:
            self.record_method('SetLowerBoundForQ', False, 0.0)
        else:
            self.record_method('SetLowerBoundForQ', True, q_min)

    def set_lower_bound_for_q(self, flag: bool = True):
        self.record_method('SetLowerBoundForQ', flag, '')

    def set_max_number_of_threads(self, number: int):
        self.record_method('SetMaxNumberOfThreads', number)

    def set_use_parallelization(self, flag: bool = True):
        self.record_method('SetUseParallelization', flag)

    def set_consider_losses_in_postprocessing_only(self, flag: bool = True):
        self.record_method('SetConsiderLossesInPostprocessingOnly', flag)

    def get_consider_losses_in_postprocessing_only(self) -> bool:
        return self.query_method_bool('GetConsiderLossesInPostprocessingOnly')

    def set_minimum_q(self, min_q: float):
        self.record_method('SetMinimumQ', min_q)

    def set_calculate_external_q_factor(self, flag: bool = True):
        self.record_method('SetCalculateExternalQFactor', flag)

    def set_q_external_accuracy(self, accuracy: float):
        self.record_method('SetQExternalAccuracy', accuracy)

    def set_order_tet(self, order: int):
        self.record_method('SetOrderTet', order)

    def set_store_results_in_cache(self, flag: bool = True):
        self.record_method('SetStoreResultsInCache', flag)

    def set_td_compatible_materials(self, flag: bool = True):
        self.record_method('SetTDCompatibleMaterials', flag)

    def set_calculate_thermal_losses(self, flag: bool = True):
        self.record_method('SetCalculateThermalLosses', flag)

    def set_accuracy(self, accuracy: float):
        self.record_method('SetAccuracy', accuracy)

    def get_number_of_modes_calculated(self) -> int:
        return self.query_method_int('GetNumberOfModesCalculated')

    def get_mode_frequency_hz(self, mode_number: int) -> float:
        return self.query_method_float('GetModeFrequencyInHz', mode_number)

    def get_mode_rel_residual_norm(self, mode_number: int) -> float:
        return self.query_method_float('GetModeRelResidualNorm', mode_number)

    def get_mode_q_factor(self, mode_number: int) -> float:
        return self.query_method_float('GetModeQFactor', mode_number)

    def get_mode_external_q_factor(self, mode_number: int) -> float:
        return self.query_method_float('GetModeExternalQFactor', mode_number)

    def get_loaded_frequency_hz(self, mode_number: int) -> float:
        return self.query_method_float('GetLoadedFrequencyInHz', mode_number)

    def get_number_of_sensitivity_design_parameters(self) -> int:
        return self.query_method_int('GetNumberOfSensitivityDesignParameters')

    # indexed from 0
    def get_sensitivity_design_parameter(self, index: int) -> str:
        return self.query_method_str('GetSensitivityDesignParameter', index+1)

    def get_frequency_sensitivity(self, param_name: str, mode_number: int) -> float:
        return self.query_method_float('GetFrequencySensitivity', param_name, mode_number)

    def get_q_factor_sensitivity(self, param_name: str, mode_number: int) -> float:
        return self.query_method_float('GetQFactorSensitivity', param_name, mode_number)

    def reset_force_calculation(self):
        self.record_method('ResetForceCalculation')

    def calculate_lorentz_force_for_mode(self, mode_index: int):
        self.record_method('CalculateLorentzForceForMode', mode_index)

    def calculate_lorentz_force_for_all_modes(self):
        self.record_method('CalculateLorentzForceForAllModes')

    def is_mode_selected_for_force_calculation(self, mode_index: int) -> bool:
        return self.query_method_bool('IsModeSelectedForForceCalculation', mode_index)

    def is_any_mode_selected_for_force_calculation(self) -> bool:
        return self.query_method_bool('IsAnyModeSelectedForForceCalculation')

    def start_force_calculation(self) -> bool:
        return self.query_method_bool('StartForceCalculation')