from . import IHistoryListProvider, IVBARuntime

class Modeler(IHistoryListProvider, IVBARuntime):
    def __init__(self, native_obj) -> None:
        self.native_obj = native_obj

    def abort_solver(self) -> None:
        self.native_obj.abort_solver()

    def run_vba(self, vba_code: str) -> bool:
        return self.native_obj._execute_vba_code(f'sub main\n{vba_code}\nend sub')

    def report_vba(self, vba_code: str) -> bool:
        return self.native_obj\
            ._execute_vba_code(f'sub main\nReportInformation({vba_code} & "")\nend sub')

    def add_to_history(self, header: str, vba_code: str) -> None:
        self.native_obj.add_to_history(header, vba_code)

    def full_history_rebuild(self) -> None:
        self.native_obj.full_history_rebuild(self)

    def get_active_solver_name(self) -> str:
        return self.native_obj.get_active_solver_name()

    def get_solver_run_info(self) -> dict:
        return self.native_obj.get_solver_run_info()

    def get_tree_items(self) -> list:
        return self.native_obj.get_tree_items()

    def is_solver_running(self) -> bool:
        return self.native_obj.is_solver_running()

    def pause_solver(self) -> None:
        self.native_obj.pause_solver()

    def resume_solver(self) -> None:
        self.native_obj.resume_solver()

    # blocking
    def run_solver(self) -> None:
        self.native_obj.run_solver()

    # non-blocking, use in combination with is_solver_running()
    def start_solver(self) -> None:
        self.native_obj.start_solver()