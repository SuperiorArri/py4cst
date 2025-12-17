from __future__ import annotations
import re
from parse import parse
import numpy as np

class Farfield:
    def __init__(self) -> None:
        self.samples = None # [theta_index,phi_index,component_index:0=theta/1=phi]
        self.frequency = 0
        self.position = np.array([0., 0., 0.])
        self.z_axis = np.array([0., 0., 1.])
        self.x_axis = np.array([1., 0., 0.])
        self.radiated_power = 0
        self.accepted_power = 0
        self.stimulated_power = 0

    def __add__(self, ff2: Farfield) -> Farfield:
        new_ff = Farfield()
        new_ff.set_samples(self.samples + ff2.samples)
        return new_ff

    def __sub__(self, ff2: Farfield) -> Farfield:
        new_ff = Farfield()
        new_ff.set_samples(self.samples - ff2.samples)
        return new_ff

    def __str__(self) -> str:
        templ = 'Farfield:\n'\
            '\tFrequency: {freq:.2e} Hz\n'\
            '\tPosition: {pos} m\n'\
            '\tZ axis: {z_axis} m\n'\
            '\tX axis: {x_axis} m\n'\
            '\tRadiated power: {r_pow:.2e} W\n'\
            '\tAccepted power: {a_pow:.2e} W\n'\
            '\tStimulated power: {s_pow:.2e} W\n'\
            '\t# Theta components: {num_theta}\n'\
            '\t# Phi components: {num_phi}'
        return templ.format(
            freq=self.frequency, pos=self.position, z_axis=self.z_axis, x_axis=self.x_axis,
            r_pow=self.radiated_power, a_pow=self.accepted_power, s_pow=self.stimulated_power,
            num_theta=self.get_num_theta_samples(), num_phi=self.get_num_phi_samples())

    def set_samples(self, samples: np.ndarray) -> None:
        self.samples = samples

    def get_samples(self) -> np.ndarray:
        return self.samples

    def set_theta_component(self, e_theta: np.ndarray) -> None:
        self.samples[:,:,0] = e_theta

    def get_theta_component(self) -> np.ndarray:
        return self.samples[:,:,0]

    def set_phi_component(self, e_phi: np.ndarray) -> None:
        self.samples[:,:,1] = e_phi

    def get_phi_component(self) -> np.ndarray:
        return self.samples[:,:,1]

    def get_sample_at(self, theta_index: int, phi_index: int) -> np.ndarray:
        return self.samples[theta_index,phi_index,:]

    def init_samples_with_zeros(self, num_theta_samples: int, num_phi_samples: int) -> None:
        dim = (num_theta_samples, num_phi_samples, 2)
        self.samples = np.zeros(dim, dtype=np.complex128)

    def get_num_theta_samples(self) -> int:
        if self.samples is None:
            return 0
        return self.samples.shape[0]

    def get_theta_step_deg(self) -> float:
        self._ensure_existing_samples()
        return 180/(self.get_num_theta_samples() - 1)

    def get_theta_step_rad(self) -> float:
        self._ensure_existing_samples()
        return np.pi/(self.get_num_theta_samples() - 1)

    def get_theta_at_index_deg(self, index: int) -> float:
        return self.get_theta_step_deg()*index

    def get_theta_at_index_rad(self, index: int) -> float:
        return self.get_theta_step_rad()*index

    def get_index_of_theta_deg(self, angle_deg: float) -> int:
        return int(np.round(angle_deg/self.get_theta_step_deg()))

    def get_index_of_theta_rad(self, angle_rad: float) -> int:
        return int(np.round(angle_rad/self.get_theta_step_rad()))

    def get_theta_vec_deg(self) -> float:
        self._ensure_existing_samples()
        return np.arange(self.get_num_theta_samples())*self.get_theta_step_deg()

    def get_theta_vec_rad(self) -> float:
        self._ensure_existing_samples()
        return np.arange(self.get_num_theta_samples())*self.get_theta_step_rad()

    def get_num_phi_samples(self) -> int:
        if self.samples is None:
            return 0
        return self.samples.shape[1]

    def get_phi_step_deg(self) -> float:
        self._ensure_existing_samples()
        return 360/(self.get_num_phi_samples() - 1)

    def get_phi_step_rad(self) -> float:
        self._ensure_existing_samples()
        return 2*np.pi/(self.get_num_phi_samples() - 1)

    def get_phi_at_index_deg(self, index: int) -> float:
        return self.get_phi_step_deg()*index

    def get_phi_at_index_rad(self, index: int) -> float:
        return self.get_phi_step_rad()*index

    def get_index_of_phi_deg(self, angle_deg: float) -> int:
        return int(np.round(angle_deg/self.get_phi_step_deg()))

    def get_index_of_phi_rad(self, angle_rad: float) -> int:
        return int(np.round(angle_rad/self.get_phi_step_rad()))

    def get_phi_vec_deg(self) -> float:
        self._ensure_existing_samples()
        return np.arange(self.get_num_phi_samples())*self.get_phi_step_deg()

    def get_phi_vec_rad(self) -> float:
        self._ensure_existing_samples()
        return np.arange(self.get_num_phi_samples())*self.get_phi_step_rad()

    def set_frequency(self, frequency: float) -> None:
        self.frequency = frequency

    def get_frequency(self) -> float:
        return self.frequency

    def set_position(self, position: np.ndarray) -> None:
        self.position = position

    def get_position(self) -> np.ndarray:
        return self.position

    def set_z_axis(self, z_axis: np.ndarray) -> None:
        self.z_axis = z_axis

    def get_z_axis(self) -> np.ndarray:
        return self.z_axis

    def set_x_axis(self, x_axis: np.ndarray) -> None:
        self.x_axis = x_axis

    def get_x_axis(self) -> np.ndarray:
        return self.x_axis

    def set_radiated_power(self, power: float) -> None:
        self.radiated_power = power

    def get_radiated_power(self) -> float:
        return self.radiated_power

    def set_accepted_power(self, power: float) -> None:
        self.accepted_power = power

    def get_accepted_power(self) -> float:
        return self.accepted_power

    def set_stimulated_power(self, power: float) -> None:
        self.stimulated_power = power

    def get_stimulated_power(self) -> float:
        return self.stimulated_power

    @staticmethod
    def _ensure_same_farfield_sizes(ff1, ff2):
        if ff1.samples.shape != ff2.samples.shape:
            raise RuntimeError('Failed to compute dot product: Farfields have different sizes')

    def _ensure_existing_samples(self):
        if self.samples is None:
            raise RuntimeError('Farfield has no samples!')

class Parser:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.lines = None
        self.current_line = None
        self.version = None
        self.data_type = None
        self.num_frequencies = None
        self.position = None
        self.z_axis = None
        self.x_axis = None
        self.radiated_powers = []
        self.accepted_powers = []
        self.stimulated_powers = []
        self.frequencies = []
        self.farfields = []
        self.num_phi_samples = None
        self.num_theta_samples = None

    def parse_string(self, ffs_source_str: str):
        self.reset()
        self.lines = ffs_source_str.splitlines(keepends=False)
        self._process_lines()

    def get_farfields(self):
        farfields = []
        for n in range(len(self.frequencies)):
            farfields.append(self._get_nth_farfield(n))
        return farfields

    def _get_nth_farfield(self, n) -> Farfield:
        farfield = Farfield()
        farfield.set_samples(self.farfields[n])
        farfield.set_frequency(self.frequencies[n])
        farfield.set_position(self.position)
        farfield.set_z_axis(self.z_axis)
        farfield.set_x_axis(self.x_axis)
        farfield.set_radiated_power(self.radiated_powers[n])
        farfield.set_accepted_power(self.accepted_powers[n])
        farfield.set_stimulated_power(self.stimulated_powers[n])
        return farfield

    def _process_lines(self):
        self.current_line = 0
        while self._has_lines_to_process():
            self._process_next_line()

    def _has_lines_to_process(self) -> bool:
        return self.current_line < len(self.lines)

    def _get_line_rel(self, relative_line_index) -> str:
        return self.lines[self.current_line+relative_line_index]

    def _jump_to_line_rel(self, relative_line_index):
        self.current_line += relative_line_index

    def _process_next_line(self):
        line = self.lines[self.current_line]
        self._process_line(line)

    def _process_line(self, line):
        if 'Version' in line:
            self._process_version_line()
        elif 'Data Type' in line:
            self._process_data_type_line()
        elif '#Frequencies' in line:
            self._process_num_frequencies_line()
        elif line.find('Position') >= 0:
            self._process_position_line()
        elif 'zAxis' in line:
            self._process_z_axis_line()
        elif 'xAxis' in line:
            self._process_x_axis_line()
        elif 'Radiated/Accepted/Stimulated Power , Frequency' in line:
            self._process_powers_and_frequencies_line()
        elif '#phi' in line and '#theta' in line:
            self._process_num_phi_theta_samples_line()
        elif 'Phi, Theta, Re(E_Theta), Im(E_Theta), Re(E_Phi), Im(E_Phi)' in line:
            self._process_farfield_samples_line()
        else:
            self.current_line += 1

    def _process_version_line(self):
        version = self._get_line_rel(1).strip()
        Parser._ensure_supported_version(version)
        self.version = version
        self._jump_to_line_rel(2)

    def _process_data_type_line(self):
        self.data_type = self._get_line_rel(1).strip()
        self._jump_to_line_rel(2)

    def _process_num_frequencies_line(self):
        self.num_frequencies = int(self._get_line_rel(1).strip())
        self._jump_to_line_rel(2)

    def _process_position_line(self):
        self.position = Parser._parse_vector_line(self._get_line_rel(1), 3)
        self._jump_to_line_rel(2)

    def _process_z_axis_line(self):
        self.z_axis = Parser._parse_vector_line(self._get_line_rel(1), 3)
        self._jump_to_line_rel(2)

    def _process_x_axis_line(self):
        self.x_axis = Parser._parse_vector_line(self._get_line_rel(1), 3)
        self._jump_to_line_rel(2)

    def _process_powers_and_frequencies_line(self):
        self._jump_to_line_rel(1)
        self._process_all_powers_and_frequencies_lines()

    def _process_all_powers_and_frequencies_lines(self):
        for _ in range(self.num_frequencies):
            self._process_next_powers_and_frequency_lines()

    def _process_next_powers_and_frequency_lines(self):
        self.radiated_powers.append(float(self._get_line_rel(0).strip()))
        self.accepted_powers.append(float(self._get_line_rel(1).strip()))
        self.stimulated_powers.append(float(self._get_line_rel(2).strip()))
        self.frequencies.append(float(self._get_line_rel(3).strip()))
        self._jump_to_line_rel(5)

    def _process_num_phi_theta_samples_line(self):
        values = Parser._parse_vector_line(self._get_line_rel(1), 2)
        self.num_phi_samples = int(values[0])
        self.num_theta_samples = int(values[1])
        self._reserve_new_farfield_tensor(self.num_phi_samples, self.num_theta_samples)
        self._jump_to_line_rel(2)

    def _reserve_new_farfield_tensor(self, num_phi_samples, num_theta_samples):
        dim = (num_theta_samples, num_phi_samples, 2)
        self.farfields.append(np.zeros(dim, dtype=np.complex128))

    def _process_farfield_samples_line(self):
        self._jump_to_line_rel(1)
        self._process_all_farfield_sample_data_lines()

    def _process_all_farfield_sample_data_lines(self):
        farfield_tensor = self.farfields[-1]
        for phi_i in range(self.num_phi_samples):
            for theta_i in range(self.num_theta_samples):
                self._process_next_farfield_sample_data_line(farfield_tensor, phi_i, theta_i)

    def _process_next_farfield_sample_data_line(self, farfield_tensor, phi_i, theta_i):
        values = Parser._parse_vector_line(self._get_line_rel(0), 6)
        self._jump_to_line_rel(1)
        farfield_tensor[theta_i, phi_i, 0] = values[2] + 1j*values[3]
        farfield_tensor[theta_i, phi_i, 1] = values[4] + 1j*values[5]

    @staticmethod
    def _ensure_supported_version(version: str):
        if not Parser._is_supported_version(version):
            raise RuntimeError('Unsupported ffs version: ' + version)

    @staticmethod
    def _is_supported_version(version: str):
        return version == '3.0'

    @staticmethod
    def _parse_vector_line(line, num_components: int) -> np.ndarray:
        line = Parser._remove_duplicate_spaces(line.strip())
        vec = parse(('{} '*num_components).rstrip(), line).fixed
        Parser._ensure_vector_line_num_components(vec, num_components)
        return np.array([float(x) for x in vec])

    @staticmethod
    def _ensure_vector_line_num_components(vec, expected_num_components: int):
        if len(vec) != expected_num_components:
            raise RuntimeError(
                'Failed to parse vector line: Invalid number of components - expected '
                + str(expected_num_components) + ', got ' + str(len(vec)))

    @staticmethod
    def _remove_duplicate_spaces(txt: str) -> str:
        return re.sub(' +', ' ', txt)

class Dumper:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.farfields = []
        self.version = '3.0'
        self.data_type = 'Farfield'

    def set_version(self, version: str):
        Dumper._ensure_supported_version(version)
        self.version = version

    def set_farfields(self, farfields: list):
        self.farfields = farfields

    def add_farfield(self, ff: Farfield):
        self.farfields.append(ff)

    def clear_farfields(self):
        self.farfields.clear()

    def dump_to_string(self) -> str:
        res = self._dump_header()
        res += self._dump_version()
        res += self._dump_data_type()
        res += self._dump_num_freq()
        res += self._dump_position()
        res += self._dump_z_axis()
        res += self._dump_x_axis()
        res += self._dump_powers_and_frequencies()
        res += self._dump_samples()
        return res

    def _dump_header(self) -> str:
        return '// CST Farfield Source File\n \n'

    def _dump_version(self) -> str:
        return '// Version:\n{ver} \n\n'.format(ver=self.version)

    def _dump_data_type(self) -> str:
        return '// Data Type\n{dt} \n\n'.format(dt=self.data_type)

    def _dump_num_freq(self) -> str:
        return '// #Frequencies\n{nf} \n\n'.format(nf=len(self.farfields))

    def _dump_position(self) -> str:
        pos = self.farfields[0].get_position()
        return '// Position\n{vec}\n\n'.format(vec=Dumper._dump_vec(pos))

    def _dump_z_axis(self) -> str:
        pos = self.farfields[0].get_z_axis()
        return '// zAxis\n{vec}\n\n'.format(vec=Dumper._dump_vec(pos))

    def _dump_x_axis(self) -> str:
        pos = self.farfields[0].get_x_axis()
        return '// xAxis\n{vec}\n\n'.format(vec=Dumper._dump_vec(pos))

    def _dump_powers_and_frequencies(self) -> str:
        templ = '// Radiated/Accepted/Stimulated Power , Frequency \n'+\
            ('{}'*len(self.farfields))+'\n'
        values = map(lambda ff: Dumper._dump_powers_and_frequency(ff), self.farfields)
        return templ.format(*values)

    def _dump_samples(self):
        res = ''
        for ff in self.farfields:
            res += Dumper._dump_ff_num_samples(ff)+Dumper._dump_ff_samples(ff)
        return res

    @staticmethod
    def _ensure_supported_version(version: str):
        if not Dumper._is_supported_version(version):
            raise RuntimeError('Unsupported ffs version: ' + version)

    @staticmethod
    def _is_supported_version(version: str):
        return version == '3.0'

    @staticmethod
    def _dump_vec(vec):
        return ('{:e} '*len(vec)).format(*vec)

    @staticmethod
    def _dump_powers_and_frequency(ff: Farfield) -> str:
        return '{:e} \n{:e} \n{:e} \n{:e} \n\n'.format(
            ff.get_radiated_power(), ff.get_accepted_power(),
            ff.get_stimulated_power(), ff.get_frequency())

    @staticmethod
    def _dump_ff_num_samples(ff: Farfield) -> str:
        templ = '// >> Total #phi samples, total #theta samples\n{n_phi} {n_theta}\n\n'
        return templ.format(n_phi=ff.get_num_phi_samples(), n_theta=ff.get_num_theta_samples())

    @staticmethod
    def _dump_ff_samples(ff: Farfield) -> str:
        templ = '// >> Phi, Theta, Re(E_Theta), Im(E_Theta), Re(E_Phi), Im(E_Phi): \n{samples}\n'
        return templ.format(samples=Dumper._dump_ff_sample_vecs(ff))

    @staticmethod
    def _dump_ff_sample_vecs(ff: Farfield) -> str:
        res = ''
        for phi_index in range(ff.get_num_phi_samples()):
            for theta_index in range(ff.get_num_theta_samples()):
                res += Dumper._dump_sample_at(ff, phi_index, theta_index)
        return res

    @staticmethod
    def _dump_sample_at(ff: Farfield, phi_index, theta_index):
        phi = ff.get_phi_at_index_deg(phi_index)
        theta = ff.get_theta_at_index_deg(theta_index)
        field_vec = ff.get_sample_at(theta_index, phi_index)
        e_theta = field_vec[0]
        e_phi = field_vec[1]
        templ = '{:>8.3f}  {:>8.3f} {:>16.8e} {:>16.8e} {:>15.8e} {:>16.8e}\n'
        return templ.format(
            phi, theta, np.real(e_theta), np.imag(e_theta),
            np.real(e_phi), np.imag(e_phi))
