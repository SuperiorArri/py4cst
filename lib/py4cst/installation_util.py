import os
import sys
from typing import Optional, Union

def get_win_install_parent_path() -> str:
    return os.path.join('C:', os.sep, 'Program Files (x86)')

def get_win_install_path(cst_version: int) -> str:
    return os.path.join(get_win_install_parent_path(), f'CST Studio Suite {cst_version}')

def find_win_installed_versions() -> tuple[str]:
    res = []
    dir_path = get_win_install_parent_path()
    for file_path in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, file_path)):
            if file_path.startswith('CST Studio Suite '):
                res.append(file_path)
    return tuple(map(lambda x: int(x[17:]), res))

def get_win_latest_installed_version() -> Optional[int]:
    versions = find_win_installed_versions()
    return None if len(versions) == 0 else max(versions)

def add_win_installation_to_path_by_version(version: int):
    add_win_installation_to_path(get_win_install_path(version))

def add_win_installation_to_path(cst_install_dir: int):
    path = os.path.join(cst_install_dir, 'AMD64', 'python_cst_libraries')
    if os.path.isdir(path):
        sys.path.append(path)
    else:
        raise RuntimeError(
            'Failed to add the CST Python lib folder to path. '+
            f'Directory \'{path}\' doesn\'t exist.')

def load_win_cst_python_lib(version_or_install_dir: Optional[Union[int,str]] = None) -> None:
    if version_or_install_dir is None:
        version_or_install_dir = get_win_latest_installed_version()
        if version_or_install_dir is None:
            raise RuntimeError(
                'No CST Studio Suite installation directory found at standard paths. '+
                'Please provide the installation directory manually.')
    if isinstance(version_or_install_dir, int):
        add_win_installation_to_path_by_version(version_or_install_dir)
    else:
        add_win_installation_to_path(version_or_install_dir)