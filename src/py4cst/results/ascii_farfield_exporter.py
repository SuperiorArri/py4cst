from ..cst import IVBAProvider
from ..cst.wrappers import FarfieldPlot
from .. import ffs
from typing import Optional, Tuple
import numpy as np
import pathlib
import time
import os.path

class ASCIIFarfieldExporter:
    DEFAULT_STEP_DEG: float = 5.0

    def __init__(self) -> None:
        self.coord_system = FarfieldPlot.CoordSystem.SPHERICAL
        self.plot_mode = FarfieldPlot.PlotMode.EFIELD
        self.polar_angle_step = ASCIIFarfieldExporter.DEFAULT_STEP_DEG
        self.lateral_angle_step = ASCIIFarfieldExporter.DEFAULT_STEP_DEG
        self.ascii_version = FarfieldPlot.AsciiVersion.V2010
        self.origin = (0.0, 0.0, 0.0)
        self.radius = 1.0
        self.current_ffs: Optional[ffs.Farfield] = None

    def set_coord_system(self, coord_system: str) -> None:
        self.coord_system = coord_system

    def set_plot_mode(self, plot_mode: str) -> None:
        self.plot_mode = plot_mode

    def set_polar_angle_step_deg(self, step_deg: float) -> None:
        self.polar_angle_step = step_deg

    def set_polar_angle_step_rad(self, step_rad: float) -> None:
        self.set_polar_angle_step_deg(np.rad2deg(step_rad))

    def set_lateral_angle_step_deg(self, step_deg: float) -> None:
        self.lateral_angle_step = step_deg

    def set_lateral_angle_step_rad(self, step_rad: float) -> None:
        self.set_lateral_angle_step_deg(np.rad2deg(step_rad))

    def set_ascii_version(self, ascii_version: str) -> None:
        self.ascii_version = ascii_version

    def set_origin(self, origin: Tuple[float, float, float]) -> None:
        self.origin = origin

    def set_radius(self, radius: float) -> None:
        self.radius = radius

    def prepare(self, vbap: IVBAProvider, farfield_name: str) -> None:
        self.vbap = vbap
        self.farfield_name = farfield_name
        self.__select_tree_item(farfield_name)
        self.__prepare_ffplot()
        self.__export_file()

    def get_abs(self) -> Optional[np.ndarray]:
        if self.current_ffs is None:
            return None
        return np.linalg.norm(self.get_complex_theta_phi(), axis=2)

    def get_complex_theta(self) -> Optional[np.ndarray]:
        if self.current_ffs is None:
            return None
        return self.current_ffs.get_theta_component()

    def get_complex_phi(self) -> Optional[np.ndarray]:
        if self.current_ffs is None:
            return None
        return self.current_ffs.get_phi_component()

    def get_complex_theta_phi(self) -> Optional[np.ndarray]:
        if self.current_ffs is None:
            return None
        return self.current_ffs.get_samples()

    def __select_tree_item(self, farfield_name: str) -> None:
        self.vbap.get_quiet_mode_controller().store_and_disable_quiet_mode()
        self.vbap.invoke_function('SelectTreeItem', f'Farfields\\{farfield_name}')
        self.vbap.get_quiet_mode_controller().restore_quiet_mode()

    def __get_tmp_path(self) -> str:
        return self.vbap.query_function('GetProjectPath', 'Temp')

    def __prepare_ffplot(self) -> None:
        ffplot = FarfieldPlot(self.vbap)
        ffplot.reset()
        ffplot.set_plot_mode(self.plot_mode)
        ffplot.set_plot_type(FarfieldPlot.PlotType.THREE_D)
        ffplot.set_coord_system(self.coord_system)
        ffplot.set_db_unit(FarfieldPlot.UnitCode.V_0) # basic units
        ffplot.set_origin(FarfieldPlot.Origin.FREE)
        ffplot.set_user_origin(self.origin)
        ffplot.set_polarization_type(FarfieldPlot.Polarization.LINEAR)
        ffplot.set_lock_steps(False)
        ffplot.set_theta_step_deg(self.polar_angle_step)
        ffplot.set_phi_step_deg(self.lateral_angle_step)
        ffplot.set_virtual_sphere_radius(self.radius)
        ffplot.set_scale_linear()
        ffplot.set_ascii_export_version(self.ascii_version)
        ffplot.plot()

    def __export_file(self) -> None:
        ffplot = FarfieldPlot(self.vbap)
        tmp_path = self.__get_tmp_path()
        timestamp = str(int(time.time()))
        file_path = os.path.join(tmp_path, f'tmp_ff_{timestamp}.ffs')
        ffplot.export_source_as_ascii(file_path)
        self.__load_ffs(file_path)
        os.remove(file_path)
        self.__remove_duplicate_samples()

    def __load_ffs(self, path) -> None:
        parser = ffs.Parser()
        parser.parse_string(pathlib.Path(path).read_text())
        self.current_ffs = parser.get_farfields()[0]

    def __remove_duplicate_samples(self) -> None:
        self.current_ffs.samples = self.current_ffs.samples[:,:-1,:]
