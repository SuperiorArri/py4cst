from ..CST import Results, ResultItem
from typing import Optional

def __raise_error_no_selected():
    raise RuntimeError('No S-Parameters selected!')

class SParameter:
    ITEM_ROOT = '1D Results\\S-Parameters'

    def __init__(self, results: Results) -> None:
        self.results = results.get_3d()
        self.result_item: Optional[ResultItem] = None

    def select_by_name(
            self, s_params_name: str, run_id: int = 0, load_impedances: bool = True) -> None:
        self.result_item = self.results.get_result_item(
            f'{SParameter.ITEM_ROOT}\\{s_params_name}', run_id, load_impedances)

    def select_by_indices(
            self, indices: tuple[int, int], run_id: int = 0, load_impedances: bool = True) -> None:
        self.result_item = self.results.get_result_item(
            f'{SParameter.ITEM_ROOT}\\S{indices[0]},{indices[1]}', run_id, load_impedances)

    def get_num_samples(self) -> int:
        if self.result_item is None:
            __raise_error_no_selected()
        else:
            return self.result_item.get_length()

    def get_frequencies(self) -> list[float]:
        if self.result_item is None:
            __raise_error_no_selected()
        else:
            return self.result_item.get_x_data()

    def get_values(self) -> list[complex]:
        if self.result_item is None:
            __raise_error_no_selected()
        else:
            return self.result_item.get_y_data()
