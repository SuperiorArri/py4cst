from . import Project
from . import ComObjectWrapper

class EigenmodeSolver(ComObjectWrapper):
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

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.EigenmodeSolver

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def start(self) -> bool:
        success = self.invoke_method('Start')
        return success != 0

    def set_mesh_adaptation_hex(self, flag: bool = True):
        self.invoke_method('SetMeshAdaptationHex', flag)

    def set_mesh_adaptation_tet(self, flag: bool = True):
        self.invoke_method('SetMeshAdaptationTet', flag)

    def set_number_of_modes(self, number: int):
        self.invoke_method('SetNumberOfModes', number)

    def set_calculate_modes_in_frequency_range(self, flag: bool = True):
        self.invoke_method('SetModesInFrequencyRange', flag)

    def set_consider_static_modes(self, flag: bool = True):
        self.invoke_method('SetConsiderStaticModes', flag)

    def set_use_remote_calculation(self, flag: bool = True):
        self.invoke_method('SetRemoteCalculation', flag)

    def set_method_type(self, method_type: str, mesh: str):
        self.invoke_method('SetMethodType', method_type, mesh)

    def set_mesh_type(self, mesh_type: str):
        self.invoke_method('SetMeshType', mesh_type)

    def set_material_eval_frequency(self, freq: float):
        if freq is None:
            self.invoke_method('SetMaterialEvaluationFrequency', False, 0.0)
        else:
            self.invoke_method('SetMaterialEvaluationFrequency', True, freq)

    def set_frequency_target(self, freq: float):
        if freq is None:
            self.invoke_method('SetFrequencyTarget', False, 0.0)
        else:
            self.invoke_method('SetFrequencyTarget', True, freq)

    def set_lower_bound_for_q(self, q_min: float):
        if q_min is None:
            self.invoke_method('SetLowerBoundForQ', False, 0.0)
        else:
            self.invoke_method('SetLowerBoundForQ', True, q_min)

    def set_lower_bound_for_q(self, flag: bool = True):
        self.invoke_method('SetLowerBoundForQ', flag, '')

    def set_max_number_of_threads(self, number: int):
        self.invoke_method('SetMaxNumberOfThreads', number)

    def set_use_parallelization(self, flag: bool = True):
        self.invoke_method('SetUseParallelization', flag)

    def set_consider_losses_in_postprocessing_only(self, flag: bool = True):
        self.invoke_method('SetConsiderLossesInPostprocessingOnly', flag)

    def get_consider_losses_in_postprocessing_only(self) -> bool:
        return self.invoke_method('GetConsiderLossesInPostprocessingOnly')

    def set_minimum_q(self, min_q: float):
        self.invoke_method('SetMinimumQ', min_q)

    def set_calculate_external_q_factor(self, flag: bool = True):
        self.invoke_method('SetCalculateExternalQFactor', flag)

    def set_q_external_accuracy(self, accuracy: float):
        self.invoke_method('SetQExternalAccuracy', accuracy)

    def set_order_tet(self, order: int):
        self.invoke_method('SetOrderTet', order)

    def set_store_results_in_cache(self, flag: bool = True):
        self.invoke_method('SetStoreResultsInCache', flag)

    def set_td_compatible_materials(self, flag: bool = True):
        self.invoke_method('SetTDCompatibleMaterials', flag)

    def set_calculate_thermal_losses(self, flag: bool = True):
        self.invoke_method('SetCalculateThermalLosses', flag)

    def set_accuracy(self, accuracy: float):
        self.invoke_method('SetAccuracy', accuracy)

    def get_number_of_modes_calculated(self) -> int:
        return self.invoke_method('GetNumberOfModesCalculated')

    def get_mode_frequency_hz(self, mode_number: int) -> float:
        return self.invoke_method('GetModeFrequencyInHz', mode_number)

    def get_mode_rel_residual_norm(self, mode_number: int) -> float:
        return self.invoke_method('GetModeRelResidualNorm', mode_number)

    def get_mode_q_factor(self, mode_number: int) -> float:
        return self.invoke_method('GetModeQFactor', mode_number)

    def get_mode_external_q_factor(self, mode_number: int) -> float:
        return self.invoke_method('GetModeExternalQFactor', mode_number)

    def get_loaded_frequency_hz(self, mode_number: int) -> float:
        return self.invoke_method('GetLoadedFrequencyInHz', mode_number)

    def get_number_of_sensitivity_design_parameters(self) -> int:
        return self.invoke_method('GetNumberOfSensitivityDesignParameters')

    def get_sensitivity_design_parameter(self, index: int) -> str:
        return self.invoke_method('GetSensitivityDesignParameter', index+1)

    def get_frequency_sensitivity(self, param_name: str, mode_number: int) -> float:
        return self.invoke_method('GetFrequencySensitivity', param_name, mode_number)

    def get_q_factor_sensitivity(self, param_name: str, mode_number: int) -> float:
        return self.invoke_method('GetQFactorSensitivity', param_name, mode_number)

    def reset_force_calculation(self):
        self.invoke_method('ResetForceCalculation')

    def calculate_lorentz_force_for_mode(self, mode_index: int):
        self.invoke_method('CalculateLorentzForceForMode', mode_index)

    def calculate_lorentz_force_for_all_modes(self):
        self.invoke_method('CalculateLorentzForceForAllModes')

    def is_mode_selected_for_force_calculation(self, mode_index: int) -> bool:
        return self.invoke_method('IsModeSelectedForForceCalculation', mode_index)

    def is_any_mode_selected_for_force_calculation(self) -> bool:
        return self.invoke_method('IsAnyModeSelectedForForceCalculation')

    def start_force_calculation(self) -> bool:
        return self.invoke_method('StartForceCalculation')