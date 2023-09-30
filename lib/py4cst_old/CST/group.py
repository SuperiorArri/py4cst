from . import Project
from . import ComObjectWrapper

class Group(ComObjectWrapper):
    TYPE_NORMAL = 'normal'
    TYPE_MESH = 'mesh'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Group

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def create(self, name: str, group_type: str = TYPE_NORMAL):
        #BUG: group is not visible after creating (CST Studio Suite bug)
        self.invoke_method('Add', name, group_type)

    def delete(self, name: str):
        self.invoke_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.invoke_method('Rename', old_name, new_name)

    def add_item(self, item_name: str, group_name: str):
        self.invoke_method('AddItem', item_name, group_name)

    def remove_item(self, item_name: str, group_name: str):
        self.invoke_method('RemoveItem', item_name, group_name)

    def create_folder(self, name: str):
        self.invoke_method('NewFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.invoke_method('RenameFolder', old_name, new_name)

    def delete_folder(self, name: str):
        self.invoke_method('DeleteFolder', name)

    def reset(self):
        self.invoke_method('Reset')