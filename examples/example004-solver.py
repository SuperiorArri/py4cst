from py4cst.CST import Interface, Project, Modeler, HFSolver, IESolver, EigenmodeSolver

interface = Interface()
proj = interface.new_microwave_studio_project()
modeler = proj.get_modeler()

# Set Solver Type
proj.set_solver_type(Project.SOLVER_HF_TIME_DOMAIN)
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
hf_solver = HFSolver(proj)
hf_solver.set_adaptive_port_meshing(True)

# Solver specific settings example
ie_solver = IESolver(proj)
ie_solver.set_accuracy_setting(IESolver.ACCURACY_HIGH)

# Getting some data
eig_solver = EigenmodeSolver(proj)
num_modes = eig_solver.get_number_of_modes_calculated()
f_mod1 = eig_solver.get_mode_frequency_hz(1)