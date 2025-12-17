from py4cst.cst import Interface
from py4cst import material_library

interface = Interface()
proj = interface.new_microwave_studio_project()

material_names = material_library.get_available_materials(proj)

if len(material_names) == 0:
    print('No available materials found.')
else:
    print('Available materials:')
    for mat_name in material_names:
        print(f'- {mat_name}')
    print(f'Loading the first material found: {material_names[0]}')
    mat = material_library.Material()
    mat.load_from_file(material_library.get_material_path(proj, material_names[0]))
    mat.import_to_project(proj)
