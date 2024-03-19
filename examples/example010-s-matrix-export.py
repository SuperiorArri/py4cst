from py4cst.CST import Interface, Results
from py4cst.results import SParameter

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
results = Results(proj.get_file_name())
s_param = SParameter(results)

s_param.select_by_indices((1,1))
# Or also specify the Run ID: s_param.select_by_indices((1,1), run_id=1)
# Or select by name (name of the item in the Navigation Tree): s_param.select_by_name('S1,1')

s11 = s_param.get_values()
frequencies = s_param.get_frequencies()

# Find the closest index of specifix frequency
f0 = 5.5
f0_idx = min(range(len(frequencies)), key=lambda i: abs(frequencies[i]-f0))
print(s11[f0_idx])