from py4cst.CST import Interface, Project

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
try:
    proj = ifc.get_active_project()
    # Or open the project from path: proj = ifc.open_project('<path to the project>')
except RuntimeError:
    proj = ifc.new_microwave_studio_project()
except Exception as e:
    print(e)
    exit(1)

print(proj.get_application_name())
print(proj.get_application_version())
print(proj.get_project_path(Project.PATH_TYPE_PROJECT))
# proj.close()