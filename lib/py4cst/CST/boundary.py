from . import IVBAProvider, VBAObjWrapper, VBATypeName
import numpy as np

class Boundary(VBAObjWrapper):
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

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Boundary')

    def set_type_x_min(self, boundary_type: str):
        self.record_method('Xmin', boundary_type)

    def set_type_x_max(self, boundary_type: str):
        self.record_method('Xmax', boundary_type)

    def set_types_x(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_x_min(min_boudary_type)
        self.set_type_x_max(max_boudary_type)

    def set_type_y_min(self, boundary_type: str):
        self.record_method('Ymin', boundary_type)

    def set_type_y_max(self, boundary_type: str):
        self.record_method('Ymax', boundary_type)

    def set_types_y(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_y_min(min_boudary_type)
        self.set_type_y_max(max_boudary_type)

    def set_type_z_min(self, boundary_type: str):
        self.record_method('Zmin', boundary_type)

    def set_type_z_max(self, boundary_type: str):
        self.record_method('Zmax', boundary_type)

    def set_types_z(self, min_boudary_type: str, max_boudary_type: str):
        self.set_type_z_min(min_boudary_type)
        self.set_type_z_max(max_boudary_type)

    def set_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_types_x(x_min, x_max)
        self.set_types_y(y_min, y_max)
        self.set_types_z(z_min, z_max)

    def get_type_x_min(self) -> str:
        return self.query_method_str('GetXmin')

    def get_type_x_max(self) -> str:
        return self.query_method_str('GetXmax')

    def get_type_y_min(self) -> str:
        return self.query_method_str('GetYmin')

    def get_type_y_max(self) -> str:
        return self.query_method_str('GetYmax')

    def get_type_z_min(self) -> str:
        return self.query_method_str('GetZmin')

    def get_type_z_max(self) -> str:
        return self.query_method_str('GetZmax')

    def set_symmetry_x(self, symmetry_type: str):
        self.record_method('Xsymmetry', symmetry_type)

    def set_symmetry_y(self, symmetry_type: str):
        self.record_method('Ysymmetry', symmetry_type)

    def set_symmetry_z(self, symmetry_type: str):
        self.record_method('Zsymmetry', symmetry_type)

    def set_symmetries(self, x_type: str, y_type: str, z_type: str):
        self.set_symmetry_x(x_type)
        self.set_symmetry_y(y_type)
        self.set_symmetry_z(z_type)

    def get_symmetry_x(self) -> str:
        return self.query_method_str('GetXSymmetry')

    def get_symmetry_y(self) -> str:
        return self.query_method_str('GetYSymmetry')

    def get_symmetry_z(self) -> str:
        return self.query_method_str('GetZSymmetry')

    def set_apply_in_all_directions(self, flag: bool = True):
        self.record_method('ApplyInAllDirections', flag)

    def set_potential_type_x_min(self, potential_type: str):
        self.record_method('XminPotentialType', potential_type)

    def set_potential_type_x_max(self, potential_type: str):
        self.record_method('XmaxPotentialType', potential_type)

    def set_potential_types_x(self, min_type: str, max_type: str):
        self.set_potential_type_x_min(min_type)
        self.set_potential_type_x_max(max_type)

    def set_potential_type_y_min(self, potential_type: str):
        self.record_method('YminPotentialType', potential_type)

    def set_potential_type_y_max(self, potential_type: str):
        self.record_method('YmaxPotentialType', potential_type)

    def set_potential_types_y(self, min_type: str, max_type: str):
        self.set_potential_type_y_min(min_type)
        self.set_potential_type_y_max(max_type)

    def set_potential_type_z_min(self, potential_type: str):
        self.record_method('ZminPotentialType', potential_type)

    def set_potential_type_z_max(self, potential_type: str):
        self.record_method('ZmaxPotentialType', potential_type)

    def set_potential_types_z(self, min_type: str, max_type: str):
        self.set_potential_type_z_min(min_type)
        self.set_potential_type_z_max(max_type)

    def set_potential_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_potential_types_x(x_min, x_max)
        self.set_potential_types_y(y_min, y_max)
        self.set_potential_types_z(z_min, z_max)

    def set_potential_x_min(self, potential: float):
        self.record_method('XminPotential', potential)

    def set_potential_x_max(self, potential: float):
        self.record_method('XmaxPotential', potential)

    def set_potentials_x(self, min_potential: float, max_potential: float):
        self.set_potential_x_min(min_potential)
        self.set_potential_x_max(max_potential)

    def set_potential_y_min(self, potential: float):
        self.record_method('YminPotential', potential)

    def set_potential_y_max(self, potential: float):
        self.record_method('YmaxPotential', potential)

    def set_potentials_y(self, min_potential: float, max_potential: float):
        self.set_potential_y_min(min_potential)
        self.set_potential_y_max(max_potential)

    def set_potential_z_min(self, potential: float):
        self.record_method('ZminPotential', potential)

    def set_potential_z_max(self, potential: float):
        self.record_method('ZmaxPotential', potential)

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
        self.record_method('XminThermal', thermal_type)

    def set_thermal_type_x_max(self, thermal_type: str):
        self.record_method('XmaxThermal', thermal_type)

    def set_thermal_types_x(self, min_type: str, max_type: str):
        self.set_thermal_type_x_min(min_type)
        self.set_thermal_type_x_max(max_type)

    def set_thermal_type_y_min(self, thermal_type: str):
        self.record_method('YminThermal', thermal_type)

    def set_thermal_type_y_max(self, thermal_type: str):
        self.record_method('YmaxThermal', thermal_type)

    def set_thermal_types_y(self, min_type: str, max_type: str):
        self.set_thermal_type_y_min(min_type)
        self.set_thermal_type_y_max(max_type)

    def set_thermal_type_z_min(self, thermal_type: str):
        self.record_method('ZminThermal', thermal_type)

    def set_thermal_type_z_max(self, thermal_type: str):
        self.record_method('ZmaxThermal', thermal_type)

    def set_thermal_types_z(self, min_type: str, max_type: str):
        self.set_thermal_type_z_min(min_type)
        self.set_thermal_type_z_max(max_type)

    def set_thermal_types(self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_thermal_types_y(y_min, y_max)
        self.set_thermal_types_x(x_min, x_max)
        self.set_thermal_types_z(z_min, z_max)

    def set_thermal_symmetry_x(self, symmetry_type: str):
        self.record_method('XsymmetryThermal', symmetry_type)

    def set_thermal_symmetry_y(self, symmetry_type: str):
        self.record_method('YsymmetryThermal', symmetry_type)

    def set_thermal_symmetry_z(self, symmetry_type: str):
        self.record_method('ZsymmetryThermal', symmetry_type)

    def set_thermal_symmetries(self, x: str, y: str, z: str):
        self.set_thermal_symmetry_x(x)
        self.set_thermal_symmetry_y(y)
        self.set_thermal_symmetry_z(z)

    def get_thermal_symmetry_x(self) -> str:
        return self.query_method_str('GetXSymmetryThermal')

    def get_thermal_symmetry_y(self) -> str:
        return self.query_method_str('GetYSymmetryThermal')

    def get_thermal_symmetry_z(self) -> str:
        return self.query_method_str('GetZSymmetryThermal')

    def set_temperature_type_x_min(self, temperature_type: str):
        self.record_method('XminTemperatureType', temperature_type)

    def set_temperature_type_x_max(self, temperature_type: str):
        self.record_method('XmaxTemperatureType', temperature_type)

    def set_temperature_types_x(self, min_type: str, max_type: str):
        self.set_temperature_type_x_min(min_type)
        self.set_temperature_type_x_max(max_type)

    def set_temperature_type_y_min(self, temperature_type: str):
        self.record_method('YminTemperatureType', temperature_type)

    def set_temperature_type_y_max(self, temperature_type: str):
        self.record_method('YmaxTemperatureType', temperature_type)

    def set_temperature_types_y(self, min_type: str, max_type: str):
        self.set_temperature_type_y_min(min_type)
        self.set_temperature_type_y_max(max_type)

    def set_temperature_type_z_min(self, temperature_type: str):
        self.record_method('ZminTemperatureType', temperature_type)

    def set_temperature_type_z_max(self, temperature_type: str):
        self.record_method('ZmaxTemperatureType', temperature_type)

    def set_temperature_types_z(self, min_type: str, max_type: str):
        self.set_temperature_type_z_min(min_type)
        self.set_temperature_type_z_max(max_type)

    def set_temperature_types(
            self, x_min: str, x_max: str, y_min: str, y_max: str, z_min: str, z_max: str):
        self.set_temperature_types_x(x_min, x_max)
        self.set_temperature_types_y(y_min, y_max)
        self.set_temperature_types_z(z_min, z_max)

    def set_temperature_x_min(self, temperature: float):
        self.record_method('XminTemperature', temperature)

    def set_temperature_x_max(self, temperature: float):
        self.record_method('XmaxTemperature', temperature)

    def set_temperatures_x(self, min_temperature: float, max_temperature: float):
        self.set_temperature_x_min(min_temperature)
        self.set_temperature_x_max(max_temperature)

    def set_temperature_y_min(self, temperature: float):
        self.record_method('YminTemperature', temperature)

    def set_temperature_y_max(self, temperature: float):
        self.record_method('YmaxTemperature', temperature)

    def set_temperatures_y(self, min_temperature: float, max_temperature: float):
        self.set_temperature_y_min(min_temperature)
        self.set_temperature_y_max(max_temperature)

    def set_temperature_z_min(self, temperature: float):
        self.record_method('ZminTemperature', temperature)

    def set_temperature_z_max(self, temperature: float):
        self.record_method('ZmaxTemperature', temperature)

    def set_temperatures_z(self, min_temperature: float, max_temperature: float):
        self.set_temperature_z_min(min_temperature)
        self.set_temperature_z_max(max_temperature)

    def set_temperatures(
            self, x_min: float, x_max: float, y_min: float, y_max: float,
            z_min: float, z_max: float):
        self.set_temperatures_x(x_min, x_max)
        self.set_temperatures_y(y_min, y_max)
        self.set_temperatures_z(z_min, z_max)

    # returns: (x_min, x_max, y_min, y_max, z_min, z_max)
    def get_calculation_box(self) -> tuple[float, float, float, float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetCalculationBox', None, D, D, D, D, D, D)

    # returns: (x_min, x_max, y_min, y_max, z_min, z_max)
    def get_structure_box(self) -> tuple[float, float, float, float, float, float]:
        D = VBATypeName.Double
        return self.query_method_t('GetStructureBox', None, D, D, D, D, D, D)

    def set_number_of_layers(self, count: int):
        self.record_method('Layer', count)

    def set_minimum_lines_distance(self, distance: float):
        self.record_method('MinimumLinesDistance', distance)

    def set_minimum_distance_type(self, distance_type: str):
        self.record_method('MinimumDistanceType', distance_type)

    def set_absolute_distance(self, distance: float):
        self.record_method('SetAbsoluteDistance', distance)

    def set_minimum_distance_reference_frequency_type(self, freq_type: str):
        self.record_method('MinimumDistanceReferenceFrequencyType', freq_type)

    def set_minimum_distance_per_wavelength(self, distance: float):
        self.record_method('MinimumDistancePerWavelength', distance)

    def set_frequency_for_minimum_distance(self, freq: float):
        self.record_method('FrequencyForMinimumDistance', freq)

    def set_period_shift_x_deg(self, angle_deg: float):
        self.record_method('XPeriodicShift', angle_deg)

    def set_period_shift_x_rad(self, angle_rad: float):
        self.set_period_shift_x_deg(np.rad2deg(angle_rad))

    def set_period_shift_y_deg(self, angle_deg: float):
        self.record_method('YPeriodicShift', angle_deg)

    def set_period_shift_y_rad(self, angle_rad: float):
        self.set_period_shift_y_deg(np.rad2deg(angle_rad))

    def set_period_shift_z_deg(self, angle_deg: float):
        self.record_method('ZPeriodicShift', angle_deg)

    def set_period_shift_z_rad(self, angle_rad: float):
        self.set_period_shift_z_deg(np.rad2deg(angle_rad))

    def set_periodic_use_constant_angles(self, flag: bool = True):
        self.record_method('PeriodicUseConstantAngles', flag)

    def set_periodic_boundary_angles_deg(self, theta_deg: float, phi_deg: float):
        self.record_method('SetPeriodicBoundaryAngles', theta_deg, phi_deg)

    def set_periodic_boundary_angles_rad(self, theta_rad: float, phi_rad: float):
        self.set_periodic_boundary_angles_deg(np.rad2deg(theta_rad), np.rad2deg(phi_rad))

    def set_periodic_boundary_angles_direction(self, direction: str):
        self.record_method('SetPeriodicBoundaryAnglesDirection', direction)

    # returns: (theta, phi, dir)
    def get_unit_cell_scan_angle(self) -> tuple[float, float, str]:
        D, L = VBATypeName.Double, VBATypeName.Long
        res = self.query_method_t('GetUnitCellScanAngle', None, D, D, L)
        dir_str = self.DIRECTION_OUTWARD if res[2] == 1 else self.DIRECTION_INWARD
        return (res[0], res[1], dir_str)

    def set_unit_cells_distance_dir1(self, distance: float):
        self.record_method('UnitCellDs1', distance)

    def set_unit_cells_distance_dir2(self, distance: float):
        self.record_method('UnitCellDs2', distance)

    def get_unit_cells_distance_dir1(self) -> float:
        return self.query_method_float('GetUnitCellDs1')

    def get_unit_cells_distance_dir2(self) -> float:
        return self.query_method_float('GetUnitCellDs2')

    def set_unit_cells_angle_deg(self, angle_deg: float):
        self.record_method('UnitCellAngle', angle_deg)

    def set_unit_cells_angle_rad(self, angle_rad: float):
        self.set_unit_cells_angle_deg(np.rad2deg(angle_rad))

    def get_unit_cells_angle_deg(self) -> float:
        return self.query_method_float('UnitCellAngle')

    def get_unit_cells_angle_rad(self) -> float:
        return np.deg2rad(self.get_unit_cells_angle_deg())

    def set_unit_cells_origin(self, pos_dir1: float, pos_dir2: float):
        self.record_method('UnitCellOrigin', pos_dir1, pos_dir2)

    def set_unit_cells_fit_to_bounding_box(self, flag: bool = True):
        self.record_method('UnitCellFitToBoundingBox', flag)