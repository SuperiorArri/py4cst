from py4cst.cst import Interface, Project
from py4cst.cst.wrappers import Solver, IESolver, EigenmodeSolver

interface = Interface()
proj = interface.new_microwave_studio_project()
modeler = proj.get_modeler()

# Set Solver Type
proj.set_solver_type(Project.SolverType.HF_TIME_DOMAIN)
print(proj.get_solver_type())

# Run Solver
modeler.run_solver()

# Abort Solver
modeler.abort_solver()

# Pause Solver
modeler.pause_solver()

# Resume Solver
modeler.resume_solver()

# High Frequency Solver settings example
hf_solver = Solver(proj)
hf_solver.set_adaptive_port_meshing(True)

# Solver specific settings example
ie_solver = IESolver(proj)
ie_solver.set_accuracy_setting(IESolver.Accuracy.HIGH)

# Getting some data
eig_solver = EigenmodeSolver(proj)
num_modes = eig_solver.get_number_of_modes_calculated()
f_mod1 = eig_solver.get_mode_frequency_in_hz(1)
