from . import IVBAProvider, VBAObjWrapper

class FieldSource(VBAObjWrapper):
    ALIGNMENT_CUSTOM = 'user'
    ALIGNMENT_CURRENT_WCS = 'currentwcs'
    ALIGNMENT_SOURCE_FILE = 'sourcefile'

    CALC_MODE_AUTOMATIC = 'automatic'
    CALC_MODE_CUSTOM = 'user defined'
    CALC_MODE_AUTOTRUNCATION = 'autotruncation'

    FIELD_TYPE_TEMPERATURE = 'Temperature'
    FIELD_TYPE_DISPLACEMENT = 'Displacement'
    FIELD_TYPE_FORCE_DENSITY = 'Force Density'
    FIELD_TYPE_NODAL_FORCES = 'Nodal Forces'
    FIELD_TYPE_THERMAL_LOSSES = 'Thermal Losses'

    FIELD_MONITOR_NAME_INITIAL_SOLUTION = 'Initial Solution'
    FIELD_MONITOR_NAME_STATIONARY_SOLUTION = 'Stationary Solution'

    IMPORT_SETTING_FORMAT_SOURCE = 'FormatSource'
    IMPORT_SETTING_FORMAT_TARGET = 'FormatTarget'
    IMPORT_SETTING_NASTRAN_FILE_NAME = 'NastranFilename'
    IMPORT_SETTING_TEMPERATURE_FILE_NAME = 'TemperatureFilename'
    IMPORT_SETTING_GEOMETRY_UNIT = 'GeometryUnit'
    IMPORT_SETTING_TEMPERATURE_UNIT = 'TemperatureUnit'
    IMPORT_SETTING_WORKING_DIR = 'WorkingDir'

    IMPORT_SETTING_FORMAT_SOURCE_ABAQUS = 'Abaqus'
    IMPORT_SETTING_FORMAT_SOURCE_TET = 'Tet'
    IMPORT_SETTING_FORMAT_SOURCE_HEX = 'Hex'
    IMPORT_SETTING_FORMAT_SOURCE_CHT = 'CHT'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'FieldSource')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def set_file_name(self, name: str):
        self.record_method('FileName', name)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def set_id(self, id: int):
        self.record_method('Id', id)

    def get_next_id(self) -> int:
        return self.query_method_int('GetNextId')

    def delete_all(self):
        self.record_method('DeleteAll')

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def read_from_file(self):
        self.record_method('Read')

    def set_project_path(self, path: str):
        self.record_method('ProjectPath', path)

    def set_use_relative_path(self, flag: bool = True):
        self.record_method('UseRelativePath', flag)

    def set_result_subdir(self, path: str):
        self.record_method('ResultSubDirectory', path)

    def set_field_type(self, field_type: str):
        self.record_method('SourceName', field_type)

    def set_field_monitor_name(self, name: str):
        self.record_method('FieldMonitorName', name)

    def set_import_setting(self, key: str, value: str):
        self.record_method('ImportSettings', key, value)

    def set_time_value(self, time: float):
        self.record_method('TimeValue', time)

    def set_use_last_time_frame(self, flag: bool = True):
        self.record_method('UseLastTimeFrame', flag)

    def set_use_copy_only(self, flag: bool = True):
        self.record_method('UseCopyOnly', flag)

    def create_field_import(self):
        self.record_method('CreateFieldImport')

    def create_field_import_from_abaqus(
            self, name: str, dir: str, nastran_file_name: str, distribution_file_name: str,
            geom_unit: str, temp_unit: str):
        self.record_method(
            'CreateFieldImportFromAbaqus', name, dir, nastran_file_name, distribution_file_name,
            geom_unit, temp_unit)