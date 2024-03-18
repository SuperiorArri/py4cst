from py4cst.CST import Interface

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.new_microwave_studio_project()

print(proj.get_application_name())
print(proj.get_application_version())
print(proj.get_project_path())