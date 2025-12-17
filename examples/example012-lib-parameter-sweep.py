from py4cst.cst import Interface, Parameters
from py4cst.parameter_sweep import ParameterSweep

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.new_microwave_studio_project()
modeler = proj.get_modeler()
parameters = Parameters(proj)

parameters.store('x', 0)
parameters.store('y', 0)

input("Parameters created (check the values in the editor). Press Enter to continue...")

param_sweep = ParameterSweep(parameters)
param_sweep.set_parameter('x', [0, 1])
param_sweep.set_parameter('y', [2, 2.1, 2.2])

def callback_before_iteration(values):
    print('Callback before iteration:')
    print('- values:', values)
    input("Parameters set (check the values in the editor). Press Enter to continue...")

def callback_after_iteration(values):
    print('Callback after iteration:')
    print('- values:', values)

def callback_to_start_simulation():
    # here you can just run the solver or do more stuff
    # for example: modeler.run_solver()
    print('Running the solver...')

param_sweep.set_callback_before_iteration(callback_before_iteration)
param_sweep.set_callback_after_iteration(callback_after_iteration)
param_sweep.set_callback_start_simulation(callback_to_start_simulation)

param_sweep.start()
