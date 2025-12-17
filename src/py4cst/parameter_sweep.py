from .cst import Parameters
from typing import Callable, Union

numeric_value = Union[float, int]

class ParameterSweep:
    def __init__(self, project_params: Parameters) -> None:
        self.project_params = project_params
        self.parameters = {}
        self.cb_before_it = None
        self.cb_after_it = None
        self.cb_start_sim = None
        self.curr_param_list = []
        self.param_indices = {}
        self.all_combinations_simulated = False

    def set_parameter(self, param_name: str, values: list[numeric_value]):
        self.parameters[param_name] = values

    def delete_parameter(self, param_name: str):
        self.parameters.pop(param_name)

    def set_callback_before_iteration(self, callback: Callable):
        self.cb_before_it = callback

    def set_callback_after_iteration(self, callback: Callable):
        self.cb_after_it = callback

    def set_callback_start_simulation(self, callback: Callable):
        self.cb_start_sim = callback

    def start(self):
        self.__prepare_sweep()
        while not self.all_combinations_simulated:
            self.__do_next_iteration()

    def __do_next_iteration(self):
        values = self.__get_current_param_values()
        self.__write_new_param_values(values)
        self.__call_before_it_cb_if_exists(values)
        self.__start_simulation()
        self.__call_after_it_cb_if_exists(values)
        self.__prepare_next_param_combination()

    def __prepare_sweep(self):
        self.__ensure_some_parameters_provided()
        self.all_combinations_simulated = False
        self.curr_param_list = list(self.parameters.keys())
        for param_name in self.curr_param_list:
            self.param_indices[param_name] = 0
        self.__ensure_cb_start_sim_provided()

    def __prepare_next_param_combination(self):
        self.__increment_param_index_if_exists(0)

    def __increment_param_index_if_exists(self, param_index: int):
            if param_index >= len(self.curr_param_list):
                self.all_combinations_simulated = True
            else:
                self.__increment_param_index(param_index)

    def __increment_param_index(self, param_index: int):
            param_name = self.curr_param_list[param_index]
            num_values = len(self.parameters[param_name])
            self.param_indices[param_name] += 1
            if self.param_indices[param_name] == num_values:
                self.param_indices[param_name] = 0
                self.__increment_param_index_if_exists(param_index + 1)

    def __get_current_param_values(self) -> dict[str, numeric_value]:
        values = {}
        for param_name in self.parameters:
            val_index = self.param_indices[param_name]
            param_values = self.parameters[param_name]
            values[param_name] = param_values[val_index]
        return values

    def __write_new_param_values(self, values: dict[str, numeric_value]):
        for param_name in values:
            self.project_params.store(param_name, values[param_name])

    def __start_simulation(self):
        self.cb_start_sim()

    def __call_before_it_cb_if_exists(self, param_values: dict[str, numeric_value]):
        if callable(self.cb_before_it):
            self.cb_before_it(param_values)

    def __call_after_it_cb_if_exists(self, param_values: dict[str, numeric_value]):
        if callable(self.cb_after_it):
            self.cb_after_it(param_values)

    def __ensure_cb_start_sim_provided(self):
        if not callable(self.cb_start_sim):
            raise RuntimeError('No run simulation callback provided.')

    def __ensure_some_parameters_provided(self):
        if not bool(self.parameters):
            raise RuntimeError('No parameters provided to sweep.')
