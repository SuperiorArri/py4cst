from . import Project
from . import ComObjectWrapper
from . import w32com
import numpy as np

class Boundary(ComObjectWrapper):
    BOUNDARY_ELECTRIC = 'electric'
    BOUNDARY_MAGNETIC = 'magnetic'
    BOUNDARY_TANGENTIAL = 'tangential'
    BOUNDARY_NORMAL = 'normal'
    BOUNDARY_OPEN = 'open'
    BOUNDARY_EXPANDED_OPEN = 'expanded open'
    BOUNDARY_PERIODIC = 'periodic'
    BOUNDARY_CONDUCTING_WALL = 'conducting wall'
    BOUNDARY_UNIT_CELL = 'unit cell'

    SYMMETRY_ELECTRIC = 'electric'
    SYMMETRY_MAGNETIC = 'magnetic'
    SYMMETRY_NONE = 'none'

    POTENTIAL_NONE = 'none'
    POTENTIAL_FIXED = 'fixed'
    POTENTIAL_FLOATING = 'floating'

    THERMAL_BOUNDARY_ISOTHERMAL = 'isothermal'
    THERMAL_BOUNDARY_ADIABATIC = 'adiabatic'
    THERMAL_BOUNDARY_OPEN = 'open'
    THERMAL_BOUNDARY_EXPANDED_OPEN = 'expanded open'

    THERMAL_SYMMETRY_ISOTHERMAL = 'isothermal'
    THERMAL_SYMMETRY_ADIABATIC = 'adiabatic'
    THERMAL_SYMMETRY_NONE = 'none'
    THERMAL_SYMMETRY_EXPANDED_OPEN = 'expanded open'

    TEMPERATURE_NONE = 'none'
    TEMPERATURE_FIXED = 'fixed'
    TEMPERATURE_FLOATING = 'floating'

    DISTANCE_FRACTION = 'Fraction'
    DISTANCE_ABSOLUTE = 'Absolute'

    DISTANCE_REF_FREQ_CENTER = 'Center'
    DISTANCE_REF_FREQ_CENTER_AND_MONITORS = 'CenterNMonitors'
    DISTANCE_REF_FREQ_USER = 'User'

    DIRECTION_OUTWARD = 'outward'
    DIRECTION_INWARD = 'inward'

    def __init__(self, project) -> None:
        self.project: Project = project
        self.com_object = project.com_object.Boundary

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_type_x_min(self, boundary_type: str):
        self.invoke_method('Xmin', boundary_type)

    def set_type_x_max(self, boundary_type: str):
        self.invoke_method('Xmax', boundary_type)

    def set_types_x(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_x_min(min_boudary_type)
        self.set_type_x_max(max_boudary_type)

    def set_type_y_min(self, boundary_type: str):
        self.invoke_method('Ymin', boundary_type)

    def set_type_y_max(self, boundary_type: str):
        self.invoke_method('Ymax', boundary_type)

    def set_types_y(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_y_min(min_boudary_type)
        self.set_type_y_max(max_boudary_type)

    def set_type_z_min(self, boundary_type: str):
        self.invoke_method('Zmin', boundary_type)

    def set_type_z_max(self, boundary_type: str):
        self.invoke_method('Zmax', boundary_type)

    def set_types_z(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_z_min(min_boudary_type)
        self.set_type_z_max(max_boudary_type)

    def set_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_types_x(x_min, x_max)
        self.set_types_y(y_min, y_max)
        self.set_types_z(z_min, z_max)

    def get_type_x_min(self) -> str:
        return self.invoke_method('GetXmin')

    def get_type_x_max(self) -> str:
        return self.invoke_method('GetXmax')

    def get_type_y_min(self) -> str:
        return self.invoke_method('GetYmin')

    def get_type_y_max(self) -> str:
        return self.invoke_method('GetYmax')

    def get_type_z_min(self) -> str:
        return self.invoke_method('GetZmin')

    def get_type_z_max(self) -> str:
        return self.invoke_method('GetZmax')

    def set_symmetry_x(self, symmetry_type: str):
        self.invoke_method('Xsymmetry', symmetry_type)

    def set_symmetry_y(self, symmetry_type: str):
        self.invoke_method('Ysymmetry', symmetry_type)

    def set_symmetry_z(self, symmetry_type: str):
        self.invoke_method('Zsymmetry', symmetry_type)

    def set_symmetries(self, x_type: str, y_type: str, z_type: str):
        self.set_symmetry_x(x_type)
        self.set_symmetry_y(y_type)
        self.set_symmetry_z(z_type)

    def get_symmetry_x(self) -> str:
        return self.invoke_method('GetXSymmetry')

    def get_symmetry_y(self) -> str:
        return self.invoke_method('GetYSymmetry')

    def get_symmetry_z(self) -> str:
        return self.invoke_method('GetZSymmetry')

    def set_apply_in_all_directions(self, flag: bool = True):
        self.invoke_method('ApplyInAllDirections', flag)

    def set_potential_type_x_min(self, potential_type: str):
        self.invoke_method('XminPotentialType', potential_type)

    def set_potential_type_x_max(self, potential_type: str):
        self.invoke_method('XmaxPotentialType', potential_type)

    def set_potential_types_x(self, min_type: str, max_type: str):
        self.set_potential_type_x_min(min_type)
        self.set_potential_type_x_max(max_type)

    def set_potential_type_y_min(self, potential_type: str):
        self.invoke_method('YminPotentialType', potential_type)

    def set_potential_type_y_max(self, potential_type: str):
        self.invoke_method('YmaxPotentialType', potential_type)

    def set_potential_types_y(self, min_type: str, max_type: str):
        self.set_potential_type_y_min(min_type)
        self.set_potential_type_y_max(max_type)

    def set_potential_type_z_min(self, potential_type: str):
        self.invoke_method('ZminPotentialType', potential_type)

    def set_potential_type_z_max(self, potential_type: str):
        self.invoke_method('ZmaxPotentialType', potential_type)

    def set_potential_types_z(self, min_type: str, max_type: str):
        self.set_potential_type_z_min(min_type)
        self.set_potential_type_z_max(max_type)

    def set_potential_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_potential_types_x(x_min, x_max)
        self.set_potential_types_y(y_min, y_max)
        self.set_potential_types_z(z_min, z_max)

    def set_potential_x_min(self, potential: float):
        self.invoke_method('XminPotential', potential)

    def set_potential_x_max(self, potential: float):
        self.invoke_method('XmaxPotential', potential)

    def set_potentials_x(self, min_potential: float, max_potential: float):
        self.set_potential_x_min(min_potential)
        self.set_potential_x_max(max_potential)

    def set_potential_y_min(self, potential: float):
        self.invoke_method('YminPotential', potential)

    def set_potential_y_max(self, potential: float):
        self.invoke_method('YmaxPotential', potential)

    def set_potentials_y(self, min_potential: float, max_potential: float):
        self.set_potential_y_min(min_potential)
        self.set_potential_y_max(max_potential)

    def set_potential_z_min(self, potential: float):
        self.invoke_method('ZminPotential', potential)

    def set_potential_z_max(self, potential: float):
        self.invoke_method('ZmaxPotential', potential)

    def set_potentials_z(self, min_potential: float, max_potential: float):
        self.set_potential_z_min(min_potential)
        self.set_potential_z_max(max_potential)

    def set_potentials(
            self, x_min: float, x_max: float, y_min: float, y_max: float,
            z_min: float, z_max: float):
        self.set_potentials_x(x_min, x_max)
        self.set_potentials_y(y_min, y_max)
        self.set_potentials_z(z_min, z_max)

    def set_thermal_type_x_min(self, thermal_type: str):
        self.invoke_method('XminThermal', thermal_type)

    def set_thermal_type_x_max(self, thermal_type: str):
        self.invoke_method('XmaxThermal', thermal_type)

    def set_thermal_types_x(self, min_type: str, max_type: str):
        self.set_thermal_type_x_min(min_type)
        self.set_thermal_type_x_max(max_type)

    def set_thermal_type_y_min(self, thermal_type: str):
        self.invoke_method('YminThermal', thermal_type)

    def set_thermal_type_y_max(self, thermal_type: str):
        self.invoke_method('YmaxThermal', thermal_type)

    def set_thermal_types_y(self, min_type: str, max_type: str):
        self.set_thermal_type_y_min(min_type)
        self.set_thermal_type_y_max(max_type)

    def set_thermal_type_z_min(self, thermal_type: str):
        self.invoke_method('ZminThermal', thermal_type)

    def set_thermal_type_z_max(self, thermal_type: str):
        self.invoke_method('ZmaxThermal', thermal_type)

    def set_thermal_types_z(self, min_type: str, max_type: str):
        self.set_thermal_type_z_min(min_type)
        self.set_thermal_type_z_max(max_type)

    def set_thermal_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_thermal_types_y(y_min, y_max)
        self.set_thermal_types_x(x_min, x_max)
        self.set_thermal_types_z(z_min, z_max)

    def set_thermal_symmetry_x(self, symmetry_type: str):
        self.invoke_method('XsymmetryThermal', symmetry_type)

    def set_thermal_symmetry_y(self, symmetry_type: str):
        self.invoke_method('YsymmetryThermal', symmetry_type)

    def set_thermal_symmetry_z(self, symmetry_type: str):
        self.invoke_method('ZsymmetryThermal', symmetry_type)

    def set_thermal_symmetries(self, x: str, y: str, z: str):
        self.set_thermal_symmetry_x(x)
        self.set_thermal_symmetry_y(y)
        self.set_thermal_symmetry_z(z)

    def get_thermal_symmetry_x(self) -> str:
        return self.invoke_method('GetXSymmetryThermal')

    def get_thermal_symmetry_y(self) -> str:
        return self.invoke_method('GetYSymmetryThermal')

    def get_thermal_symmetry_z(self) -> str:
        return self.invoke_method('GetZSymmetryThermal')

    def set_temperature_type_x_min(self, temperature_type: str):
        self.invoke_method('XminTemperatureType', temperature_type)

    def set_temperature_type_x_max(self, temperature_type: str):
        self.invoke_method('XmaxTemperatureType', temperature_type)

    def set_temperature_types_x(self, min_type: str, max_type: str):
        self.set_temperature_type_x_min(min_type)
        self.set_temperature_type_x_max(max_type)

    def set_temperature_type_y_min(self, temperature_type: str):
        self.invoke_method('YminTemperatureType', temperature_type)

    def set_temperature_type_y_max(self, temperature_type: str):
        self.invoke_method('YmaxTemperatureType', temperature_type)

    def set_temperature_types_y(self, min_type: str, max_type: str):
        self.set_temperature_type_y_min(min_type)
        self.set_temperature_type_y_max(max_type)

    def set_temperature_type_z_min(self, temperature_type: str):
        self.invoke_method('ZminTemperatureType', temperature_type)

    def set_temperature_type_z_max(self, temperature_type: str):
        self.invoke_method('ZmaxTemperatureType', temperature_type)

    def set_temperature_types_z(self, min_type: str, max_type: str):
        self.set_temperature_type_z_min(min_type)
        self.set_temperature_type_z_max(max_type)

    def set_temperature_types(
            self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_temperature_types_x(x_min, x_max)
        self.set_temperature_types_y(y_min, y_max)
        self.set_temperature_types_z(z_min, z_max)

    def set_temperature_x_min(self, temperature: float):
        self.invoke_method('XminTemperature', temperature)

    def set_temperature_x_max(self, temperature: float):
        self.invoke_method('XmaxTemperature', temperature)

    def set_temperatures_x(self, min_temperature: float, max_temperature: float):
        self.set_temperature_x_min(min_temperature)
        self.set_temperature_x_max(max_temperature)

    def set_temperature_y_min(self, temperature: float):
        self.invoke_method('YminTemperature', temperature)

    def set_temperature_y_max(self, temperature: float):
        self.invoke_method('YmaxTemperature', temperature)

    def set_temperatures_y(self, min_temperature: float, max_temperature: float):
        self.set_temperature_y_min(min_temperature)
        self.set_temperature_y_max(max_temperature)

    def set_temperature_z_min(self, temperature: float):
        self.invoke_method('ZminTemperature', temperature)

    def set_temperature_z_max(self, temperature: float):
        self.invoke_method('ZmaxTemperature', temperature)

    def set_temperatures_z(self, min_temperature: float, max_temperature: float):
        self.set_temperature_z_min(min_temperature)
        self.set_temperature_z_max(max_temperature)

    def set_temperatures(
            self, x_min: float, x_max: float, y_min: float, y_max: float,
            z_min: float, z_max: float):
        self.set_temperatures_x(x_min, x_max)
        self.set_temperatures_y(y_min, y_max)
        self.set_temperatures_z(z_min, z_max)

    def get_calculation_box(self):
        x_min = w32com.create_ref_double()
        x_max = w32com.create_ref_double()
        y_min = w32com.create_ref_double()
        y_max = w32com.create_ref_double()
        z_min = w32com.create_ref_double()
        z_max = w32com.create_ref_double()
        self.invoke_method('GetCalculationBox', x_min, x_max, y_min, y_max, z_min, z_max)
        return (x_min.value, x_max.value, y_min.value, y_max.value, z_min.value, z_max.value)

    def get_structure_box(self):
        x_min = w32com.create_ref_double()
        x_max = w32com.create_ref_double()
        y_min = w32com.create_ref_double()
        y_max = w32com.create_ref_double()
        z_min = w32com.create_ref_double()
        z_max = w32com.create_ref_double()
        self.invoke_method('GetStructureBox', x_min, x_max, y_min, y_max, z_min, z_max)
        return (x_min.value, x_max.value, y_min.value, y_max.value, z_min.value, z_max.value)

    def set_number_of_layers(self, count: int):
        self.invoke_method('Layer', count)

    def set_minimum_lines_distance(self, distance: float):
        self.invoke_method('MinimumLinesDistance', distance)

    def set_minimum_distance_type(self, distance_type: str):
        self.invoke_method('MinimumDistanceType', distance_type)

    def set_absolute_distance(self, distance: float):
        self.invoke_method('SetAbsoluteDistance', distance)

    def set_minimum_distance_reference_frequency_type(self, freq_type: str):
        self.invoke_method('MinimumDistanceReferenceFrequencyType', freq_type)

    def set_minimum_distance_per_wavelength(self, distance: float):
        self.invoke_method('MinimumDistancePerWavelength', distance)

    def set_frequency_for_minimum_distance(self, freq: float):
        self.invoke_method('FrequencyForMinimumDistance', freq)

    def set_period_shift_x_deg(self, angle_deg: float):
        self.invoke_method('XPeriodicShift', angle_deg)

    def set_period_shift_x_rad(self, angle_rad: float):
        self.set_period_shift_x_deg(np.rad2deg(angle_rad))

    def set_period_shift_y_deg(self, angle_deg: float):
        self.invoke_method('YPeriodicShift', angle_deg)

    def set_period_shift_y_rad(self, angle_rad: float):
        self.set_period_shift_y_deg(np.rad2deg(angle_rad))

    def set_period_shift_z_deg(self, angle_deg: float):
        self.invoke_method('ZPeriodicShift', angle_deg)

    def set_period_shift_z_rad(self, angle_rad: float):
        self.set_period_shift_z_deg(np.rad2deg(angle_rad))

    def set_periodic_use_constant_angles(self, flag: bool = True):
        self.invoke_method('PeriodicUseConstantAngles', flag)

    def set_periodic_boundary_angles_deg(self, theta_deg: float, phi_deg: float):
        self.invoke_method('SetPeriodicBoundaryAngles', theta_deg, phi_deg)

    def set_periodic_boundary_angles_rad(self, theta_rad: float, phi_rad: float):
        self.set_periodic_boundary_angles_deg(np.rad2deg(theta_rad), np.rad2deg(phi_rad))

    def set_periodic_boundary_angles_direction(self, direction: str):
        self.invoke_method('SetPeriodicBoundaryAnglesDirection', direction)

    def get_unit_cell_scan_angle(self):
        theta = w32com.create_ref_double()
        phi = w32com.create_ref_double()
        dir = w32com.create_ref_long()
        self.invoke_method('GetUnitCellScanAngle', theta, phi, dir)
        dir_str = self.DIRECTION_OUTWARD if dir.value == 1 else self.DIRECTION_INWARD
        return (theta.value, phi.value, dir_str)

    def set_unit_cells_distance_dir1(self, distance: float):
        self.invoke_method('UnitCellDs1', distance)

    def set_unit_cells_distance_dir2(self, distance: float):
        self.invoke_method('UnitCellDs2', distance)

    def get_unit_cells_distance_dir1(self) -> float:
        return self.invoke_method('GetUnitCellDs1')

    def get_unit_cells_distance_dir2(self) -> float:
        return self.invoke_method('GetUnitCellDs2')

    def set_unit_cells_angle_deg(self, angle_deg: float):
        self.invoke_method('UnitCellAngle', angle_deg)

    def set_unit_cells_angle_rad(self, angle_rad: float):
        self.set_unit_cells_angle_deg(np.rad2deg(angle_rad))

    def get_unit_cells_angle_deg(self) -> float:
        return self.invoke_method('GetUnitCellAngle')

    def get_unit_cells_angle_rad(self) -> float:
        return np.deg2rad(self.get_unit_cells_angle_deg())

    def set_unit_cells_origin(self, pos_dir1: float, pos_dir2: float):
        self.invoke_method('UnitCellOrigin', pos_dir1, pos_dir2)

    def set_unit_cells_fit_to_bounding_box(self, flag: bool = True):
        self.invoke_method('UnitCellFitToBoundingBox', flag)