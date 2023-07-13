from . import Project
from . import ComObjectWrapper

class ADSCosimulation(ComObjectWrapper):
    SOLVER_TYPE_TRANSIENT = 'transient'
    SOLVER_TYPE_FREQUNCY_DOMAIN = 'frequency domain'

    PARAM_TYPE_NONE = 'None'
    PARAM_TYPE_LENGTH = 'Length'
    PARAM_TYPE_TEMPERATURE = 'Temperature'
    PARAM_TYPE_VOLTAGE = 'Voltage'
    PARAM_TYPE_CURRENT = 'Current'
    PARAM_TYPE_RESISTANCE = 'Resistance'
    PARAM_TYPE_CONDUCTANCE = 'Conductance'
    PARAM_TYPE_CAPACITANCE = 'Capacitance'
    PARAM_TYPE_INDUCTANCE = 'Inductance'
    PARAM_TYPE_FREQUENCY = 'Frequency'
    PARAM_TYPE_TIME = 'Time'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.ADSCosimulation

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_cosimulation_enabled(self, flag: bool = True):
        self.invoke_method('EnableCoSimulation', flag)

    def set_use_interpolation(self, flag: bool = True):
        self.invoke_method('UseInterpolation', flag)

    def set_solver_type(self, solver_type: str):
        self.invoke_method('SolverType', solver_type)

    def set_description(self, description: str):
        self.invoke_method('Description', description)

    def set_parameter_info(
            self, param_name: str, use: bool, param_type: str, nominal_value: float,
            step_size: float):
        self.invoke_method(
            'ParameterInformation', param_name, use, param_type, nominal_value, step_size)