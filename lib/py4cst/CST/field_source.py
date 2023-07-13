from . import Project
from . import ComObjectWrapper

class FieldSource(ComObjectWrapper):
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

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.FieldSource

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_file_name(self, name: str):
        self.invoke_method('FileName', name)

    def delete(self, name: str):
        self.invoke_method('Delete', name)

    def set_id(self, id: int):
        self.invoke_method('Id', id)

    def get_next_id(self) -> int:
        return self.invoke_method('GetNextId')

    def delete_all(self):
        self.invoke_method('DeleteAll')

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def read_from_file(self):
        self.invoke_method('Read')

    def set_project_path(self, path: str):
        self.invoke_method('ProjectPath', path)

    def set_use_relative_path(self, flag: bool = True):
        self.invoke_method('UseRelativePath', flag)

    def set_result_subdir(self, path: str):
        self.invoke_method('ResultSubDirectory', path)

    def set_field_type(self, field_type: str):
        self.invoke_method('SourceName', field_type)

    def set_field_monitor_name(self, name: str):
        self.invoke_method('FieldMonitorName', name)

    def set_import_setting(self, key: str, value: str):
        self.invoke_method('ImportSettings', key, value)

    def set_time_value(self, time: float):
        self.invoke_method('TimeValue', time)

    def set_use_last_time_frame(self, flag: bool = True):
        self.invoke_method('UseLastTimeFrame', flag)

    def set_use_copy_only(self, flag: bool = True):
        self.invoke_method('UseCopyOnly', flag)

    def create_field_import(self):
        self.invoke_method('CreateFieldImport')

    def create_field_import_from_abaqus(
            self, name: str, dir: str, nastran_file_name: str, distribution_file_name: str,
            geom_unit: str, temp_unit: str):
        self.invoke_method(
            'CreateFieldImportFromAbaqus', name, dir, nastran_file_name, distribution_file_name,
            geom_unit, temp_unit)