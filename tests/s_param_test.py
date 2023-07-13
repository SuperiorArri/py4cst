import lib_test
from py4cst import CST
from py4cst import results

cst = CST.Interface(version=2023)
proj = CST.Project(cst)

s_params = results.SParameters(CST.ResultTree(proj))

frequencies = s_params.get_frequencies()
s_mats = s_params.get_matrices()

print(frequencies)
print(s_mats)

lib_test.finalize()