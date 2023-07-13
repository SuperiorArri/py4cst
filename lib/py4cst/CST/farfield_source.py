from . import Project
from . import ComObjectWrapper

class FarfieldSource(ComObjectWrapper):
    ALIGNMENT_CUSTOM = 'user'
    ALIGNMENT_CURRENT_WCS = 'currentwcs'
    ALIGNMENT_SOURCE_FILE = 'sourcefile'

    CALC_MODE_AUTOMATIC = 'automatic'
    CALC_MODE_CUSTOM = 'user defined'
    CALC_MODE_AUTOTRUNCATION = 'autotruncation'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.FarfieldSource

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_id(self, id: int):
        self.invoke_method('Id', id)

    def set_position(self, x: float, y: float, z: float):
        self.invoke_method('SetPosition', x, y, z)

    def set_phi0_vec(self, x: float, y: float, z: float):
        self.invoke_method('SetPhi0XYZ', x, y, z)

    def set_theta0_vec(self, x: float, y: float, z: float):
        self.invoke_method('SetTheta0XYZ', x, y, z)

    def import_from_file(self, file_path: str):
        self.invoke_method('Import', file_path)

    def set_use_copy_only(self, flag: bool = True):
        self.invoke_method('UseCopyOnly', flag)

    def set_use_multipole_ffs(self, flag: bool = True):
        self.invoke_method('UseMultipoleFFS', flag)

    def set_alignment_type(self, alignment_type: str):
        self.invoke_method('SetAlignmentType', alignment_type)

    def set_multipole_degree(self, degree: int):
        self.invoke_method('SetMultipoleDegree', degree)

    def set_multipole_calc_mode(self, mode: str):
        self.invoke_method('SetMultipoleCalcMode', mode)

    def store(self):
        self.invoke_method('Store')

    def delete(self):
        self.invoke_method('Delete')

    def delete_all(self):
        self.invoke_method('DeleteAll')

    def get_next_id(self) -> int:
        return self.invoke_method('GetNextId')