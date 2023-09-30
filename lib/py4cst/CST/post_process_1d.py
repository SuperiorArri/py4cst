from . import IVBAProvider, VBAObjWrapper

class PostProcess1D(VBAObjWrapper):
    APPLY_TARGET_S_PARAM = 'S-parameter'
    APPLY_TARGET_PROBES = 'Probes'
    APPLY_TARGET_MONITORS = 'Monitors'

    OPERATION_TYPE_TIME_WINDOW = 'Time Window'
    OPERATION_TYPE_AR_FILTER = 'AR-Filter'
    OPERATION_TYPE_PHASE_DEEMBEDDING = 'Phase Deembedding'
    OPERATION_TYPE_RENORMALIZATION = 'Renormalization'
    OPERATION_TYPE_VSWR = 'VSWR'
    OPERATION_TYPE_YZ_MATRICES = 'YZ-matrices'
    OPERATION_TYPE_EXCLUDE_PORT_MODES = 'Exclude Port Modes'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'PostProcess1D')

    def reset(self):
        self.record_method('Reset')

    def set_apply_target(self, apply_target: str):
        self.record_method('ApplyTo', apply_target)

    def add_operation(self, operation_type: str):
        self.record_method('AddOperation', operation_type)

    def set_deembed_distance(self, port_name: int, distance: float):
        self.record_method('SetDeembedDistance', port_name, distance)

    def set_renorm_impedance(self, port_name: int, mode_name: int, impedance: float):
        self.record_method('SetRenormImpedance', port_name, mode_name, impedance)

    def set_renorm_impedance_on_all_ports(self, impedance: float):
        self.record_method('SetRenormImpedanceOnAllPorts', impedance)

    def reset_renorm_impedance_on_all_ports(self):
        self.record_method('SetUnnormImpedanceOnAllPorts')

    def set_consider_port_mode(self, port_name: int, mode_name: int, flag: bool = True):
        self.record_method('SetConsiderPortMode', port_name, mode_name, flag)

    def run(self):
        self.invoke_method('Run')

    def set_operation_active(self, operation_type: str, active: bool = True):
        self.record_method('ActivateOperation', operation_type, active)