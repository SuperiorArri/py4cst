from ..CST import FarfieldPlot
from .farfields import Farfield
import numpy as np

class FarfieldExporter:
    def __init__(self) -> None:
        self.coord_system = FarfieldPlot.COORD_SYSTEM_SPHERICAL
        self.plot_mode = FarfieldPlot.PLOT_MODE_EFIELD
        self.points = [] # array of tuples(polar angle, lateral angle, radius)
        self.current_farfield: Farfield = None
        self.origin = (0.0, 0.0, 0.0)

    def set_coord_system(self, coord_system: str):
        self.coord_system = coord_system

    def set_plot_mode(self, plot_mode: str):
        self.plot_mode = plot_mode

    def set_origin(self, x: float, y: float, z: float):
        self.origin = (x, y, z)

    def set_points(self, points):
        self.points = points

    def clear_points(self):
        self.points = []

    def add_point(self, polar_angle: float, lateral_angle: float, radius: float):
        self.points.append((polar_angle, lateral_angle, radius))

    def get_points(self):
        return self.points

    def prepare(self, farfield: Farfield):
        self.current_farfield = farfield
        self.current_farfield.select()
        ffplot = FarfieldPlot(farfield.project)
        ffplot.reset()
        ffplot.set_plot_mode(self.plot_mode)
        ffplot.set_plot_type(FarfieldPlot.PLOT_TYPE_3D)
        ffplot.set_db_unit(FarfieldPlot.UNIT_CODE_0) # basic units
        ffplot.set_origin(self.origin[0], self.origin[1], self.origin[2])
        ffplot.set_scale_linear()
        ffplot.plot()
        self.__generate_points()
        self.__add_plot_points(ffplot, farfield.get_frequency())
        ffplot.calculate_list()

    def export_abs(self):
        self.current_farfield.select()
        ffplot = FarfieldPlot(self.current_farfield.project)
        return np.asarray(ffplot.get_list(self.__get_comp_abs()))

    def export_complex_theta(self):
        self.current_farfield.select()
        ffplot = FarfieldPlot(self.current_farfield.project)
        re_comp = np.asarray(ffplot.get_list(self.__get_comp_theta_re()))
        im_comp = np.asarray(ffplot.get_list(self.__get_comp_theta_im()))
        return re_comp + 1j*im_comp

    def export_complex_phi(self):
        self.current_farfield.select()
        ffplot = FarfieldPlot(self.current_farfield.project)
        re_comp = np.asarray(ffplot.get_list(self.__get_comp_phi_re()))
        im_comp = np.asarray(ffplot.get_list(self.__get_comp_phi_im()))
        return re_comp + 1j*im_comp

    def __generate_points(self): # virtual method
        pass

    def __add_plot_points(self, ffplot: FarfieldPlot, frequency):
        for point in self.points:
            ffplot.add_list_eval_point_deg(
                point[0], point[1], point[2], self.coord_system,
                FarfieldPlot.TF_TYPE_FREQUENCY, frequency)

    def __get_comp_abs(self):
        return '{} {}'.format(self.coord_system, FarfieldPlot.COMPLEX_COMP_ABS)

    def __get_comp_theta_re(self):
        return '{} {} {} {}'.format(
            self.coord_system, FarfieldPlot.POLARIZATION_LINEAR,
            FarfieldPlot.COMPONENT_THETA, FarfieldPlot.COMPLEX_COMP_RE)

    def __get_comp_theta_im(self):
        return '{} {} {} {}'.format(
            self.coord_system, FarfieldPlot.POLARIZATION_LINEAR,
            FarfieldPlot.COMPONENT_THETA, FarfieldPlot.COMPLEX_COMP_IM)

    def __get_comp_phi_re(self):
        return '{} {} {} {}'.format(
            self.coord_system, FarfieldPlot.POLARIZATION_LINEAR,
            FarfieldPlot.COMPONENT_PHI, FarfieldPlot.COMPLEX_COMP_RE)

    def __get_comp_phi_im(self):
        return '{} {} {} {}'.format(
            self.coord_system, FarfieldPlot.POLARIZATION_LINEAR,
            FarfieldPlot.COMPONENT_PHI, FarfieldPlot.COMPLEX_COMP_IM)
