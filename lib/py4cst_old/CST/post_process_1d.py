from . import Project
from . import ComObjectWrapper

class PostProcess1D(ComObjectWrapper):
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

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.PostProcess1D

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_apply_target(self, apply_target: str):
        self.invoke_method('ApplyTo', apply_target)

    def add_operation(self, operation_type: str):
        self.invoke_method('AddOperation', operation_type)

    def set_deembed_distance(self, port_name: int, distance: float):
        self.invoke_method('SetDeembedDistance', port_name, distance)

    def set_renorm_impedance(self, port_name: int, mode_name: int, impedance: float):
        self.invoke_method('SetRenormImpedance', port_name, mode_name, impedance)

    def set_renorm_impedance_on_all_ports(self, impedance: float):
        self.invoke_method('SetRenormImpedanceOnAllPorts', impedance)

    def reset_renorm_impedance_on_all_ports(self):
        self.invoke_method('SetUnnormImpedanceOnAllPorts')

    def set_consider_port_mode(self, port_name: int, mode_name: int, flag: bool = True):
        self.invoke_method('SetConsiderPortMode', port_name, mode_name, flag)

    def run(self):
        self.invoke_method('Run')

    def set_operation_active(self, operation_type: str, active: bool = True):
        self.invoke_method('ActivateOperation', operation_type, active)