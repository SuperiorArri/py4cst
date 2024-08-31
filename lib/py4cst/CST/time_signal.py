from . import IVBAProvider, VBAObjWrapper

class TimeSignal(VBAObjWrapper):
    TYPE_GAUSSIAN = 'Gaussian'
    TYPE_RECTANGULAR = 'Rectangular'
    TYPE_SINE_STEP = 'Sine step'
    TYPE_SINE = 'Sine'
    TYPE_SMOOTH_STEP = 'Smooth step'
    TYPE_CONSTANT = 'Constant'
    TYPE_DOUBLE_EXPONENTIAL = 'Double exponential'
    TYPE_IMPULSE = 'Impulse'
    TYPE_USER = 'User'
    TYPE_IMPORT = 'Import'

    PROBLEM_TYPE_HIGH_FREQUENCY = 'High Frequency'
    PROBLEM_TYPE_LOW_FREQUENCY = 'Low Frequency'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'TimeSignal')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def set_id(self, id: int):
        self.cache_method('Id', id)

    def rename(self, old_name: str, new_name: str, problem_type: str):
        self.record_method('Rename', old_name, new_name, problem_type)

    def delete(self, name: str, problem_type: str):
        self.record_method('Delete', name, problem_type)

    def create(self):
        self.cache_method('Create')
        self.flush_cache('Create TimeSignal')

    def set_file_name(self, file_name: str):
        self.cache_method('FileName', file_name)

    def set_use_copy_only(self, flag: bool = True):
        self.cache_method('UseCopyOnly', flag)

    def set_f_min(self, value: float):
        self.cache_method('Fmin', value)

    def set_f_max(self, value: float):
        self.cache_method('Fmax', value)

    def set_total_time(self, time: float):
        self.cache_method('Ttotal', time)

    def set_rise_time(self, time: float):
        self.cache_method('Trise', time)

    def set_hold_time(self, time: float):
        self.cache_method('Thold', time)

    def set_fall_time(self, time: float):
        self.cache_method('Tfall', time)

    def set_vertical_offset(self, offset: float):
        self.cache_method('Voffset', offset)

    def set_amplitude_rise_percent(self, percent: float):
        self.cache_method('AmplitudeRisePercent', percent)

    def set_rise_factor(self, factor: float):
        self.cache_method('RiseFactor', factor)

    def set_chirp_rate(self, rate: float):
        self.cache_method('ChirpRate', rate)

    def set_frequency(self, frequency: float):
        self.cache_method('Frequency', frequency)

    def set_phase(self, phase: float):
        self.cache_method('Phase', phase)

    def set_amplitude(self, amplitude: float):
        self.cache_method('Amplitude', amplitude)

    def set_start_amplitude(self, amplitude: float):
        self.cache_method('StartAmplitude', amplitude)

    def set_end_amplitude(self, amplitude: float):
        self.cache_method('EndAmplitude', amplitude)

    def set_signal_type(self, signal_type: str):
        self.cache_method('SignalType', signal_type)

    def set_min_number_of_user_signal_samples(self, number: int):
        self.cache_method('MinUserSignalSamples', number)

    def set_periodic(self, flag: bool = True):
        self.cache_method('Periodic', flag)

    def set_problem_type(self, problem_type: str):
        self.cache_method('ProblemType', problem_type)

    def set_excitation_signal_as_reference(self, signal_name: str, problem_type: str):
        self.cache_method('ExcitationSignalAsReference', signal_name, problem_type)

    def resample_excitation_signal(
            self, signal_name: str, t_min: float, t_max: float, t_step: float, problem_type: str):
        self.cache_method(
            'ExcitationSignalResample', signal_name, t_min, t_max, t_step, problem_type)

    def get_next_id(self) -> int:
        return self.query_method_int('GetNextId')