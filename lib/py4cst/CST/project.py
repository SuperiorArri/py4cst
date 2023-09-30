# from . import info
from . import \
    IProject, IVBAProvider, Modeler, Schematic, InterfacePCBS, HistoryListGenerator, Parameters, \
    VBATypeName, IQuietModeController
from enum import Enum
from typing import Optional, Union

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
    class Kind(Enum):
        from cst.interface import ProjectType
        DesignStudio = ProjectType.DS
        MicrowaveStudio = ProjectType.MWS
        EMStudio = ProjectType.EMS
        ParticleStudio = ProjectType.PS
        MphysicsStudio = ProjectType.MPS
        CableStudio = ProjectType.CS
        PCBStudio = ProjectType.PCBS
        FilterDesigner3D = ProjectType.FD3D

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
            *args: Union[str, int, float, bool, VBATypeName]) -> tuple:
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
            *args: Union[str, int, float, bool, VBATypeName]) -> tuple:
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
        return Project.Kind(self.native_obj.project_type())

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

    # def __get_welcome_message(self):
    #     return \
    #         f'CST Studio Suite Python interface v{info.MODULE_VERSION} by '+\
    #         f'Samuel Travnicek connected.'