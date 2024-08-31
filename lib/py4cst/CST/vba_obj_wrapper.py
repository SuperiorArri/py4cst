from . import IVBAProvider, VBATypeName
from typing import Optional, Union

class VBAObjWrapper:
    def __init__(self, vbap: IVBAProvider, native_obj_name: str) -> None:
        self.history_list = vbap.get_history_list_generator()
        self.vbap = vbap
        self.native_obj_name = native_obj_name

    def record_method(self, name: str, *args: Union[str, int, float, bool]) -> None:
        self.history_list.invoke_method(self.native_obj_name, name, *args)

    def cache_method(self, name: str, *args: Union[str, int, float, bool]) -> None:
        self.history_list.cache_method(self.native_obj_name, name, *args)

    def flush_cache(self, item_name: Optional[str]) -> None:
        self.history_list.flush_cache(item_name)

    def invoke_method(self, name: str, *args: Union[str, int, float, bool]) -> None:
        self.vbap.invoke_method(self.native_obj_name, name, *args)

    def query_method_str(self, name: str, *args: Union[str, int, float, bool]) -> str:
        return self.vbap.query_method(self.native_obj_name, name, *args)

    def query_method_int(self, name: str, *args: Union[str, int, float, bool]) -> int:
        return int(self.query_method_str(name, *args))

    def query_method_float(self, name: str, *args: Union[str, int, float, bool]) -> float:
        return float(self.query_method_str(name, *args))

    def query_method_bool(self, name: str, *args: Union[str, int, float, bool]) -> bool:
        return self.query_method_str(name, *args) != 'False'

    def query_method_t(
            self, name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]) -> tuple:
        return self.vbap.query_method_t(self.native_obj_name, name, return_type, *args)