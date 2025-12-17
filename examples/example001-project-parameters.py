from py4cst.cst import Interface

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.new_microwave_studio_project()

params = proj.get_parameters()
params.store('x', 1.0)
params.store('y', 'x*2', description='x times 2')

x_num = params.restore_as_number('x')
y_num = params.restore_as_number('y')
y_expr = params.restore_expression('y')
y_desc = params.get_description('y')
print(f'x: {x_num}')
print(f'y: {y_expr} = {y_num} ({y_desc})')
