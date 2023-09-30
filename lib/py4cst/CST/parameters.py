from . import IVBAProvider, VBATypeName
from typing import Union, Optional

class Parameters:
    def __init__(self, vbap: IVBAProvider) -> None:
        self.vbap = vbap

    def invoke_fn(self, name: str, *args) -> None:
        self.vbap.invoke_function(name, *args)

    def query_fn(self, name: str, *args) -> str:
        self.vbap.query_function(name, *args)

    def delete(self, name: str):
        self.invoke_fn('DeleteParameter', name)

    def has(self, name: str) -> bool:
        return self.query_fn('DoesParameterExist', name) != 'False'

    def get_count(self) -> int:
        return int(self.query_fn('GetNumberOfParameters'))

    def get_name(self, index: int) -> str:
        return self.query_fn('GetParameterName', index)

    def get_value(self, index: int) -> float:
        return float(self.query_fn('GetParameterNValue', index))

    def get_expression(self, index: int) -> str:
        return self.query_fn('GetParameterSValue', index)

    def rename(self, old_name: str, new_name: str):
        self.invoke_fn('RenameParameter', old_name, new_name)

    def restore(self, name: str) -> str:
        return self.query_fn('RestoreParameter', name)

    def restore_as_number(self, name: str) -> float:
        return float(self.query_fn('RestoreDoubleParameter', name))

    def restore_expression(self, name: str) -> str:
        return self.query_fn('RestoreParameterExpression', name)

    def store(
            self, name: str, expression: Union[str, int, float],
            description: Optional[str] = None):
        if description is None:
            self.invoke_fn('StoreParameter', name, str(expression))
        else:
            self.invoke_fn('StoreParameterWithDescription', name, expression, description)

    def ensure_exists(self, name: str, default_expression: Union[str, int, float]):
        self.invoke_fn('MakeSureParameterExists', name, default_expression)

    def does_project_depend_on(self, param_name: str) -> bool:
        return self.query_fn('DoesProjectDependOnParameter', param_name) != 'False'

    def set_description(self, name: str, description: str):
        self.invoke_fn('SetParameterDescription', name, description)

    def get_description(self, name: str) -> str:
        return self.query_fn('GetParameterDescription', name)

    # returns: (names_var, values_var) or None
    def get_combination(self, result_id: str) -> Optional[tuple[str, str]]:
        B, V = VBATypeName.Boolean, VBATypeName.Variant
        res = self.vbap.query_function_t('GetParameterCombination', B, result_id, V, V)
        return None if not res[0] else res[1:]