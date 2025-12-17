from py4cst.cst import Interface, Project, Parameters
import py4cst.cst_file_utils as cfu

interface = Interface()
proj: Project = interface.new_microwave_studio_project()
params = Parameters(proj)
modeler = proj.get_modeler()

# Load CST file:
cst_file = cfu.decode('path/to/project.cst')
dec_params = cfu.get_parameters(cst_file)
dec_history_list = cfu.get_history_list(cst_file)

# Import parameters:
for p in dec_params: # store names first to avoid need to resolve dependencies
    params.store(p.name, 0)
for p in dec_params:
    params.store(p.name, p.expression, p.description)

# Import history list:
for it in dec_history_list:
    if it.type == 'vba' and not it.hidden:
        modeler.add_to_history(f'[imported] {it.caption}', it.code)
