from . import Project
from . import ComObjectWrapper

class ParameterSweep(ComObjectWrapper):
    SIMULATION_TYPE_TRANSIENT = 'Transient'
    SIMULATION_TYPE_PORT_MODES_ONLY = 'Calculate port modes only'
    SIMULATION_TYPE_EIGENMODE = 'Eigenmode'
    SIMULATION_TYPE_FREQUENCY = 'Frequency'
    SIMULATION_TYPE_TLM = 'TLM'
    SIMULATION_TYPE_ASYMPTOTIC = 'Asymtotic'

    SIMULATION_TYPE_E_STATIC = 'E-Static'
    SIMULATION_TYPE_ELECTROQUASISTATIC = 'Electroquasistatic'
    SIMULATION_TYPE_TRANSIENT_ELECTROQUASISTATIC = 'Transient Electroquasistatic'
    SIMULATION_TYPE_M_STATIC = 'M-Static'
    SIMULATION_TYPE_MAGNETOQUASISTATIC = 'Transient Magnetoquasistatic'
    SIMULATION_TYPE_J_STATIC = 'J-Static'
    SIMULATION_TYPE_LOW_FREQUENCY = 'Low Frequency'

    SIMULATION_TYPE_THERMAL = 'Thermal'
    SIMULATION_TYPE_TRANSIENT_THERMAL = 'Transient Thermal'
    SIMULATION_TYPE_STRUCTURAL_MECHANICS = 'Structural Mechanics'

    SIMULATION_TYPE_PIC = 'PIC'
    SIMULATION_TYPE_PARTICLE_TRACKING = 'Particle Tracking'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.ParameterSweep

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_simulation_type(self, sim_type: str):
        self.invoke_method('SetSimulationType', sim_type)

    def add_sequence(self, name: str):
        self.invoke_method('AddSequence', name)

    def delete_sequence(self, name: str):
        self.invoke_method('DeleteSequence', name)

    def set_sequence_enabled(self, name: str, flag: bool = True):
        self.invoke_method('EnableSequence', name, flag)

    def delete_all_sequences(self):
        self.invoke_method('DeleteAllSequences')

    def rename_sequence(self, old_name: str, new_name: str):
        self.invoke_method('RenameSequence', old_name, new_name)

    def add_parameter_samples_lin(
            self, seq_name: str, param_name: str, lower_bound: float, upper_bound: float,
            num_steps: int):
        self.invoke_method(
            'AddParameter_Samples', seq_name, param_name, lower_bound, upper_bound,
            num_steps, False)

    def add_parameter_samples_log(
            self, seq_name: str, param_name: str, lower_bound: float, upper_bound: float,
            num_steps: int):
        self.invoke_method(
            'AddParameter_Samples', seq_name, param_name, lower_bound, upper_bound,
            num_steps, True)

    def add_parameter_step_width(
            self, seq_name: str, param_name: str, lower_bound: float, upper_bound: float,
            width: float):
        self.invoke_method(
            'AddParameter_Stepwidth', seq_name, param_name, lower_bound, upper_bound, width)

    def add_parameter_arbitrary_points(self, seq_name: str, param_name: str, points: list[float]):
        points_str = ';'.join(str(s) for s in points)
        self.invoke_method('AddParameter_ArbitraryPoints', seq_name, param_name, points_str)

    def delete_parameter(self, seq_name: str, param_name: str):
        self.invoke_method('DeleteParameter', seq_name, param_name)

    def start(self):
        self.invoke_method('Start')

    def set_use_distributed_computing(self, flag: bool = True):
        self.invoke_method('UseDistributedComputing', flag)