from . import IVBAProvider, VBAObjWrapper

class Align(VBAObjWrapper):
    ALIGN_WHAT_SHAPE = 'Shape'
    ALIGN_WHAT_SUBPROJECT = 'Subproject'
    ALIGN_WHAT_PART = 'Part'
    ALIGN_WHAT_MIXED = 'Mixed'

    ALIGN_HOW_FACES = 'Faces'
    ALIGN_HOW_ROTATE = 'Rotate'
    ALIGN_HOW_ROTATE_BY_ANGLE = 'RotateByDegree'

    PICK_WHAT_SOURCE_PLANE = 'SourcePlane'
    PICK_WHAT_TARGET_PLANE = 'TargetPlane'
    PICK_WHAT_ZERO_ANGLE = 'ZeroAngle'
    PICK_WHAT_FINAL_ANGLE = 'FinalAngle'

    PICK_KIND_FACE = 'Face'
    PICK_KIND_EDGE = 'Edge'
    PICK_KIND_POINT = 'Point'

    NUMERICAL_VALUE_ANGLE = 'Angle'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Align')

    def reset(self):
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def add_name(self, name: str):
        self.record_method('AddName', name)

    def align(self, what: str, how: str):
        self.record_method('Align', what, how)

    def set_kind_of_pick_for(self, what: str, kind: str):
        self.record_method('SetKindOfPickFor', what, kind)

    def set_name_to_step(self, what: str, name: str):
        self.record_method('SetNameToStep', what. name)

    def set_numerical_value(self, what: str, value: float):
        self.record_method('SetNumericalValue', what, value)

    def set_opposite_face_orientation(self, flag: bool = True):
        self.record_method('SetOppositeFaceOrientation', flag)

    def set_clear_subproject_import_info(self, flag: bool = True):
        self.record_method('ClearSubProjectImportInfo', flag)

    #TODO: implement methods {specializations of enum values}