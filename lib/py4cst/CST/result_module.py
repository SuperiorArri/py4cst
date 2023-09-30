from . import ResultItem

class ResultModule:
    def __init__(self, native_obj) -> None:
        self.native_obj = native_obj

    def get_all_run_ids(self, max_mesh_passes_only: bool = True) -> list[int]:
        return self.native_obj.get_all_run_ids(max_mesh_passes_only)

    def get_parameter_combination(self, run_id: int) -> dict:
        return self.native_obj.get_parameter_combination(run_id)

    def get_result_item(
            self, tree_path: str, run_id: int = 0, load_impedances: bool = True) -> ResultItem:
        return ResultItem(self.native_obj.get_result_item(tree_path, run_id, load_impedances))

    def get_run_ids(self, tree_path: str, skip_non_parametric: bool = False) -> list[int]:
        return self.native_obj.get_run_ids(tree_path, skip_non_parametric)

    def get_tree_items(self, item_filter: str = '0D/1D') -> list[str]:
        return self.native_obj.get_tree_items(item_filter)