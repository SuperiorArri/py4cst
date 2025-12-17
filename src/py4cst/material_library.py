from .cst import Project
import os.path
from typing import Optional
import os.path

def get_win_library_path(cst_version: int) -> str:
    return f'C:\\Program Files (x86)\\CST Studio Suite {cst_version}\\Library\\Materials'

def get_default_win_material_path(cst_version: int, mat_name: str) -> str:
    return os.path.join(get_win_library_path(cst_version), f'{mat_name}.mtd')

def get_library_path(project: Project) -> str:
    return os.path.join(project.get_install_path(), 'Library', 'Materials')

def get_material_path(project: Project, mat_name: str) -> str:
    return os.path.join(get_library_path(project), f'{mat_name}.mtd')

def get_available_materials(project: Project) -> list[str]:
    material_names = []
    for file in os.listdir(get_library_path(project)):
        if file.endswith(".mtd"):
            material_names.append(file[:-4])
    return material_names

class Material:
    def __init__(self) -> None:
        self.commands = []
        self.curr_section = ''
        self.is_def_section = False
        self.custom_name = None
        self.loaded_name = ''

    def get_loaded_name(self) -> str:
        return self.loaded_name

    def set_custom_name(self, name: str):
        self.custom_name = name

    def get_custom_name(self) -> Optional[str]:
        return self.custom_name

    def load_from_file(self, file_path: str):
        file = open(file_path, 'r')
        self.__set_loaded_name(file_path)
        lines = file.readlines()
        for line in lines:
            self.__process_line(line)

    def __process_line(self, line: str):
        line = line.strip()
        if line.startswith('['):
            self.__process_section_line(line)
        elif len(line) == 0:
            pass
        elif self.is_def_section:
            self.__process_definition_line(line)
        else:
            pass

    def import_to_project(self, project: Project):
        project.get_modeler().add_to_history(
            f'Define material: {self.__get_name()}', self.__get_import_command())

    def __process_section_line(self, line: str):
        self.curr_section = line[1:-1]
        self.is_def_section = self.curr_section == 'Definition'

    def __process_definition_line(self, line: str):
        self.commands.append(line)

    def __get_import_command(self) -> str:
        return \
            'With Material\n'+\
            '.Reset\n'+\
            f'.Name "{self.__get_name()}"\n'+\
            '\n'.join(self.commands)+\
            '\nEnd With'

    def __set_loaded_name(self, file_path: str):
        self.loaded_name = os.path.basename(file_path).removesuffix('.mtd')

    def __get_name(self) -> str:
        if self.custom_name is not None:
            return self.custom_name
        else:
            return self.loaded_name
