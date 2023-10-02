from py4cst.CST import Interface, Results
from py4cst.results import SParameter

ifc = Interface(2023, start_mode=Interface.StartMode.Existing)
proj = ifc.get_active_project()
results = Results(proj.get_file_name())

s_param = SParameter(results)
s_param.select_by_indices((1,1))

print(s_param.get_num_samples())
print(s_param.get_frequencies()[:4])
print(s_param.get_values()[:4])