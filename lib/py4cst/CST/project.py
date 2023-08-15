from . import ComObjectWrapper
from . import Interface
from . import w32com
import os.path
from typing import Optional

MODULE_VERSION = '1.1'

class Project(ComObjectWrapper):
    SOLVER_HF_TIME_DOMAIN = 'HF Time Domain'
    SOLVER_HF_EIGENMODE = 'HF Eigenmode'
    SOLVER_HF_FREQUENCY_DOMAIN = 'HF Frequency Domain'
    SOLVER_HF_INTEGRAL_EQ = 'HF IntegralEq'
    SOLVER_HF_MULTILAYER = 'HF Multilayer'
    SOLVER_HF_ASYMPTOTIC = 'HF Asymptotic'
    SOLVER_LF_E_STATIC = 'LF EStatic'
    SOLVER_LF_M_STATIC = 'LF MStatic'
    SOLVER_LF_STATIONARY_CURRENT = 'LF Stationary Current'
    SOLVER_LF_FREQUENCY_DOMAIN = 'LF Frequency Domain'
    SOLVER_LF_TIME_DOMAIN_MQS = 'LF Time Domain (MQS)'
    SOLVER_PT_TRACKING = 'PT Tracking'
    SOLVER_PT_WAKEFIELDS = 'PT Wakefields'
    SOLVER_PT_PIC = 'PT PIC'
    SOLVER_THERMAL_STEADY_STATE = 'Thermal Steady State'
    SOLVER_THERMAL_TRANSIENT = 'Thermal Transient'
    SOLVER_MECHANICS = 'Mechanics'

    GUIDE_TYPE_TRANSIENT = 'Transient'
    GUIDE_TYPE_EIGENMODE = 'Eigenmode'
    GUIDE_TYPE_FREQUENCY_DOMAIN = 'Frequency Domain'
    GUIDE_TYPE_ELECTROSTATIC = 'Electrostatic'
    GUIDE_TYPE_MAGNETOSTATIC = 'Magnetostatic'
    GUIDE_TYPE_STATIONARY_CURRENT = 'Stationary Current'
    GUIDE_TYPE_LOW_FREQUENCY = 'Low Frequency'
    GUIDE_TYPE_PARTICLE_TRACKING = 'Particle Tracking'

    APP_NAME_EMS = 'EMS'
    APP_NAME_PS = 'PS'
    APP_NAME_MWS = 'MWS'
    APP_NAME_MS = 'MS'
    APP_NAME_DS_FOR_MWS = 'DS for MWS'
    APP_NAME_DS_FOR_PCBS = 'DS for PCBS'
    APP_NAME_DS_FOR_CS = 'DS for CS'
    APP_NAME_DS_FOR_MS = 'DS for MS'
    APP_NAME_DS = 'DS'

    FILTER_NAME_RESULT_NAME = 'resultname'
    FILTER_NAME_TYPE = 'type'
    FILTER_NAME_TEMPLATE_NAME = 'templatename'
    FILTER_NAME_FOLDER = 'folder'

    VAL_TYPE_0D = '0D'
    VAL_TYPE_1D = '1D'
    VAL_TYPE_1D_COMPLEX = '1DC'
    VAL_TYPE_M0D = 'M0D'
    VAL_TYPE_M1D = 'M1D'
    VAL_TYPE_M1D_COMPLEX = 'M1DC'

    ARCHITECTURE_WIN32 = 'Windows IA32'
    ARCHITECTURE_WIN64 = 'Windows AMD64'
    ARCHITECTURE_LINUX32 = 'Linux IA32'
    ARCHITECTURE_LINUX64 = 'Linux AMD64'

    PATH_TYPE_ROOT = 'Root'
    PATH_TYPE_PROJECT = 'Project'
    PATH_TYPE_MODEL_3D = 'Model3D'
    PATH_TYPE_MODEL_CACHE = 'ModelCache'
    PATH_TYPE_RESULT = 'Result'
    PATH_TYPE_TEMP = 'Temp'

    def __init__(self, interface: Interface):
        self.interface = interface
        self.com_object = self.interface.com_object.Active3D()
        self.__update_path()
        self.report_information(self.__get_welcome_message())

    def invoke_method(self, name, *args, **kwargs):
        self.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def get_path(self):
        return self.path

    def close_without_saving(self):
        # NOTE: officially undocumented
        self.interface.store_and_enable_quiet_mode()
        self.interface.com_object.CloseProject(self.get_path())
        self.interface.restore_quiet_mode()

    def close(self):
        # NOTE: officially undocumented
        self.invoke_method('Quit')

    def is_active(self):
        return self.path == self.__read_path()

    def activate(self):
        self.interface.com_object.OpenFile(self.path)

    def reset_all(self):
        self.invoke_method('ResetAll')

    def set_screen_updating(self, flag: bool = True):
        self.invoke_method('ScreenUpdating', flag)

    def select_quick_start_guide(self, guide_type: str):
        self.invoke_method('SelectQuickStartGuide', guide_type)

    def select_tree_item(self, item_name: str):
        self.interface.store_and_disable_quiet_mode()
        self.invoke_method('SelectTreeItem', item_name)
        self.interface.restore_quiet_mode()

    def get_number_of_selected_tree_items(self) -> int:
        return self.invoke_method('GetNumberOfSelectedTreeItems')

    def get_selected_tree_item(self) -> str:
        return self.invoke_method('GetSelectedTreeItem')

    def get_next_selected_tree_item(self) -> str:
        return self.invoke_method('GetNextSelectedTreeItem')

    def set_lock(self, flag: bool = True):
        self.invoke_method('SetLock', flag)

    def lock(self, flag: bool = True):
        self.invoke_method('SetLock', flag)

    def unlock(self):
        self.invoke_method('SetLock', False)

    def add_to_history(self, caption: str, contents: str):
        if not self.invoke_method('AddToHistory', caption, contents):
            raise Exception('Failed to add \''+caption+'\' to history!')

    def get_database_value(self, key) -> str:
        return self.invoke_method('GetDataBaseValue', key)

    def get_database_array_value(self, key, index) -> str:
        return self.invoke_method('GetDataBaseArrayValue', key, index)

    def set_solver_type(self, solver_type: str):
        self.invoke_method('ChangeSolverType', solver_type)

    def get_solver_type(self) -> str:
        return self.invoke_method('GetSolverType')

    def run_solver(self):
        if not self.invoke_method('RunSolver'):
            raise Exception('Failed to run solver!')

    def import_subproject(self, file_name: str, do_wcs_alignment: bool = False):
        error_msg = self.invoke_method('ImportSubProject', file_name, do_wcs_alignment)
        if isinstance(error_msg, str) and len(error_msg) > 0:
            raise Exception(error_msg)

    def backup(self, path: str):
        return self.invoke_method('Backup', path)

    def open_new_file(self):
        self.invoke_method('FileNew')
        self.__update_path()

    def open_file(self, path: str):
        self.invoke_method('OpenFile', path)
        self.__update_path()

    def save(self):
        self.invoke_method('Save')

    def save_as(self, new_path: str, include_results: bool = False):
        new_path = os.path.abspath(new_path)
        self.invoke_method('SaveAs', new_path, include_results)
        self.path = new_path

    def store_in_archive(
            self, path: str, keep_all_results: bool = True, keep_1d_results: bool = True,
            keep_farfield_data: bool = True, delete_project_folder: bool = False):
        self.invoke_method('StoreInArchive',
            path, keep_all_results, keep_1d_results, keep_farfield_data, delete_project_folder)

    def delete_parameter(self, name: str):
        self.invoke_method('DeleteParameter', name)

    def has_parameter(self, name: str) -> bool:
        return self.invoke_method('DoesParameterExist', name)

    def get_number_of_parameters(self) -> int:
        return self.invoke_method('GetNumberOfParameters')

    def get_parameter_name(self, index: int) -> str:
        return self.invoke_method('GetParameterName', index)

    def get_parameter_value(self, index: int) -> float:
        return self.invoke_method('GetParameterNValue', index)

    def get_parameter_expression(self, index: int) -> str:
        return self.invoke_method('GetParameterSValue', index)

    def rename_parameter(self, old_name: str, new_name: str):
        self.invoke_method('RenameParameter', old_name, new_name)

    def restore_parameter(self, name: str) -> str:
        return self.invoke_method('RestoreParameter', name)

    def restore_parameter_as_number(self, name: str) -> float:
        return self.invoke_method('RestoreDoubleParameter', name)

    def restore_parameter_expression(self, name: str) -> str:
        return self.invoke_method('RestoreParameterExpression', name)

    def store_parameter_with_description(self, name: str, expression: str, description: str):
        self.invoke_method('StoreParameterWithDescription', name, expression, description)

    def store_parameter(self, name: str, expression: str):
        self.invoke_method('StoreParameter', name, expression)

    def store_parameters(self, names: list[str], values: list[any]):
        names_arr = w32com.create_str_array(names)
        values_arr = w32com.create_str_array(values)
        self.invoke_method('StoreParameters', names_arr, values_arr)

    def store_numeric_parameter(self, name: str, value: float):
        self.invoke_method('StoreDoubleParameter', name, value)

    def ensure_parameter(self, name: str, default_expression: str):
        self.invoke_method('MakeSureParameterExists', name, default_expression)

    def does_project_depend_on_parameter(self, param_name: str) -> bool:
        return self.invoke_method('DoesProjectDependOnParameter', param_name)

    def set_parameter_description(self, name: str, description: str):
        self.invoke_method('SetParameterDescription', name, description)

    def get_parameter_description(self, name: str):
        return self.invoke_method('GetParameterDescription', name)

    def get_parameter_combination(self, result_id: str) -> Optional[tuple[any]]:
        names_var = w32com.create_ref_variant()
        values_var = w32com.create_ref_variant()
        success = self.invoke_method('GetParameterCombination', result_id, names_var, values_var)
        return (names_var.value, values_var.value) if success else None

    #TODO implement: def get_project_parameters(self, file_path: str)

    def clear_global_data_values(self):
        self.invoke_method('ClearGlobalDataValues')

    def delete_global_data_values(self, name: str):
        self.invoke_method('DeleteGlobalDataValue', name)

    def restore_global_data_value(self, name: str):
        return self.invoke_method('RestoreGlobalDataValue', name)

    def store_global_data_value(self, name: str, value):
        self.invoke_method('StoreGlobalDataValue', name, value)

    def reset_global_data_storage(self):
        self.invoke_method('ResetGlobalDataStorage')

    def set_global_data(self, name: str, value):
        self.invoke_method('SetGlobalData', name, value)

    def get_global_data(self, name: str):
        return self.invoke_method('GetGlobalData', name)

    # math functions won't be implemented, it's unnecessary

    def evaluate(self, expression):
        return self.invoke_method('Evaluate', expression)

    def set_activate_script_settings(self, switch: bool = True):
        self.invoke_method('ActivateScriptSettings', switch)

    def clear_script_settings(self):
        self.invoke_method('ClearScriptSettings')

    def get_last_0d_result(self, name: str) -> float:
        return self.invoke_method('GetLast0DResult', name)

    def get_last_1d_result(self, name: str):
        # TODO: return list[float]
        return self.invoke_method('GetLast1DResult', name)

    def get_last_1d_complex_result(self, name: str):
        # TODO: return list[complex]
        return self.invoke_method('GetLast1DComplexResult', name)

    def get_last_result_id(self) -> str:
        return self.invoke_method('GetLastResultID')

    def get_script_setting(self, name: str, default_value: str) -> str:
        return self.invoke_method('GetScriptSetting', name, default_value)

    def store_script_setting(self, name: str, value: str) -> str:
        self.invoke_method('StoreScriptSetting', name, value)

    def store_template_setting(self, name: str, value: str) -> str:
        self.invoke_method('StoreTemplateSetting', name, value)

    def get_script_file_name(self) -> str:
        return self.invoke_method('GetScriptFileName')

    def evaluate_result_templates(self):
        self.invoke_method('EvaluateResultTemplates')

    def set_application_name(self, name: str):
        self.invoke_method('SetApplicationName', name)

    def reset_application_name(self):
        self.invoke_method('ResetApplicationName')

    def reset_template_iterator(self):
        self.invoke_method('ResetTemplateIterator')

    def set_template_filter(self, filter_name: str, value: str):
        self.invoke_method('SetTemplateFilter', filter_name, value)

    def get_next_template(
            self, result_name: str, val_type: str, template_name: str, folder: str) -> bool:
        return self.invoke_method('GetNextTemplate', result_name, val_type, template_name, folder)

    def get_file_type(self, file_path: str) -> str:
        return self.invoke_method('GetFileType', file_path)

    def get_impedance_from_tree_item(self, tree_item_name: str):
        # TODO: return list[complex]
        return self.invoke_method('GetImpedanceFromTreeItem', tree_item_name)

    def get_first_table_result(self, result_name: str) -> str:
        return self.invoke_method('GetFirstTableResult', result_name)

    def get_next_table_result(self, result_name: str) -> str:
        return self.invoke_method('GetNextTableResult', result_name)

    def was_template_aborted(self) -> bool:
        return self.invoke_method('GetTemplateAborted')

    def get_macro_path(self) -> str:
        return self.invoke_method('GetMacroPath')

    def get_macro_path_from_index(self, index: int) -> str:
        return self.invoke_method('GetMacroPathFromIndex', index)

    def get_number_of_macro_paths(self) -> int:
        return self.invoke_method('GetNumberOfMacroPaths')

    def run_and_wait(self, command: str):
        self.invoke_method('RunAndWait', command)

    def run_macro(self, macro_name: str):
        self.invoke_method('RunMacro', macro_name)

    def run_script(self, script_name: str):
        self.invoke_method('RunScript', script_name)

    def report_information(self, *msg):
        self.invoke_method('ReportInformation', ''.join(list(map(lambda x: str(x), msg))))

    def report_warning(self, *msg):
        self.invoke_method('ReportWarning', ''.join(list(map(lambda x: str(x), msg))))

    def report_information_to_window(self, *msg):
        self.invoke_method('ReportInformationToWindow', ''.join(list(map(lambda x: str(x), msg))))

    def report_warning_to_window(self, *msg):
        self.invoke_method('ReportWarningToWindow', ''.join(list(map(lambda x: str(x), msg))))

    def report_error(self, *msg):
        self.invoke_method('ReportError', ''.join(list(map(lambda x: str(x), msg))))

    def set_common_mpi_cluster_config(
            self, install_folder: str, temp_folder: str, architecture: str):
        self.invoke_method('SetCommonMPIClusterConfig', install_folder, temp_folder, architecture)

    def set_common_mpi_cluster_login_info(self, user_name: str, private_key_file_path: str):
        self.invoke_method('SetCommonMPIClusterLoginInfo', user_name, private_key_file_path)

    def get_mpi_cluster_size(self) -> int:
        return self.invoke_method('GetMPIClusterSize')

    def clear_mpi_cluster_config(self):
        self.invoke_method('ClearMPIClusterConfig')

    def add_mpi_cluster_node_config(
            self, host_name: str, install_folder: str, temp_folder: str, architecture: str,
            active: bool = True):
        self.invoke_method(
            'AddMPIClusterNodeConfig', host_name, install_folder, temp_folder,
            architecture, active)

    def import_xy_curve_from_ascii_file(self, folder_name: str, file_path: str):
        self.invoke_method('ImportXYCurveFromASCIIFile', folder_name, file_path)

    def paste_curves_from_ascii_file(self, folder_name: str, file_path: str):
        self.invoke_method('PasteCurvesFromASCIIFile', folder_name, file_path)

    def paste_curves_from_clipboard(self, folder_name: str):
        self.invoke_method('PasteCurvesFromClipboard', folder_name)

    def scale_curves(self, folder_name: str, x_scale: float, y_scale: float):
        self.invoke_method('ScaleCurves', folder_name, x_scale, y_scale)

    def store_curves_in_ascii_files(self, file_name: str):
        self.invoke_method('StoreCurvesInASCIIFile', file_name)

    def store_curves_in_clipboard(self):
        self.invoke_method('StoreCurvesInClipboard')

    #TODO: implement CalculateFourierComplex
    #TODO: implement CalculateCONV
    #TODO: implement CalculateCROSSCOR
    #TODO: implement ApplyWindow

    def delete_results(self):
        self.invoke_method('DeleteResults')

    def get_field_frequency(self) -> float:
        return self.invoke_method('GetFieldFrequency')

    # TODO: implement missing methods

    def get_application_name(self) -> str:
        return self.invoke_method('GetApplicationName')

    def get_application_version(self) -> str:
        return self.invoke_method('GetApplicationVersion')

    def get_install_path(self) -> str:
        return self.invoke_method('GetInstallPath')

    def get_project_path(self, path_type: str) -> str:
        return self.invoke_method('GetProjectPath', path_type)

    # TODO: implement missing methods?

    def is_building_model(self) -> bool:
        return self.invoke_method('IsBuildingModel')

    def get_license_host_id(self) -> str:
        return self.invoke_method('GetLicenseHostId')

    def get_license_customer_number(self) -> str:
        return self.invoke_method('GetLicenseCustomerNumber')

    # TODO: implement missing methods

    def rebuild(self):
        self.invoke_method('Rebuild')

    def rebuild_on_parametric_change(self):
        show_msg_box = self.interface.is_in_quiet_mode()
        full_rebuild = False
        self.invoke_method('RebuildOnParametricChange', full_rebuild, show_msg_box)

    def rebuild_fully_on_parametric_change(self):
        show_msg_box = self.interface.is_in_quiet_mode()
        full_rebuild = True
        self.invoke_method('RebuildOnParametricChange', full_rebuild, show_msg_box)

    def get_pickpoint_coords(self, pickpoint_id: int):
        x = self.invoke_method('xp', pickpoint_id)
        y = self.invoke_method('yp', pickpoint_id)
        z = self.invoke_method('zp', pickpoint_id)
        return [x, y, z]

    # TODO: implement missing methods

    def export_image_to_file(self, path: str, width: int = 0, height: int = 0):
        self.invoke_method('ExportImageToFile', path, width, height)

    def export_image_to_clipboard(self, width: int = 0, height: int = 0):
        self.invoke_method('ExportImageToClipboard', width, height)

    # TODO: implement missing methods

    def ensure_active(self):
        if not self.is_active():
            self.activate()

    def __read_path(self):
        return super().invoke_method('GetProjectPath', 'Project') + '.cst'

    def __update_path(self):
        self.path = self.__read_path()

    def __get_welcome_message(self):
        return f'CST Studio Suite Python interface v{MODULE_VERSION} by Samuel Travnicek connected.'