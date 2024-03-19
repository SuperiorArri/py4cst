from py4cst.CST import Interface, MeshSettings

interface = Interface()
proj = interface.new_microwave_studio_project()
mesh_settings = MeshSettings(proj)

mesh_settings.set_mesh_type(MeshSettings.MESH_TYPE_HEX)

mesh_settings.set_number_of_steps_per_wave_near(18)
# mesh_settings.set_number_of_steps_per_wave_far(18)
mesh_settings.set_wavelength_refinement_same_as_near(True)

mesh_settings.set_number_of_steps_per_box_near(21)
mesh_settings.set_number_of_steps_per_box_far(2)