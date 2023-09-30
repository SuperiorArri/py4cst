from . import IVBAProvider, VBAObjWrapper

class Monitor(VBAObjWrapper):
    FIELD_TYPE_E_FIELD = 'Efield'
    FIELD_TYPE_H_FIELD = 'Hfield'
    FIELD_TYPE_POWER_FLOW = 'Powerflow'
    FIELD_TYPE_CURRENT = 'Current'
    FIELD_TYPE_POWER_LOSS = 'Powerloss'
    FIELD_TYPE_E_ENERGY = 'Eenergy'
    FIELD_TYPE_H_ENERGY = 'Henergy'
    FIELD_TYPE_FARFIELD = 'Farfield'
    FIELD_TYPE_FIELD_SOURCE = 'Fieldsource'
    FIELD_TYPE_SPACE_CHARGE = 'Spacecharge'
    FIELD_TYPE_PARTICLE_CURRENT_DENSITY = 'Particlecurrentdensity'

    DIMENSION_PLANE = 'plane'
    DIMENSION_VOLUME = 'volume'

    DIRECTION_X = 'x'
    DIRECTION_Y = 'y'
    DIRECTION_Z = 'z'

    DOMAIN_FREQUENCY = 'frequency'
    DOMAIN_TIME = 'time'
    DOMAIN_STATIC = 'static'

    ACCURACY_LOW = '1e-3'
    ACCURACY_MEDIUM = '1e-4'
    ACCURACY_HIGH = '1e-5'

    ORIGIN_BOUNDING_BOX = 'bbox'
    ORIGIN_ZERO = 'zero'
    ORIGIN_CUSTOM = 'free'

    SAMPLING_STRATEGY_FREQUENCIES = 'Frequencies'
    SAMPLING_STRATEGY_STEPS = 'Steps'
    SAMPLING_STRATEGY_LINEAR = 'Linear'
    SAMPLING_STRATEGY_LOGARITHMIC = 'Logarithmic'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Monitor')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def create(self):
        self.record_method('Create')

    def set_field_type(self, field_type: str):
        self.record_method('FieldType', field_type)

    def set_dimension(self, dimension: str):
        self.record_method('Dimension', dimension)

    def set_plane_normal_direction(self, direction: str):
        self.record_method('PlaneNormal', direction)

    def set_plane_position(self, position: float):
        self.record_method('PlanePosition', position)

    def set_domain(self, domain: str):
        self.record_method('Domain', domain)

    def set_frequency(self, frequency: float):
        self.record_method('Frequency', frequency)

    def set_time_start(self, start: float):
        self.record_method('Tstart', start)

    def set_time_step(self, step: float):
        self.record_method('Tstep', step)

    def set_time_end(self, end: float):
        self.record_method('Tend', end)

    def set_use_time_end(self, flag: bool = True):
        self.record_method('UseTend', flag)

    def set_average_over_time(self, flag: bool = True):
        self.record_method('TimeAverage', flag)

    def set_repetition_period(self, period: float):
        self.record_method('RepetitionPeriod', period)

    def set_automatic_order(self, flag: bool = True):
        self.record_method('AutomaticOrder', flag)

    def set_max_order(self, order: int):
        self.record_method('MaxOrder', order)

    def set_number_of_frequency_samples(self, number: int):
        self.record_method('FrequencySamples', number)

    def set_compute_transient_farfield(self, flag: bool = True):
        self.record_method('TransientFarfield', flag)

    def set_accuracy(self, accuracy: str):
        self.record_method('Accuracy', accuracy)

    def set_origin(self, origin: str):
        self.record_method('Origin', origin)

    def set_custom_origin(self, x: float, y: float, z: float):
        self.record_method('UserOrigin', x, y, z)

    def set_frequency_range(self, f_min: float, f_max: float):
        self.record_method('FrequencyRange', f_min, f_max)

    def set_domain(self, domain: str):
        self.record_method('Domain', domain)

    def set_number_of_samples(self, number: int):
        self.record_method('Samples', number)

    def set_sampling_strategy(self, strategy: str):
        self.record_method('SamplingStrategy', strategy)

    def set_monitor_value(self, value: float):
        self.record_method('MonitorValue', value)

    def set_monitor_value_list(self, frequencies: list[float]):
        freq_str = ';'.join(str(s) for s in frequencies)
        print('freq_str=', freq_str)
        self.record_method('MonitorValueList', freq_str)

    def set_sampling_step(self, step: float):
        self.record_method('SampleStep', step)

    def set_monitor_value_range(self, f_min: float, f_max: float):
        self.record_method('MonitorValueRange', f_min, f_max)

    def set_use_subvolume(self, flag: bool = True):
        self.record_method('UseSubvolume', flag)

    def set_subvolume(
            self, x_min: float, x_max: float, y_min: float, y_max: float,
            z_min: float, z_max: float):
        self.record_method('SetSubvolume', x_min, x_max, y_min, y_max, z_min, z_max)

    def set_invert_orientation(self, flag: bool = True):
        self.record_method('InvertOrientation', flag)

    def set_export_farfield_source(self, flag: bool = True):
        self.record_method('ExportFarfieldSource', flag)

    def set_enable_near_calculation(self, flag: bool = True):
        self.record_method('EnableNearfieldCalculation', flag)

    def create_using_arbitrary_values(self, frequencies: list[float]):
        freq_str = ';'.join(str(s) for s in frequencies)
        self.record_method('CreateUsingArbitraryValues', freq_str)

    def create_using_linear_samples(self, f_min: float, f_max: float, num_samples: int):
        self.record_method('CreateUsingLinearSamples', f_min, f_max, num_samples)

    def create_using_linear_step(self, f_min: float, f_max: float, f_step: float):
        self.record_method('CreateUsingLinearStep', f_min, f_max, f_step)

    def create_using_log_samples(self, f_min: float, f_max: float, num_samples: int):
        self.record_method('CreateUsingLogSamples', f_min, f_max, num_samples)

    def export(self, excitation_name: str, file_path: str, flag: bool = True):
        #TODO: find out the meaning of the flag
        self.record_method('Export', 'nfs', excitation_name, file_path, flag)

    def set_subvolume_sampling(self, x: float, y: float, z: float):
        self.record_method('SetSubVolumeSampling', x, y, z)

    def change_subvolume_sampling(self, monitor_name: str, x: float, y: float, z: float):
        self.record_method('ChangeSubVolumeSampling', monitor_name, x, y, z)

    def change_subvolume_sampling_to_history(self, monitor_name: str, x: float, y: float, z: float):
        self.record_method('ChangeSubVolumeSamplingToHistory', monitor_name, x, y, z)

    def get_number_of_monitors(self) -> int:
        return self.query_method_int('GetNumberOfMonitors')

    def get_monitor_name_from_index(self, index: int) -> str:
        #TODO: check if index is one based or zero based
        return self.query_method_str('GetMonitorNameFromIndex', index)

    def get_monitor_type_from_index(self, index: int) -> str:
        #TODO: check if index is one based or zero based
        return self.query_method_str('GetMonitorTypeFromIndex', index)

    def get_monitor_domain_from_index(self, index: int) -> str:
        #TODO: check if index is one based or zero based
        return self.query_method_str('GetMonitorDomainFromIndex', index)

    def get_monitor_frequency_from_index(self, index: int) -> float:
        #TODO: check if index is one based or zero based
        return self.query_method_float('GetMonitorFrequencyFromIndex', index)

    def get_monitor_time_start_from_index(self, index: int) -> float:
        #TODO: check if index is one based or zero based
        return self.query_method_float('GetMonitorTstartFromIndex', index)

    def get_monitor_time_step_from_index(self, index: int) -> float:
        #TODO: check if index is one based or zero based
        return self.query_method_float('GetMonitorTstepFromIndex', index)

    def get_monitor_time_end_from_index(self, index: int) -> float:
        #TODO: check if index is one based or zero based
        return self.query_method_float('GetMonitorTendFromIndex', index)