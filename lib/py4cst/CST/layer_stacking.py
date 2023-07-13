from . import Project
from . import ComObjectWrapper

class LayerStacking(ComObjectWrapper):
    MATERIAL_NORMAL = 'normal'
    MATERIAL_PEC = 'pec'

    THERMAL_TYPE_NORMAL = 'normal'
    THERMAL_TYPE_PTC = 'ptc'

    NORMAL_DIRECTION_X = 'x'
    NORMAL_DIRECTION_Y = 'y'
    NORMAL_DIRECTION_Z = 'z'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.LayerStacking

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_layer_stacking_active(self, flag: bool = True):
        self.invoke_method('LayerStackingActive', flag)

    def set_background_items_align_value(self, value: float):
        self.invoke_method('AlignValueBackgroundItems', value)

    def set_background_items_normal(self, direction: str):
        self.invoke_method('NormalBackgroundItems', direction)

    def set_invert_direction(self, flag: bool = True):
        self.invoke_method('InvertDirection', flag)

    def set_fix_traversal(self, flag: bool = True):
        self.invoke_method('FixTransversal', flag)

    def add_item(self, index: int, height: float, material_name: str):
        self.invoke_method('AddItem', index, height, material_name)