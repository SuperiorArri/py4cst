from py4cst.CST import Interface, Project, Parameters, Component, LumpedElement, Boundary, Results
from py4cst.results import ASCIIFarfieldExporter
from py4cst import material_library
from pprint import pprint

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.new_microwave_studio_project()

params = proj.get_parameters()
params.store('x', 1.0)
params.store('y', 'x*2', description='x times 2')

print(f'x: {params.restore_as_number('x')}')
print(f'y: {params.restore_expression('y')} = {params.restore_as_number('y')} ({params.get_description('y')})')