from ..cst import Results
from . import SParameter
import numpy as np

class CustomSTensor:
    def __init__(self, results: Results, structure: np.ndarray) -> None:
        self.s_param = SParameter(results)
        self.structure = structure

    def get_num_samples(self, run_id: int = 0) -> int:
        self.s_param.select_by_name(self.__get_first_structure_item(), run_id)
        return self.s_param.get_num_samples()

    def get_frequencies(self, run_id: int = 0) -> list[float]:
        self.s_param.select_by_name(self.__get_first_structure_item(), run_id)
        return self.s_param.get_frequencies()

    def get_tensor(self, run_id: int = 0):
        s_tensor = self.__prealloc_tensor(run_id)
        for i,v in np.ndenumerate(self.structure):
            self.s_param.select_by_name(v, run_id)
            s_tensor[i] = self.s_param.get_values()
        return s_tensor

    def __get_first_structure_item(self):
        return np.ravel(self.structure)[0]

    def __prealloc_tensor(self, run_id):
        num_samples = self.get_num_samples(run_id)
        return np.zeros((*self.structure.shape, num_samples), dtype=complex)
