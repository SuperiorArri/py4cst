from . import Project
from . import ComObjectWrapper

class SolverParameter(ComObjectWrapper):
    SOLVER_TYPE_TRANSIENT = 'Transient solver'
    SOLVER_TYPE_FREQ_DOMAIN = 'Frequency domain solver'
    SOLVER_TYPE_ASYMPTOTIC = 'Asymptotic solver'
    SOLVER_TYPE_EIGENMODE = 'Eigenmode solver'
    SOLVER_TYPE_ELECTROSTATICS = 'Electrostatics solver'
    SOLVER_TYPE_MAGNETOSTATIC = 'Magnetostatic solver'
    SOLVER_TYPE_LF_FREQ_DOMAIN = 'LF Frequency domain solver'
    SOLVER_TYPE_LF_FREQ_DOMAIN_EQS = 'LF Frequency domain solver (EQS)'
    SOLVER_TYPE_STATIONARY_CURRENT = 'Stationary current solver'
    SOLVER_TYPE_PARTICLE_TRACKING = 'Particle tracking solver'
    SOLVER_TYPE_PIC = 'PIC solver'
    SOLVER_TYPE_THERMAL = 'Thermal solver'
    SOLVER_TYPE_INTEGRAL_EQUATION = 'Integral equation solver'
    SOLVER_TYPE_MULTILAYER = 'Multilayer solver'
    SOLVER_TYPE_LF_TIME_DOMAIN_MQS = 'LF Time domain solver (MQS)'
    SOLVER_TYPE_LF_TIME_DOMAIN_EQS = 'LF Time domain solver (EQS)'
    SOLVER_TYPE_THERMAL_TRANSIENT = 'Thermal transient solver'
    SOLVER_TYPE_STRUCTURAL_MECHANICS = 'Structural mechanics solver'
    SOLVER_TYPE_WAKEFIELD = 'Wakefield solver'

    MESH_HEXAHEDRAL = 'Hexahedral'
    MESH_TETRAHEDRAL = 'Tetrahedral'
    MESH_SURFACE = 'Surface'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.SolverParameter

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_solver_type(self, solver_type: str, mesh: str):
        self.invoke_method('SolverType', solver_type, mesh)

    def set_ignore_lossy_metals(self, flag: bool = True):
        self.invoke_method('IgnoreLossyMetals', flag)

    def set_ignore_lossy_dielectrics(self, flag: bool = True):
        self.invoke_method('IgnoreLossyDielectrics', flag)

    def set_ignore_lossy_metals_for_wires(self, flag: bool = True):
        self.invoke_method('IgnoreLossyMetalsForWires', flag)

    def set_ignore_nonlinear_materials(self, flag: bool = True):
        self.invoke_method('IgnoreNonlinearMaterials', flag)

    def set_use_thin_wire_model(self, flag: bool = True):
        self.invoke_method('UseThinWireModel', flag)

    def set_use_zero_wire_radius(self, flag: bool = True):
        self.invoke_method('UseZeroWireRadius', flag)