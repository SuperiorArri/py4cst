from . import IVBAProvider, VBAObjWrapper

class IESolver(VBAObjWrapper):
    ACCURACY_CUSTOM = 'Custom'
    ACCURACY_LOW = 'Low'
    ACCURACY_MEDIUM = 'Medium'
    ACCURACY_HIGH = 'High'

    REAL_GROUND_MODEL_AUTO = 'Auto'
    REAL_GROUND_MODEL_TYPE1 = 'Type 1'
    REAL_GROUND_MODEL_TYPE2 = 'Type 2'

    PRECONDITIONER_AUTO = 'Auto'
    PRECONDITIONER_TYPE1 = 'Type 1'
    PRECONDITIONER_TYPE2 = 'Type 2'
    PRECONDITIONER_TYPE3 = 'Type 3'

    CMA_ACCURACY_DEFAULT = 'Default'
    CMA_ACCURACY_CUSTOM = 'Custom'

    CMA_MEM_CUSTOM = 'Custom'
    CMA_MEM_LOW = 'Low'
    CMA_MEM_MEDIUM = 'Medium'
    CMA_MEM_HIGH = 'High'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'IESolver')

    def reset(self):
        self.record_method('Reset')

    def set_accuracy_setting(self, accuracy: str):
        self.record_method('SetAccuracySetting', accuracy)

    def set_use_fast_frequency_sweep(self, flag: bool = True):
        self.record_method('UseFastFrequencySweep', flag)

    def set_use_ie_ground_plane(self, flag: bool = True):
        self.record_method('UseIEGroundPlane', flag)

    def set_real_ground_material_name(self, name: str):
        if name is None:
            name = ''
        self.record_method('SetRealGroundMaterialName', name)

    def set_calc_farfield_in_real_ground(self, flag: bool = True):
        self.record_method('CalcFarFieldInRealGround', flag)

    def set_real_ground_model_type(self, model_type: str):
        self.record_method('RealGroundModelType', model_type)

    def set_preconditioner_type(self, preconditioner_type: str):
        self.record_method('PreconditionerType', preconditioner_type)

    def set_low_frequency_stabilization(self, flag: bool = True):
        self.record_method('LowFrequencyStabilization', flag)

    def set_low_frequency_stabilization_multilayer(self, flag: bool = True):
        self.record_method('LowFrequencyStabilizationML', flag)

    def set_multilayer(self, flag: bool = True):
        self.record_method('Multilayer', flag)

    def set_iterative_mom_accuracy_ie_solver(self, accuracy: float):
        self.record_method('SetiMoMACC_I', accuracy)

    def set_iterative_mom_accuracy_multilayer_solver(self, accuracy: float):
        self.record_method('SetiMoMACC_M', accuracy)

    def set_cfie_alpha(self, accuracy: float):
        self.record_method('SetCFIEAlpha', accuracy)

    def set_deembed_external_ports(self, flag: bool = True):
        self.record_method('DeembedExternalPorts', flag)

    def set_open_boundary_condition_in_xy_dir(self, flag: bool = True):
        self.record_method('SetOpenBC_XY', flag)

    def set_cma_mode_tracking(self, flag: bool = True):
        self.record_method('ModeTrackingCMA', flag)

    def set_cma_number_of_modes(self, number: int):
        self.record_method('NumberOfModesCMA', number)

    def set_cma_start_frequency(self, freq: float):
        self.record_method('StartFrequencyCMA', freq)

    def set_cma_accuracy_setting(self, accuracy: str):
        self.record_method('SetAccuracySettingCMA', accuracy)

    def set_cma_number_of_frequency_samples(self, number: int):
        self.record_method('FrequencySamplesCMA', number)

    def set_cma_mem_setting(self, mem: str):
        self.record_method('SetMemSettingCMA', mem)

    def set_cma_calculate_modal_weighting_coefficients(self, flag: bool = True):
        self.record_method('CalculateModalWeightingCoefficientsCMA', flag)