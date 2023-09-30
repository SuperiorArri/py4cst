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
        self.record_method('Reset')

    def set_name(self, name: str):
        self.record_method('Name', name)

    def add_name(self, name: str):
        self.record_method('AddName', name)

    def translate_curve(self):
        self.record_method('TranslateCurve')

    def scale_curve(self):
        self.record_method('ScaleCurve')

    def rotate_curve(self):
        self.record_method('RotateCurve')

    def mirror_curve(self):
        self.record_method('MirrorCurve')

    def translate_wire(self):
        self.record_method('TranslateWire')

    def scale_wire(self):
        self.record_method('ScaleWire')

    def rotate_wire(self):
        self.record_method('RotateWire')

    def mirror_wire(self):
        self.record_method('MirrorWire')

    def translate_coil(self):
        self.record_method('TranslateCoil')

    def scale_coil(self):
        self.record_method('ScaleCoil')

    def rotate_coil(self):
        self.record_method('RotateCoil')

    def mirror_coil(self):
        self.record_method('MirrorCoil')

    def transform(self, what: str, how: str):
        self.record_method('Transform', what, how)

    def set_use_picked_points(self, flag: bool = True):
        self.record_method('UsePickedPoints', flag)

    def set_invert_picked_points(self, flag: bool = True):
        self.record_method('InvertPickedPoints', flag)

    def set_multiple_objects(self, flag: bool = True):
        self.record_method('MultipleObjects', flag)

    def set_group_objects(self, flag: bool = True):
        self.record_method('GroupObjects', flag)

    def set_origin(self, key: str):
        self.record_method('Origin', key)

    def set_center(self, u: float, v: float, w: float):
        self.record_method('Center', u, v, w)

    def set_vector(self, u: float, v: float, w: float):
        self.record_method('Vector', u, v, w)

    def set_scale_factor(self, u: float, v: float, w: float):
        self.record_method('ScaleFactor', u, v, w)

    def set_angle(self, u: float, v: float, w: float):
        self.record_method('Angle', u, v, w)

    def set_plane_normal(self, u: float, v: float, w: float):
        self.record_method('PlaneNormal', u, v, w)

    def set_matrix(
            self,
            c11: float, c12: float, c13: float,
            c21: float, c22: float, c23: float,
            c31: float, c32: float, c33: float):
        self.record_method('Matrix', c11, c12, c13, c21, c22, c23, c31, c32, c33)

    def set_number_of_repetitions(self, count: int):
        self.record_method('Repetitions', count)

    def set_component(self, name: str):
        self.record_method('Component', name)

    def set_material(self, name: str):
        self.record_method('Material', name)

    def set_multiple_selection(self, flag: bool = True):
        self.record_method('MultipleSelection', flag)

    def set_destination(self, destination: str):
        self.record_method('Destination', destination)

    def set_auto_destination(self, flag: bool = True):
        #NOTE: officially undocumented
        self.record_method('AutoDestination', flag)

    def set_touch(self, flag: bool = True):
        self.record_method('Touch', flag)

    def add_name_to_active_touch_set(self, name: str):
        self.record_method('AddNameToActiveTouchSet', name)

    def add_name_to_passive_touch_set(self, name: str):
        self.record_method('AddNameToPassiveTouchSet', name)

    def set_touch_tolerance(self, tolerance: float):
        self.record_method('TouchTolerance', tolerance)

    def set_touch_max_num_iterations(self, count: int):
        self.record_method('TouchMaxIterations', count)

    def set_touch_heuristic(self, flag: bool = True):
        self.record_method('TouchHeuristic', flag)

    def set_touch_offset(self, offset: float):
        self.record_method('TouchOffset', offset)