from . import IHistoryListProvider
from typing import Optional, Union

class HistoryItem:
    def __init__(
            self, object_name: Optional[str], method_name: str,
            *method_args: Union[str, int, float, bool]) -> None:
        self.object_name = object_name
        self.method_name = method_name
        self.method_args = list(method_args)

    def to_vba_code(self) -> str:
        obj_name = '' if self.object_name is None else f'{self.object_name}.'
        args = [f'"{arg}"' if isinstance(arg, str) else str(arg) for arg in self.method_args]
        args_str = ", ".join(args)
        return f'{obj_name}{self.method_name}({args_str})'

class HistoryListGenerator:
    def __init__(self, history_list_provider: IHistoryListProvider) -> None:
        self.names = {}
        self.history: list[HistoryItem] = []
        self.history_list_provider = history_list_provider

    def invoke_method(self, object_name, method_name, *args) -> None:
        self.generate_item(HistoryItem(object_name, method_name, *args))

    def cache_method(self, object_name, method_name, *args) -> None:
        self.history.append(HistoryItem(object_name, method_name, *args))

    def generate_cache(self):
        for item in self.history:
            self.generate_item(item)

    def generate_item(self, item: HistoryItem):
        name = '' if item.object_name is None else f'{item.object_name}.'
        name += item.method_name
        id = self.names.get(name, 0)
        self.names[name] = id + 1
        name += f':{id}'
        self.history_list_provider.add_to_history(name, item.to_vba_code())

class IHistoryListGeneratorProvider:
    def get_history_list_generator(self) -> HistoryListGenerator:
        pass