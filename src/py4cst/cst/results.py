from .. import installation_util
from . import ResultModule
from typing import Optional, Union
import os.path

class Results:
    def __init__(
            self, project_file_path: str,
            version_or_install_dir: Optional[Union[int,str]] = None,
            allow_interactive: bool = True) -> None:
        installation_util.load_win_cst_python_lib(version_or_install_dir)
        import cst.results # type: ignore
        project_file_path = os.path.abspath(project_file_path)
        self.proj_file = cst.results.ProjectFile(project_file_path, allow_interactive)

    def get_3d(self) -> ResultModule:
        return ResultModule(self.proj_file.get_3d())

    def get_schematic(self) -> ResultModule:
        return ResultModule(self.proj_file.get_schematic())
