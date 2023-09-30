from . import Project
from . import ComObjectWrapper

class ResultTree(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.ResultTree

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def enable_update(self, flag: bool = True):
        self.invoke_method('EnableTreeUpdate', flag)

    def disable_update(self, flag: bool = True):
        self.invoke_method('EnableTreeUpdate', not flag)

    def get_first_child_name(self, parent_item: str) -> str:
        return self.invoke_method('GetFirstChildName', parent_item)

    def get_next_item_name(self, current_item: str) -> str:
        return self.invoke_method('GetNextItemName', current_item)

    def refresh_view(self):
        self.invoke_method('RefreshView')

    def has_item(self, item: str):
        return self.invoke_method('DoesTreeItemExist', item)