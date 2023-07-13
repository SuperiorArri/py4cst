import lib_test
from py4cst import material_library as ml
from py4cst.CST import Interface, Project

cst = Interface()
cst.create_new_mws_project()
proj = Project(cst)

material = ml.Material()
material.set_custom_name('MyCopper')
# mat_file_path = ml.get_default_win_material_path(2023, 'Copper (pure)')
mat_file_path = ml.get_material_path(proj, 'Copper (pure)')
material.load_from_file(mat_file_path)
print('Loaded:', material.get_loaded_name())
material.import_to_project(proj)

lib_test.finalize()