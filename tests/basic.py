from py4cst.CST import Interface, Project, Parameters, Component, LumpedElement, Boundary, Results
from py4cst.results import ASCIIFarfieldExporter
from py4cst import material_library
from pprint import pprint

ifc = Interface(2023, start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
# proj = ifc.new_microwave_studio_project()
# print(proj.get_file_name())
# print(proj.get_modeler().is_solver_running())
# params = proj.get_parameters()
# params.store('jejda', 12.3, description='haha')

# le = LumpedElement(proj)
# le.reset()
# le.set_name('test_le')
# le.set_point1(1.2, 1.4, 2.1)
# le.set_point2(0, 0, 0)
# le.set_resistance(50.0)
# le.create()

# le.start_name_iteration()
# print(le.get_next_lumped_element_name())
# print(le.get_properties('test_le'))

# boundary = Boundary(proj)
# print(boundary.get_unit_cell_scan_angle())

# component = Component(proj)
# component.create('component1')
# print(component.does_exist('component2'))
# print(component.get_next_free_name())

# print(proj.query_function_t('SinD', VBATypeName.Double, 1.57075))

# print('VBA res:', proj.query_vba('Anchorpoint.DoesExist("jaha")'))

# proj.generate_history_list()

# print(proj.get_install_path())
# mat = material_library.Material()
# mat.load_from_file(material_library.get_material_path(proj, 'Air'))
# mat.import_to_project(proj)

# results = Results(proj.get_file_name())
# results_3d = results.get_3d()
# pprint(results_3d.get_tree_items())

ffexp = ASCIIFarfieldExporter()
ffexp.prepare(proj, 'farfield (f=3) [1]')
print(ffexp.export_complex_theta())

input("Press Enter to continue...")

# import inspect
# for attr in inspect.getmembers(proj.native_obj):
#     print(attr)

# proj.close()
# ifc.set_quiet_mode(False)
ifc.set_quiet_mode(False)