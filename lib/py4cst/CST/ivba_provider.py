from . import HistoryListGenerator, VBATypeName, IQuietModeController
from typing import Optional, Union

class IVBAProvider:
    def get_history_list_generator(self) -> HistoryListGenerator:
        pass

    def run_vba(self, vba_code: str) -> bool:
        pass

    def invoke_function(self, function_name: str, *args: Union[str, int, float, bool]) -> bool:
        pass

    def invoke_method(
            self, object_name: str, function_name: str, *args: Union[str, int, float, bool]):
        pass

    def query_vba(self, vba_code: str) -> Optional[str]:
        pass

    def query_function(
            self, function_name: str, *args: Union[str, int, float, bool]) -> Optional[str]:
        pass

    def query_method(
            self, object_name: str, function_name: str,
            *args: Union[str, int, float, bool]) -> Optional[str]:
        pass

    def query_function_t(
            self, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]) -> tuple:
        pass

    def query_method_t(
            self, object_name: str, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]) -> tuple:
        pass

    def get_quiet_mode_controller(self) -> IQuietModeController:
        pass