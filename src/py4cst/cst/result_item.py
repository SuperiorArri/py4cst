class ResultItem:
    def __init__(self, native_obj) -> None:
        self.native_obj = native_obj

    def get_data(self) -> list:
        return self.native_obj.get_data()

    def get_parameter_combination(self) -> dict:
        return self.native_obj.get_parameter_combination()

    def get_ref_imp_data(self) -> list:
        return self.native_obj.get_ref_imp_data()

    def get_x_data(self) -> list:
        return self.native_obj.get_xdata()

    def get_y_data(self) -> list:
        return self.native_obj.get_ydata()

    def get_length(self) -> int:
        return self.native_obj.length

    def get_run_id(self) -> int:
        return self.native_obj.run_id

    def get_title(self) -> str:
        return self.native_obj.title

    def get_tree_path(self) -> str:
        return self.native_obj.tree_path

    def get_x_label(self) -> str:
        return self.native_obj.xlabel

    def get_y_label(self) -> str:
        return self.native_obj.ylabel
