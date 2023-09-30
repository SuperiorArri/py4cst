from . import IVBAProvider, VBAObjWrapper

class TraceFromCurve(VBAObjWrapper):
    GAP_TYPE_ROUNDED = 0
    GAP_TYPE_EXTENDED = 1
    GAP_TYPE_NATURAL = 2

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'TraceFromCurve')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def set_component(self, component_name: str):
        self.record_method('Component', component_name)

    def set_material(self, mat_name: str):
        self.record_method('Material', mat_name)

    def set_curve(self, curve_name: str):
        self.record_method('Curve', curve_name)

    def set_thickness(self, thickness: float):
        self.record_method('Thickness', thickness)

    def set_width(self, width: float):
        self.record_method('Width', width)

    def set_start_round(self, flag: bool = True):
        self.record_method('RoundStart', flag)

    def set_end_round(self, flag: bool = True):
        self.record_method('RoundEnd', flag)

    def set_gap_type(self, gap_type: int):
        self.record_method('GapType', gap_type)

    def create(self):
        #TODO: check if Create or CreateNew
        self.record_method('Create')