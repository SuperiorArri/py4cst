from . import Project
from . import ComObjectWrapper

class Align(ComObjectWrapper):
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

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Align

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def add_name(self, name: str):
        self.invoke_method('AddName', name)

    def align(self, what: str, how: str):
        self.invoke_method('Align', what, how)

    def set_kind_of_pick_for(self, what: str, kind: str):
        self.invoke_method('SetKindOfPickFor', what, kind)

    def set_name_to_step(self, what: str, name: str):
        self.invoke_method('SetNameToStep', what. name)

    def set_numerical_value(self, what: str, value: float):
        self.invoke_method('SetNumericalValue', what, value)

    def set_opposite_face_orientation(self, flag: bool = True):
        self.invoke_method('SetOppositeFaceOrientation', flag)

    def set_clear_subproject_import_info(self, flag: bool = True):
        self.invoke_method('ClearSubProjectImportInfo', flag)

    #TODO: implement methods {specializations of enum values}