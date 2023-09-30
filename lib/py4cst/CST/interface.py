from .. import installation_util
from . import Project, IQuietModeController
from typing import Optional, Union
from enum import Enum
import os.path

class Interface(IQuietModeController):
    class StartMode(Enum):
        import cst.interface
        New = cst.interface.DesignEnvironment.StartMode.New
        ExistingOrNew = cst.interface.DesignEnvironment.StartMode.ExistingOrNew
        Existing = cst.interface.DesignEnvironment.StartMode.Existing

    def __init__(
            self, version_or_install_dir: Optional[Union[int,str]] = None,
            start_mode: StartMode = StartMode.ExistingOrNew) -> None:
        installation_util.load_win_cst_python_lib(version_or_install_dir)
        self.stored_quiet_mode = False
        self.__init_cst_interface(start_mode)
        self.set_quiet_mode(True)

    def __del__(self) -> None:
        # FIXME: here should be set_quiet_mode(False) but it doesn't work here (for an unknown
        # reason the connection to the Design Environment is lost)
        pass

    def __init_cst_interface(self, start_mode: StartMode = StartMode.New) -> None:
        import cst.interface
        self.design_env = cst.interface.DesignEnvironment(mode=start_mode.value)

    def store_quiet_mode(self) -> None:
        self.stored_quiet_mode = self.is_in_quiet_mode()

    def restore_quiet_mode(self) -> None:
        self.set_quiet_mode(self.stored_quiet_mode)

    def store_and_disable_quiet_mode(self) -> None:
        self.store_quiet_mode()
        self.set_quiet_mode(False)

    def store_and_enable_quiet_mode(self) -> None:
        self.store_quiet_mode()
        self.set_quiet_mode(True)

    def set_quiet_mode(self, enabled: bool = True) -> None:
        self.design_env.set_quiet_mode(enabled)

    def is_in_quiet_mode(self) -> bool:
        return self.design_env.in_quiet_mode()

    def get_open_projects(self) -> list[str]:
        return self.design_env.list_open_projects()

    def open_project(self, path: str) -> Project:
        return Project(self.design_env.open_project(os.path.abspath(path)), self)

    def get_active_project(self) -> Project:
        return Project(self.design_env.active_project(), self)

    def new_project(self, kind: Project.Kind) -> Project:
        return Project(self.design_env.new_project(kind.value), self)

    def new_cable_studio_project(self) -> Project:
        return Project(self.design_env.new_cs(), self)

    def new_design_studio_project(self) -> Project:
        return Project(self.design_env.new_ds(), self)

    def new_em_studio_project(self) -> Project:
        return Project(self.design_env.new_ems(), self)

    def new_filter_designer_3d_project(self) -> Project:
        return Project(self.design_env.new_fd3d(), self)

    def new_mphysics_studio_project(self) -> Project:
        return Project(self.design_env.new_mps(), self)

    def new_microwave_studio_project(self) -> Project:
        return Project(self.design_env.new_mws(), self)

    def new_pcb_studio_project(self) -> Project:
        return Project(self.design_env.new_pcbs(), self)

    def new_particle_studio_project(self) -> Project:
        return Project(self.design_env.new_ps(), self)

    def close(self) -> None:
        self.design_env.close()

    def get_version() -> str:
        import cst.interface
        return cst.interface.DesignEnvironment.version()