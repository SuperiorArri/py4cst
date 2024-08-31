from . import IVBAProvider, VBAObjWrapper

class FarfieldSource(VBAObjWrapper):
    ALIGNMENT_CUSTOM = 'user'
    ALIGNMENT_CURRENT_WCS = 'currentwcs'
    ALIGNMENT_SOURCE_FILE = 'sourcefile'

    CALC_MODE_AUTOMATIC = 'automatic'
    CALC_MODE_CUSTOM = 'user defined'
    CALC_MODE_AUTOTRUNCATION = 'autotruncation'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'FarfieldSource')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def set_id(self, id: int):
        self.cache_method('Id', id)

    def set_position(self, x: float, y: float, z: float):
        self.cache_method('SetPosition', x, y, z)

    def set_phi0_vec(self, x: float, y: float, z: float):
        self.cache_method('SetPhi0XYZ', x, y, z)

    def set_theta0_vec(self, x: float, y: float, z: float):
        self.cache_method('SetTheta0XYZ', x, y, z)

    def import_from_file(self, file_path: str):
        self.cache_method('Import', file_path)

    def set_use_copy_only(self, flag: bool = True):
        self.cache_method('UseCopyOnly', flag)

    def set_use_multipole_ffs(self, flag: bool = True):
        self.cache_method('UseMultipoleFFS', flag)

    def set_alignment_type(self, alignment_type: str):
        self.cache_method('SetAlignmentType', alignment_type)

    def set_multipole_degree(self, degree: int):
        self.cache_method('SetMultipoleDegree', degree)

    def set_multipole_calc_mode(self, mode: str):
        self.cache_method('SetMultipoleCalcMode', mode)

    def store(self):
        self.cache_method('Store')
        self.flush_cache('Store FarfieldSource')

    def delete(self):
        self.record_method('Delete')

    def delete_all(self):
        self.record_method('DeleteAll')

    def get_next_id(self) -> int:
        return self.query_method_int('GetNextId')