from . import VBATypeName
from typing import Union, Optional

def construct_function(function_name: str, *args: Union[str, int, float, bool]) -> str:
    args_as_strings = [f'"{arg}"' if isinstance(arg, str) else str(arg) for arg in args]
    args_str = ", ".join(args_as_strings)
    return f'{function_name}({args_str})'

def construct_method(
        object_name: str, function_name: str, *args: Union[str, int, float, bool]) -> str:
    args_as_strings = [f'"{arg}"' if isinstance(arg, str) else str(arg) for arg in args]
    args_str = ", ".join(args_as_strings)
    return f'{object_name}.{function_name}({args_str})'

def get_num_vars(*args: Union[str, int, float, bool, VBATypeName]):
    num_vars = 0
    for arg in args:
        if isinstance(arg, VBATypeName):
            num_vars += 1
    return num_vars

def generate_variables_lines(
        return_type: Optional[VBATypeName], *args: Union[str, int, float, bool, VBATypeName]):
    variables = ''
    if return_type is not None:
        variables += f'Dim r As {return_type.value}\n'
    arg_cntr = 0
    for arg in args:
        if isinstance(arg, VBATypeName):
            variables += f'Dim var{arg_cntr} As {arg.value}\n'
        arg_cntr += 1
    return variables

def generate_statement_line(
        object_name: Optional[str], function_name: str, return_type: Optional[VBATypeName],
        *args: Union[str, int, float, bool, VBATypeName]):
    statement = ''
    if return_type is not None:
        statement += 'r = '
    if object_name is not None:
        statement += f'{object_name}.'
    statement += f'{function_name}('
    arg_cntr = 0
    for arg in args:
        if arg_cntr != 0:
            statement += ','
        if isinstance(arg, VBATypeName):
            statement += f'var{arg_cntr}'
        elif isinstance(arg, str):
            statement += f'"{arg}"'
        else:
            statement += f'{arg}'
        arg_cntr += 1
    statement += ')'
    return statement

def generate_report_line(
        return_type: Optional[VBATypeName], *args: Union[str, int, float, bool, VBATypeName]):
    if get_num_vars(*args) == 0 and return_type is None:
        return ''
    report = 'ReportInformation('
    if return_type is not None:
        report += 'r'
        if get_num_vars(*args) > 0:
            report += ' & "," & '
    var_cntr = 0
    arg_cntr = 0
    for arg in args:
        if isinstance(arg, VBATypeName):
            if var_cntr != 0:
                report += ' & "," & '
            report += f'var{arg_cntr}'
            var_cntr += 1
        arg_cntr += 1
    report += ' & "")'
    return report

class IVBARuntime:
    def run_vba(self, vba_code: str) -> bool:
        return False

    def invoke_function(self, function_name: str, *args: Union[str, int, float, bool]):
        self.run_vba(construct_function(function_name, *args))

    def invoke_method(
            self, object_name: str, function_name: str, *args: Union[str, int, float, bool]):
        self.run_vba(construct_method(object_name, function_name, *args))

    def report_vba(self, vba_code: str) -> bool:
        return False

    def report_function(self, function_name: str, *args: Union[str, int, float, bool]):
        self.report_vba(construct_function(function_name, *args))

    def report_method(
            self, object_name: str, function_name: str, *args: Union[str, int, float, bool]):
        self.report_vba(construct_method(object_name, function_name, *args))

    def report_function_t(
            self, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]):
        variables = generate_variables_lines(return_type, *args)
        statement = generate_statement_line(None, function_name, return_type, *args)
        report = generate_report_line(return_type, *args)
        self.run_vba(f'{variables}{statement}\n{report}')

    def report_method_t(
            self, object_name: str, function_name: str, return_type: Optional[VBATypeName],
            *args: Union[str, int, float, bool, VBATypeName]):
        variables = generate_variables_lines(return_type, *args)
        statement = generate_statement_line(object_name, function_name, return_type, *args)
        report = generate_report_line(return_type, *args)
        self.run_vba(f'{variables}{statement}\n{report}')
