from py4cst.CST import Interface, Results
from py4cst.results import CustomSTensor
import matplotlib.pyplot as plt
import numpy as np

ifc = Interface(start_mode=Interface.StartMode.ExistingOrNew)
proj = ifc.get_active_project()
results = Results(proj.get_file_name())

# CustomSTensor allows one to define a custom S-Matrix array structure
#  - useful in cases where the S-Parameters don't follow naming pattern S(j),(i)
# We will export matrices of S11, S12, S21 and S22 parameters as a numpy array
#  -> we need to specify the structure of the tensor (use the names seen in the CST Studio Suite)
structure = np.array([['S1,1', 'S1,2'], ['S2,1', 'S2,2']])
s_tensor_exporter = CustomSTensor(results, structure)

f = s_tensor_exporter.get_frequencies()
s_tensor = s_tensor_exporter.get_tensor()

# Be aware the indices in the resulting matrices start from 0, not 1 !
s11 = s_tensor[0, 0, :]
s12 = s_tensor[0, 1, :]
s21 = s_tensor[1, 0, :]
s22 = s_tensor[1, 1, :]

plt.plot(f, 20*np.log10(np.abs(s11)))
plt.plot(f, 20*np.log10(np.abs(s12)))
plt.plot(f, 20*np.log10(np.abs(s21)))
plt.plot(f, 20*np.log10(np.abs(s22)))
plt.legend(['S11', 'S12', 'S21', 'S22'])
plt.ylabel('S-Parameter (dB)')
plt.xlabel('Frequency (GHz)')
plt.show()