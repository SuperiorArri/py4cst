from ..CST import ResultTree
import re

#TODO: modify to use custom farfield names instead

class Farfields:
    ITEM_ROOT = 'Farfields'
    ITEM_REGEX = '^Farfields\\\\farfield \\(f=(\d+(?:\.\d*)?|\.\d+)\\) \\[(\d+)\\]$'
    ITEM_TEMPL = 'Farfields\\farfield (f={}) [{}]'

    def get_name(frequency: float, port: int = 1) -> str:
        return Farfields.get_item_name_from_params((frequency, port))

    def get_params_from_item_name(name):
        x = re.search(Farfields.ITEM_REGEX, name)
        return None if x is None else (float(x.group(1)), int(x.group(2)))

    def get_item_name_from_params(params):
        frequency = float(params[0]) if params[0] != int(params[0]) else int(params[0])
        port = int(params[1])
        return Farfields.ITEM_TEMPL.format(frequency, port)

    def __init__(self, result_tree: ResultTree) -> None:
        self.result_tree = result_tree
        self.project = result_tree.project
        self.com_object = result_tree.com_object

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def are_available(self):
        return self.result_tree.has_item(Farfields.ITEM_ROOT) and self.__has_at_least_one_result()

    def get_available_params(self):
        res = map(Farfields.get_params_from_item_name, self.__get_available_items())
        res = Farfields.__remove_none_values(res)
        return res

    def get_by_params(self, params):
        if params in self.get_available_params():
            return Farfield(self, params[0], params[1])
        return None

    def get_all(self):
        map_fn = lambda params: Farfield(self, params[0], params[1])
        return list(map(map_fn, self.get_available_params()))

    def __has_at_least_one_result(self):
        return len(self.result_tree.get_first_child_name(Farfields.ITEM_ROOT)) > 0

    def __get_available_items(self):
        res = []
        child_name = self.result_tree.get_first_child_name(Farfields.ITEM_ROOT)
        while len(child_name) > 0:
            res.append(child_name)
            child_name = self.result_tree.get_next_item_name(child_name)
        return res

    def __remove_none_values(arr):
        return list(filter(lambda x: x is not None, arr))

class Farfield:
    def __init__(self, farfields: Farfields, frequency: float, port: int) -> None:
        self.farfields = farfields
        self.project = farfields.project
        self.frequency = frequency
        self.port = port

    def select(self):
        item_name = Farfields.get_item_name_from_params((self.frequency, self.port))
        self.project.select_tree_item(item_name)

    def get_frequency(self) -> float:
        return self.frequency

    def get_port(self) -> int:
        return self.port