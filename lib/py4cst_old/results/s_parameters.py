from ..CST import Result1DComplex
from ..CST import ResultTree
from ..CST import ResultTreeItem
import numpy as np
import re

class SParameters:
    ITEM_ROOT = '1D Results\\S-Parameters'
    ITEM_REGEX = '^1D Results\\\\S-Parameters\\\\S(\d+),(\d+)$'
    ITEM_TEMPL = '1D Results\\S-Parameters\\S{},{}'

    def __init__(self, result_tree: ResultTree) -> None:
        self.result_tree = result_tree
        self.project = result_tree.project
        self.com_object = result_tree.com_object

    def are_available(self):
        return self.result_tree.has_item(SParameters.ITEM_ROOT) and self.__has_at_least_one_result()

    def get_available_indices(self):
        res = map(SParameters.get_indices_from_item_name, self.__get_available_items())
        res = SParameters.__remove_none_values(res)
        return res

    def get_by_indices(self, indices):
        if indices in self.get_available_indices():
            return SParameter(self, indices)
        return None

    def get_all(self):
        map_fn = lambda indices: SParameter(self, indices)
        return list(map(map_fn, self.get_available_indices()))

    def get_matrix_size(self):
        return self.get_available_indices()[-1]

    def get_matrix_at_index(self, index: int, result_id = None):
        s_matrix = np.zeros(shape=self.get_matrix_size(), dtype=np.complex128)
        for i in range(s_matrix.shape[0]):
            for j in range(s_matrix.shape[1]):
                s_matrix[i, j] = SParameter(self, (i+1, j+1)).get_value_at_index(index, result_id)
        return s_matrix

    def get_matrix_at_frequency(self, frequency: float, result_id = None):
        index = SParameter(self, (1, 1)).get_nearest_frequency_index(frequency)
        return self.get_matrix_at_index(index, result_id)

    def get_frequencies(self, result_id = None):
        return SParameter(self, (1, 1)).get_frequencies(result_id)

    def get_num_frequencies(self, result_id = None):
        return SParameter(self, (1, 1)).get_num_frequencies(result_id)

    def get_frequency_at_index(self, index: int, result_id = None):
        return SParameter(self, (1, 1)).get_frequency_at_index(index, result_id)

    def get_nearest_frequency_index(self, frequency: float, result_id = None):
        return SParameter(self, (1, 1)).get_nearest_frequency_index(frequency, result_id)

    def get_matrices(self, result_id = None):
        matrix_size = self.get_matrix_size()
        num_points = self.get_num_frequencies(result_id)
        s_matrix = np.zeros(shape=(num_points, matrix_size[0], matrix_size[1]), dtype=np.complex128)
        for i in range(s_matrix.shape[1]):
            for j in range(s_matrix.shape[2]):
                s_matrix[:, i, j] = SParameter(self, (i+1, j+1)).get_values(result_id)
        return s_matrix

    def __has_at_least_one_result(self):
        return len(self.result_tree.get_first_child_name(SParameters.ITEM_ROOT)) > 0

    def __get_available_items(self):
        res = []
        child_name = self.result_tree.get_first_child_name(SParameters.ITEM_ROOT)
        while len(child_name) > 0:
            res.append(child_name)
            child_name = self.result_tree.get_next_item_name(child_name)
        return res

    def __remove_none_values(arr):
        return list(filter(lambda x: x is not None, arr))

    def get_indices_from_item_name(name):
        x = re.search(SParameters.ITEM_REGEX, name)
        return None if x is None else (int(x.group(1)), int(x.group(2)))

    def get_item_name_from_indices(indices):
        return SParameters.ITEM_TEMPL.format(int(indices[0]), int(indices[1]))

    def get_z_matrix(s_matrix, z_ref: complex = 50):
        E = np.eye(s_matrix.shape[0])
        sqrt_z = E*np.sqrt(z_ref)
        return sqrt_z@np.linalg.solve(E-s_matrix, E+s_matrix)@sqrt_z

    def get_z_matrices(s_matrices, z_ref: complex = 50):
        return np.array(list(map(lambda x: SParameters.get_z_matrix(x, z_ref), s_matrices)))

class SParameter:
    def __init__(self, s_parameters: SParameters, indices: tuple[int, int]) -> None:
        self.s_parameters = s_parameters
        self.indices = indices

    def get_result_ids(self):
        item_name = SParameters.get_item_name_from_indices(self.indices)
        return ResultTreeItem(self.s_parameters.result_tree).get_result_ids(item_name)

    def get_result(self, result_id = None):
        if result_id is None:
            result_id = self.get_result_ids()[0]
        obj = self.__get_result_obj(result_id)
        return Result1DComplex(obj)

    def get_num_frequencies(self, result_id = None) -> int:
        return self.get_result(result_id).get_num_elements()

    def get_frequencies(self, result_id = None):
        if result_id is None:
            result_id = self.get_result_ids()[0]
        return self.get_result(result_id).get_x_values()

    def get_frequency_at_index(self, index: int, result_id = None):
        return self.get_result(result_id).get_x_at(index)

    def get_nearest_frequency_index(self, frequency: float, result_id = None):
        freqs = self.get_frequencies(result_id)
        if frequency < freqs[0] or frequency > freqs[-1]:
            return None
        return np.abs(freqs - frequency).argmin()

    def get_values(self, result_id = None):
        if result_id is None:
            result_id = self.get_result_ids()[0]
        return self.get_result(result_id).get_y_values()

    def get_value_at_index(self, index: int, result_id = None):
        return self.get_result(result_id).get_y_at(index)

    def get_value_at_frequency(self, frequency: float, result_id = None):
        index = self.get_nearest_frequency_index(frequency)
        return self.get_value_at_index(index, result_id)

    def __get_result_obj(self, result_id):
        item_name = SParameters.get_item_name_from_indices(self.indices)
        return ResultTreeItem(self.s_parameters.result_tree).get_result(item_name, result_id)