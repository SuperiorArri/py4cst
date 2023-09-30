from . import IVBAProvider, VBAObjWrapper

class LayerStacking(VBAObjWrapper):
    MATERIAL_NORMAL = 'normal'
    MATERIAL_PEC = 'pec'

    THERMAL_TYPE_NORMAL = 'normal'
    THERMAL_TYPE_PTC = 'ptc'

    NORMAL_DIRECTION_X = 'x'
    NORMAL_DIRECTION_Y = 'y'
    NORMAL_DIRECTION_Z = 'z'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'LayerStacking')

    def reset(self):
        self.record_method('Reset')

    def set_layer_stacking_active(self, flag: bool = True):
        self.record_method('LayerStackingActive', flag)

    def set_background_items_align_value(self, value: float):
        self.record_method('AlignValueBackgroundItems', value)

    def set_background_items_normal(self, direction: str):
        self.record_method('NormalBackgroundItems', direction)

    def set_invert_direction(self, flag: bool = True):
        self.record_method('InvertDirection', flag)

    def set_fix_traversal(self, flag: bool = True):
        self.record_method('FixTransversal', flag)

    def add_item(self, index: int, height: float, material_name: str):
        self.record_method('AddItem', index, height, material_name)