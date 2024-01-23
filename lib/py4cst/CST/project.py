# from . import info
from . import \
    IProject, IVBAProvider, Modeler, Schematic, InterfacePCBS, HistoryListGenerator, Parameters, \
    VBATypeName, IQuietModeController
from enum import Enum
from typing import Optional, Union
import os.path

def cast_vba_value(value: str, type_name: str):
    if type_name in ['Byte', 'Integer', 'Long']:
        return int(value)
    elif type_name in ['String', 'Variant']:
        return value
    elif type_name in ['Single', 'Double']:
        return float(value)
    elif type_name == 'Boolean':
        return value != 'False'
    else:
        raise RuntimeError('Unsupported VBA Type Name')

def get_types_vba_t(
        return_type: Optional[VBATypeName], *args: Union[str, int, float, bool, VBATypeName]):
    res = []
    if return_type is not None:
        res.append(return_type.value)
    for arg in args:
        if isinstance(arg, VBATypeName):
            res.append(arg.value)
    return res

class Project(IProject, IVBAProvider):
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

    class Kind(Enum):
        DesignStudio = 'DS'
        MicrowaveStudio = 'MWS'
        EMStudio = 'EMS'
        ParticleStudio = 'PS'
        MphysicsStudio = 'MPS'
        CableStudio = 'CS'
        PCBStudio = 'PCBS'
        FilterDesigner3D = 'FD3D'

        @staticmethod
        def to_cst(value):
            from cst.interface import ProjectType
            return getattr(ProjectType, value.value)

        @staticmethod
        def from_cst(value):
            return Project.Kind(value.name)

    def __init__(self, native_obj, quiet_mode_controller: IQuietModeController) -> None:
        self.native_obj = native_obj
        self.quiet_mode_controller = quiet_mode_controller
        self.history_list_generator = HistoryListGenerator(self.get_modeler())
        # self.report_information(self.__get_welcome_message())

    def get_history_list_generator(self) -> HistoryListGenerator:
        return self.history_list_generator

    def run_vba(self, vba_code: str) -> bool:
        modeler = self.get_modeler()
        if modeler is None:
            return False
        else:
            return modeler.run_vba(vba_code)

    def invoke_function(self, function_name: str, *args: Union[str, int, float, bool]) -> bool:
        modeler = self.get_modeler()
        if modeler is None:
            return False
        else:
            return modeler.invoke_function(function_name, *args)

    def invoke_method(
            self, object_name: str, function_name: str, *args: Union[str, int, float, bool]):
        modeler = self.get_modeler()
        if modeler is None:
            return False
        else:
            return modeler.invoke_method(object_name, function_name, *args)

    def query_vba(self, vba_code: str) -> Optional[str]:
        modeler = self.get_modeler()
        if modeler is None:
            return None
        else:
            modeler.report_vba(vba_code)
            return self.get_last_message_text()

    def query_function(
            self, function_name: str, *args: Union[str, int, float, bool]) -> Optional[str]:
        modeler = self.get_modeler()
        if modeler is None:
            return None
        else:
            modeler.report_function(function_name, *args)
            return self.get_last_message_text()

    def query_method(
            self, object_name: str, function_name: str,
            *args: Union[str, int, float, bool]) -> Optional[str]:
        modeler = self.get_modeler()
        if modeler is None:
            return None
        else:
            modeler.report_method(object_name, function_name, *args)
            return self.get_last_message_text()

    def query_function_t(
            self, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]) -> Optional[tuple]:
        modeler = self.get_modeler()
        if modeler is None:
            return None
        else:
            modeler.report_function_t(function_name, return_type, *args)
            type_names = get_types_vba_t(return_type, *args)
            res_parts = self.get_last_message_text().split(',')
            if len(type_names) != len(res_parts):
                raise RuntimeError('Invalid number of return values')
            res = []
            for i in range(len(type_names)):
                res.append(cast_vba_value(res_parts[i], type_names[i]))
            return tuple(res)

    def query_method_t(
            self, object_name: str, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]) -> Optional[tuple]:
        modeler = self.get_modeler()
        if modeler is None:
            return None
        else:
            modeler.report_method_t(object_name, function_name, return_type, *args)
            type_names = get_types_vba_t(return_type, *args)
            res_parts = self.get_last_message_text().split(',')
            if len(type_names) != len(res_parts):
                raise RuntimeError('Invalid number of return values')
            res = []
            for i in range(len(type_names)):
                res.append(cast_vba_value(res_parts[i], type_names[i]))
            return tuple(res)

    def get_quiet_mode_controller(self) -> IQuietModeController:
        return self.quiet_mode_controller

    def activate(self) -> None:
        self.native_obj.activate()

    def close(self) -> None:
        self.native_obj.close()

    def get_file_name(self) -> str:
        return self.native_obj.filename()

    def get_folder(self) -> str:
        return self.native_obj.folder()

    def get_messages(self) -> list:
        msgs = self.native_obj.get_messages()
        return [] if msgs is None else msgs

    def get_last_message_text(self) -> Optional[str]:
        msgs = self.get_messages()
        return None if len(msgs) == 0 else msgs[-1]['text']

    def get_kind(self) -> Kind:
        return Project.Kind.from_cst(self.native_obj.project_type())

    def save(self, path: str, include_results: bool = True) -> None:
        self.native_obj.save(path, include_results)

    def get_modeler(self) -> Modeler:
        return None if self.native_obj.modeler is None else Modeler(self.native_obj.modeler)

    def get_schematic(self) -> Schematic:
        return None if self.native_obj.schematic is None else Schematic(self.native_obj.schematic)

    def get_interface_pcbs(self) -> InterfacePCBS:
        return None if self.native_obj.pcbs is None else InterfacePCBS(self.native_obj.pcbs)

    def generate_history_list_from_cache(self) -> None:
        self.get_history_list_generator().generate_cache()

    def get_parameters(self) -> Parameters:
        return Parameters(self)

    def reset_all(self):
        self.invoke_function('ResetAll')

    def set_screen_updating(self, flag: bool = True):
        self.invoke_function('ScreenUpdating', flag)

    def select_quick_start_guide(self, guide_type: str):
        self.invoke_function('SelectQuickStartGuide', guide_type)

    def select_tree_item(self, item_name: str):
        self.quiet_mode_controller.store_and_disable_quiet_mode()
        self.invoke_function('SelectTreeItem', item_name)
        self.quiet_mode_controller.restore_quiet_mode()

    def get_number_of_selected_tree_items(self) -> int:
        return int(self.query_function('GetNumberOfSelectedTreeItems'))

    def get_selected_tree_item(self) -> str:
        return self.query_function('GetSelectedTreeItem')

    def get_next_selected_tree_item(self) -> str:
        return self.query_function('GetNextSelectedTreeItem')

    def set_lock(self, flag: bool = True):
        self.invoke_function('SetLock', flag)

    def lock(self, flag):
        self.invoke_function('SetLock', True)

    def unlock(self):
        self.invoke_function('SetLock', False)

    def save_as(self, new_path: str, include_results: bool = False):
        new_path = os.path.abspath(new_path)
        self.invoke_function('SaveAs', new_path, include_results)

    def store_in_archive(
            self, path: str, keep_all_results: bool = True, keep_1d_results: bool = True,
            keep_farfield_data: bool = True, delete_project_folder: bool = False):
        self.invoke_function('StoreInArchive',
            path, keep_all_results, keep_1d_results, keep_farfield_data, delete_project_folder)

    def clear_global_data_values(self):
        self.invoke_function('ClearGlobalDataValues')

    def delete_global_data_values(self, name: str):
        self.invoke_function('DeleteGlobalDataValue', name)

    def restore_global_data_value(self, name: str) -> str:
        return self.query_function('RestoreGlobalDataValue', name)

    def store_global_data_value(self, name: str, value):
        self.invoke_function('StoreGlobalDataValue', name, value)

    def reset_global_data_storage(self):
        self.invoke_function('ResetGlobalDataStorage')

    def set_global_data(self, name: str, value):
        self.invoke_function('SetGlobalData', name, value)

    def get_global_data(self, name: str) -> str:
        return self.query_function('GetGlobalData', name)

    def evaluate(self, expression) -> str:
        return self.query_function('Evaluate', expression)

    def set_activate_script_settings(self, switch: bool = True):
        self.invoke_function('ActivateScriptSettings', switch)

    def clear_script_settings(self):
        self.invoke_function('ClearScriptSettings')

    def get_script_setting(self, name: str, default_value: str) -> str:
        return self.query_function('GetScriptSetting', name, default_value)

    def store_script_setting(self, name: str, value: str) -> str:
        self.invoke_function('StoreScriptSetting', name, value)

    def store_template_setting(self, name: str, value: str) -> str:
        self.invoke_function('StoreTemplateSetting', name, value)

    def get_script_file_name(self) -> str:
        return self.query_function('GetScriptFileName')

    def evaluate_result_templates(self):
        self.invoke_function('EvaluateResultTemplates')

    def set_application_name(self, name: str):
        self.invoke_function('SetApplicationName', name)

    def reset_application_name(self):
        self.invoke_function('ResetApplicationName')

    def reset_template_iterator(self):
        self.invoke_function('ResetTemplateIterator')

    def set_template_filter(self, filter_name: str, value: str):
        self.invoke_function('SetTemplateFilter', filter_name, value)

    def get_next_template(
            self, result_name: str, val_type: str, template_name: str, folder: str) -> bool:
        return self.query_function(
            'GetNextTemplate', result_name, val_type, template_name, folder) != 'False'

    def get_file_type(self, file_path: str) -> str:
        return self.query_function('GetFileType', file_path)

    def get_first_table_result(self, result_name: str) -> str:
        return self.query_function('GetFirstTableResult', result_name)

    def get_next_table_result(self, result_name: str) -> str:
        return self.query_function('GetNextTableResult', result_name)

    def was_template_aborted(self) -> bool:
        return self.query_function('GetTemplateAborted') != 'False'

    def get_macro_path(self) -> str:
        return self.invoke_function('GetMacroPath')

    def get_macro_path_from_index(self, index: int) -> str:
        return self.invoke_function('GetMacroPathFromIndex', index)

    def get_number_of_macro_paths(self) -> int:
        return int(self.invoke_function('GetNumberOfMacroPaths'))

    def run_and_wait(self, command: str):
        self.invoke_function('RunAndWait', command)

    def run_macro(self, macro_name: str):
        self.invoke_function('RunMacro', macro_name)

    def run_script(self, script_name: str):
        self.invoke_function('RunScript', script_name)

    def report_information(self, *msg):
        self.invoke_function('ReportInformation', ''.join(list(map(lambda x: str(x), msg))))

    def report_warning(self, *msg):
        self.invoke_function('ReportWarning', ''.join(list(map(lambda x: str(x), msg))))

    def report_information_to_window(self, *msg):
        self.invoke_function('ReportInformationToWindow', ''.join(list(map(lambda x: str(x), msg))))

    def report_warning_to_window(self, *msg):
        self.invoke_function('ReportWarningToWindow', ''.join(list(map(lambda x: str(x), msg))))

    def report_error(self, *msg):
        self.invoke_function('ReportError', ''.join(list(map(lambda x: str(x), msg))))

    def set_common_mpi_cluster_config(
            self, install_folder: str, temp_folder: str, architecture: str):
        self.invoke_function('SetCommonMPIClusterConfig', install_folder, temp_folder, architecture)

    def set_common_mpi_cluster_login_info(self, user_name: str, private_key_file_path: str):
        self.invoke_function('SetCommonMPIClusterLoginInfo', user_name, private_key_file_path)

    def get_mpi_cluster_size(self) -> int:
        return int(self.query_function('GetMPIClusterSize'))

    def clear_mpi_cluster_config(self):
        self.invoke_function('ClearMPIClusterConfig')

    def add_mpi_cluster_node_config(
            self, host_name: str, install_folder: str, temp_folder: str, architecture: str,
            active: bool = True):
        self.invoke_function(
            'AddMPIClusterNodeConfig', host_name, install_folder, temp_folder,
            architecture, active)

    def import_xy_curve_from_ascii_file(self, folder_name: str, file_path: str):
        self.invoke_function('ImportXYCurveFromASCIIFile', folder_name, file_path)

    def paste_curves_from_ascii_file(self, folder_name: str, file_path: str):
        self.invoke_function('PasteCurvesFromASCIIFile', folder_name, file_path)

    def paste_curves_from_clipboard(self, folder_name: str):
        self.invoke_function('PasteCurvesFromClipboard', folder_name)

    def scale_curves(self, folder_name: str, x_scale: float, y_scale: float):
        self.invoke_function('ScaleCurves', folder_name, x_scale, y_scale)

    def store_curves_in_ascii_files(self, file_name: str):
        self.invoke_function('StoreCurvesInASCIIFile', file_name)

    def store_curves_in_clipboard(self):
        self.invoke_function('StoreCurvesInClipboard')

    def delete_results(self):
        self.invoke_function('DeleteResults')

    def get_field_frequency(self) -> float:
        return float(self.query_function('GetFieldFrequency'))

    def get_application_name(self) -> str:
        return self.query_function('GetApplicationName')

    def get_application_version(self) -> str:
        return self.query_function('GetApplicationVersion')

    def get_install_path(self) -> str:
        return self.query_function('GetInstallPath')

    def get_project_path(self, path_type: str) -> str:
        return self.query_function('GetProjectPath', path_type)

    def is_building_model(self) -> bool:
        return self.query_function('IsBuildingModel') != 'False'

    def get_license_host_id(self) -> str:
        return self.query_function('GetLicenseHostId')

    def get_license_customer_number(self) -> str:
        return self.query_function('GetLicenseCustomerNumber')

    def rebuild(self):
        self.invoke_function('Rebuild')

    def rebuild_on_parametric_change(self):
        show_msg_box = self.interface.is_in_quiet_mode()
        full_rebuild = False
        self.invoke_function('RebuildOnParametricChange', full_rebuild, show_msg_box)

    def rebuild_fully_on_parametric_change(self):
        show_msg_box = self.interface.is_in_quiet_mode()
        full_rebuild = True
        self.invoke_function('RebuildOnParametricChange', full_rebuild, show_msg_box)

    def get_pickpoint_coords(self, pickpoint_id: int) -> tuple[float, float, float]:
        x = float(self.query_function('xp', pickpoint_id))
        y = float(self.query_function('yp', pickpoint_id))
        z = float(self.query_function('zp', pickpoint_id))
        return (x, y, z)

    def export_image_to_file(self, path: str, width: int = 0, height: int = 0):
        self.invoke_function('ExportImageToFile', path, width, height)

    def export_image_to_clipboard(self, width: int = 0, height: int = 0):
        self.invoke_function('ExportImageToClipboard', width, height)

    # def __get_welcome_message(self):
    #     return \
    #         f'CST Studio Suite Python interface v{info.MODULE_VERSION} by '+\
    #         f'Samuel Travnicek connected.'