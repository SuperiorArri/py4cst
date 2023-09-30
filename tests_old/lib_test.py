import sys
import os
from pathlib import Path

def get_input_file_path(relative_file_path) -> Path:
    return _get_relative_file_path('input', relative_file_path)

def get_output_file_path(relative_file_path) -> Path:
    return _get_relative_file_path('output', relative_file_path)

def get_tests_dir():
    return TESTS_DIR

def get_lib_dir():
    return LIB_DIR

def finalize():
    print('Test finished with success.')

def _get_relative_file_path(subdir_path, relative_file_path):
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_file_path = os.path.join(current_dir_path, subdir_path, relative_file_path)
    return Path(abs_file_path)

def _ensure_subdir_exists(subdir_path):
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_file_path = os.path.join(current_dir_path, subdir_path)
    if not os.path.exists(abs_file_path):
        os.makedirs(abs_file_path)

####################################################################################################

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_DIR = os.path.join(os.path.dirname(TESTS_DIR), 'lib')

sys.path.append(LIB_DIR)
_ensure_subdir_exists('output')