from . import IVBAProvider, VBAObjWrapper

class Group(VBAObjWrapper):
    TYPE_NORMAL = 'normal'
    TYPE_MESH = 'mesh'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Group')

    def create(self, name: str, group_type: str = TYPE_NORMAL):
        self.record_method('Add', name, group_type)

    def delete(self, name: str):
        self.record_method('Delete', name)

    def rename(self, old_name: str, new_name: str):
        self.record_method('Rename', old_name, new_name)

    def add_item(self, item_name: str, group_name: str):
        self.record_method('AddItem', item_name, group_name)

    def remove_item(self, item_name: str, group_name: str):
        self.record_method('RemoveItem', item_name, group_name)

    def create_folder(self, name: str):
        self.record_method('NewFolder', name)

    def rename_folder(self, old_name: str, new_name: str):
        self.record_method('RenameFolder', old_name, new_name)

    def delete_folder(self, name: str):
        self.record_method('DeleteFolder', name)

    def reset(self):
        self.record_method('Reset')