from . import IVBAProvider, VBAObjWrapper

class Transform(VBAObjWrapper):
    TRANSFORM_WHAT_SHAPE = 'Shape'
    TRANSFORM_WHAT_ANCHOR_POINT = 'Anchorpoint'
    TRANSFORM_WHAT_FACE = 'Face'
    TRANSFORM_WHAT_MESH_SHAPE = 'Meshshape'
    TRANSFORM_WHAT_PROBE = 'Probe'
    TRANSFORM_WHAT_VOXEL_DATA = 'Voxeldata'
    TRANSFORM_WHAT_MIXED = 'mixed'
    TRANSFORM_WHAT_FFS = 'FFS'
    TRANSFORM_WHAT_HF_3D_MONITOR = 'HF3DMonitor'
    TRANSFORM_WHAT_PORT = 'Port'
    TRANSFORM_WHAT_LUMPED_ELEMENT = 'Lumpedelement'
    TRANSFORM_WHAT_CURRENT_DISTRIBUTION = 'Currentdistribution'
    TRANSFORM_WHAT_COIL = 'Coil'
    TRANSFORM_WHAT_CURRENT_MONITOR = 'currentmonitor'
    TRANSFORM_WHAT_CURRENT_WIRE = 'currentwire'
    TRANSFORM_WHAT_VOLTAGE_MONITOR = 'voltagemonitor'
    TRANSFORM_WHAT_VOLTAGE_WIRE = 'voltagewire'

    TRANSFORM_HOW_TRANSLATE = 'Translate'
    TRANSFORM_HOW_ROTATE = 'Rotate'
    TRANSFORM_HOW_SCALE = 'Scale'
    TRANSFORM_HOW_MIRROR = 'Mirror'
    TRANSFORM_HOW_MATRIX = 'Matrix'
    TRANSFORM_HOW_LOCAL_TO_GLOBAL = 'LocalToGlobal'
    TRANSFORM_HOW_GLOBAL_TO_LOCAL = 'GlobalToLocal'

    ORIGIN_SHAPE_CENTER = 'ShapeCenter'
    ORIGIN_COMMON_CENTER = 'CommonCenter'
    ORIGIN_FREE = 'Free'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Transform')

    def reset(self):
        self.cache_method('Reset')

    def set_name(self, name: str):
        self.cache_method('Name', name)

    def add_name(self, name: str):
        self.cache_method('AddName', name)

    def translate_curve(self):
        self.cache_method('TranslateCurve')
        self.flush_cache('Transform: TranslateCurve')

    def scale_curve(self):
        self.cache_method('ScaleCurve')
        self.flush_cache('Transform: ScaleCurve')

    def rotate_curve(self):
        self.cache_method('RotateCurve')
        self.flush_cache('Transform: RotateCurve')

    def mirror_curve(self):
        self.cache_method('MirrorCurve')
        self.flush_cache('Transform: MirrorCurve')

    def translate_wire(self):
        self.cache_method('TranslateWire')
        self.flush_cache('Transform: TranslateWire')

    def scale_wire(self):
        self.cache_method('ScaleWire')
        self.flush_cache('Transform: ScaleWire')

    def rotate_wire(self):
        self.cache_method('RotateWire')
        self.flush_cache('Transform: RotateWire')

    def mirror_wire(self):
        self.cache_method('MirrorWire')
        self.flush_cache('Transform: MirrorWire')

    def translate_coil(self):
        self.cache_method('TranslateCoil')
        self.flush_cache('Transform: TranslateCoil')

    def scale_coil(self):
        self.cache_method('ScaleCoil')
        self.flush_cache('Transform: ScaleCoil')

    def rotate_coil(self):
        self.cache_method('RotateCoil')
        self.flush_cache('Transform: RotateCoil')

    def mirror_coil(self):
        self.cache_method('MirrorCoil')
        self.flush_cache('Transform: MirrorCoil')

    def transform(self, what: str, how: str):
        self.cache_method('Transform', what, how)
        self.flush_cache('Transform')

    def set_use_picked_points(self, flag: bool = True):
        self.cache_method('UsePickedPoints', flag)

    def set_invert_picked_points(self, flag: bool = True):
        self.cache_method('InvertPickedPoints', flag)

    def set_multiple_objects(self, flag: bool = True):
        self.cache_method('MultipleObjects', flag)

    def set_group_objects(self, flag: bool = True):
        self.cache_method('GroupObjects', flag)

    def set_origin(self, key: str):
        self.cache_method('Origin', key)

    def set_center(self, u: float, v: float, w: float):
        self.cache_method('Center', u, v, w)

    def set_vector(self, u: float, v: float, w: float):
        self.cache_method('Vector', u, v, w)

    def set_scale_factor(self, u: float, v: float, w: float):
        self.cache_method('ScaleFactor', u, v, w)

    def set_angle(self, u: float, v: float, w: float):
        self.cache_method('Angle', u, v, w)

    def set_plane_normal(self, u: float, v: float, w: float):
        self.cache_method('PlaneNormal', u, v, w)

    def set_matrix(
            self,
            c11: float, c12: float, c13: float,
            c21: float, c22: float, c23: float,
            c31: float, c32: float, c33: float):
        self.cache_method('Matrix', c11, c12, c13, c21, c22, c23, c31, c32, c33)

    def set_number_of_repetitions(self, count: int):
        self.cache_method('Repetitions', count)

    def set_component(self, name: str):
        self.cache_method('Component', name)

    def set_material(self, name: str):
        self.cache_method('Material', name)

    def set_multiple_selection(self, flag: bool = True):
        self.cache_method('MultipleSelection', flag)

    def set_destination(self, destination: str):
        self.cache_method('Destination', destination)

    def set_auto_destination(self, flag: bool = True):
        #NOTE: officially undocumented
        self.cache_method('AutoDestination', flag)

    def set_touch(self, flag: bool = True):
        self.cache_method('Touch', flag)

    def add_name_to_active_touch_set(self, name: str):
        self.cache_method('AddNameToActiveTouchSet', name)

    def add_name_to_passive_touch_set(self, name: str):
        self.cache_method('AddNameToPassiveTouchSet', name)

    def set_touch_tolerance(self, tolerance: float):
        self.cache_method('TouchTolerance', tolerance)

    def set_touch_max_num_iterations(self, count: int):
        self.cache_method('TouchMaxIterations', count)

    def set_touch_heuristic(self, flag: bool = True):
        self.cache_method('TouchHeuristic', flag)

    def set_touch_offset(self, offset: float):
        self.cache_method('TouchOffset', offset)