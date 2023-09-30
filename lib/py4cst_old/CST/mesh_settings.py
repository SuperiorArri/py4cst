from . import Project
from . import ComObjectWrapper

class MeshSettings(ComObjectWrapper):
    # This object is completely undocumented in CST Studio Suite Help, found in the history list

    MESH_TYPE_HEX = 'Hex'
    MESH_TYPE_HEX_TLM = 'HexTLM'
    MESH_TYPE_TET = 'Tet'
    MESH_TYPE_UNSTR = 'Unstr'
    MESH_TYPE_ALL = 'All'

    def __init__(self, project: Project):
        self.project = project
        self.com_object = project.com_object.MeshSettings

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_mesh_type(self, mesh_type: str):
        self.invoke_method('SetMeshType', mesh_type)

    def set_version(self, version: int):
        self.invoke_method('Set', 'Version', version)

    def set_number_of_steps_per_wave_near(self, number: float):
        self.invoke_method('Set', 'StepsPerWaveNear', number)

    def set_number_of_steps_per_wave_far(self, number: float):
        self.invoke_method('Set', 'StepsPerWaveFar', number)

    def set_wavelength_refinement_same_as_near(self, flag: bool = True):
        self.invoke_method('Set', 'WavelengthRefinementSameAsNear', 1 if flag else 0)

    def set_number_of_steps_per_box_near(self, number: float):
        self.invoke_method('Set', 'StepsPerBoxNear', number)

    def set_number_of_steps_per_box_far(self, number: float):
        self.invoke_method('Set', 'StepsPerBoxFar', number)

    def set_max_number_of_steps_near(self, number: float):
        self.invoke_method('Set', 'MaxStepNear', number)

    def set_max_number_of_steps_far(self, number: float):
        self.invoke_method('Set', 'MaxStepFar', number)

    def set_model_box_descr_near(self, descr: str):
        self.invoke_method('Set', 'ModelBoxDescrNear', descr)

    def set_model_box_descr_far(self, descr: str):
        self.invoke_method('Set', 'ModelBoxDescrFar', descr)

    def set_use_max_step_absolute(self, flag: bool = True):
        self.invoke_method('Set', 'UseMaxStepAbsolute', 1 if flag else 0)

    def set_geometry_refinement_same_as_near(self, flag: bool = True):
        self.invoke_method('Set', 'WavelengthRefinementSameAsNear', 1 if flag else 0)

    def set_use_ratio_limit_geometry(self, flag: bool = True):
        self.invoke_method('Set', 'UseRatioLimitGeometry', 1 if flag else 0)

    def set_ratio_limit_geometry(self, limit: float):
        self.invoke_method('Set', 'RatioLimitGeometry', limit)

    def set_min_step_geometry_x(self, step: float):
        self.invoke_method('Set', 'MinStepGeometryX', step)

    def set_min_step_geometry_y(self, step: float):
        self.invoke_method('Set', 'MinStepGeometryY', step)

    def set_min_step_geometry_z(self, step: float):
        self.invoke_method('Set', 'MinStepGeometryZ', step)

    def set_min_step_geometry_xyz(self, x: float, y: float, z: float):
        self.set_min_step_geometry_x(x)
        self.set_min_step_geometry_y(y)
        self.set_min_step_geometry_z(z)

    def set_use_same_min_step_geometry(self, flag: bool = True):
        self.invoke_method('Set', 'UseSameMinStepGeometryXYZ', 1 if flag else 0)

    def set_plane_merge_version(self, version: str):
        self.invoke_method('Set', 'PlaneMergeVersion', version)

    def set_face_refinement_on(self, flag: bool = True):
        self.invoke_method('Set', 'FaceRefinementOn', 1 if flag else 0)

    def set_face_refinement_policy(self, value: int):
        self.invoke_method('Set', 'FaceRefinementPolicy', value)

    def set_face_refinement_ratio(self, value: float):
        self.invoke_method('Set', 'FaceRefinementRatio', value)

    def set_face_refinement_step(self, value: float):
        self.invoke_method('Set', 'FaceRefinementStep', value)

    def set_face_refinement_number_of_steps(self, number: int):
        self.invoke_method('Set', 'FaceRefinementNSteps', number)

    def set_face_refinement_number_of_buffer_lines(self, number: int):
        self.invoke_method('Set', 'FaceRefinementBufferLines', number)

    def set_ellipse_refinement_on(self, flag: bool = True):
        self.invoke_method('Set', 'EllipseRefinementOn', 1 if flag else 0)

    def set_ellipse_refinement_policy(self, value: int):
        self.invoke_method('Set', 'EllipseRefinementPolicy', value)

    def set_ellipse_refinement_ratio(self, value: float):
        self.invoke_method('Set', 'EllipseRefinementRatio', value)

    def set_ellipse_refinement_step(self, value: float):
        self.invoke_method('Set', 'EllipseRefinementStep', value)

    def set_ellipse_refinement_number_of_steps(self, number: int):
        self.invoke_method('Set', 'EllipseRefinementNSteps', number)

    def set_edge_refinement_on(self, flag: bool = True):
        self.invoke_method('Set', 'EdgeRefinementOn', 1 if flag else 0)

    def set_edge_refinement_policy(self, value: int):
        self.invoke_method('Set', 'EdgeRefinementPolicy', value)

    def set_edge_refinement_ratio(self, value: float):
        self.invoke_method('Set', 'EdgeRefinementRatio', value)

    def set_edge_refinement_step(self, value: float):
        self.invoke_method('Set', 'EdgeRefinementStep', value)

    def set_edge_refinement_number_of_buffer_lines(self, number: int):
        self.invoke_method('Set', 'EdgeRefinementBufferLines', number)

    def set_refine_edge_material_global(self, flag: bool = True):
        self.invoke_method('Set', 'RefineEdgeMaterialGlobal', 1 if flag else 0)

    def set_refine_axial_edge_global(self, flag: bool = True):
        self.invoke_method('Set', 'RefineAxialEdgeGlobal', 1 if flag else 0)

    def set_number_of_buffer_lines_near(self, number: int):
        self.invoke_method('Set', 'BufferLinesNear', number)

    def set_use_dielectrics(self, flag: bool = True):
        self.invoke_method('Set', 'UseDielectrics', 1 if flag else 0)

    def set_equilibrate_on(self, flag: bool = True):
        self.invoke_method('Set', 'EquilibrateOn', 1 if flag else 0)

    def set_equilibrate(self, value: float):
        self.invoke_method('Set', 'Equilibrate', value)

    def set_ignore_thin_panel_material(self, flag: bool = True):
        self.invoke_method('Set', 'IgnoreThinPanelMaterial', 1 if flag else 0)

    def set_snap_to_axial_edges(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToAxialEdges', 1 if flag else 0)

    def set_snap_to_planes(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToPlanes', 1 if flag else 0)

    def set_snap_to_spheres(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToSpheres', 1 if flag else 0)

    def set_snap_to_ellipses(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToEllipses', 1 if flag else 0)

    def set_snap_to_cylinders(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToCylinders', 1 if flag else 0)

    def set_snap_to_cylinder_centers(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToCylinderCenters', 1 if flag else 0)

    def set_snap_to_ellipse_centers(self, flag: bool = True):
        self.invoke_method('Set', 'SnapToEllipseCenters', 1 if flag else 0)

    def set_phase_error_near(self, error: float):
        self.invoke_method('Set', 'PhaseErrorNear', error)

    def set_phase_error_far(self, error: float):
        self.invoke_method('Set', 'PhaseErrorFar', error)

    def set_cells_per_wavelength_policy(self, policy: str):
        self.invoke_method('Set', 'CellsPerWavelengthPolicy', policy)

    def set_min_step(self, value: float):
        self.invoke_method('Set', 'MinStep', value)

    def set_method(self, method: str):
        self.invoke_method('Set', 'Method', method)

    def set_curvature_order(self, order: int):
        self.invoke_method('Set', 'CurvatureOrder', order)

    def set_curvature_order_policy(self, policy: str):
        self.invoke_method('Set', 'CurvatureOrderPolicy', policy)

    def set_curv_refinement_control(self, value: str):
        self.invoke_method('Set', 'CurvRefinementControl', value)

    def set_normal_tolerance(self, value: float):
        self.invoke_method('Set', 'NormalTolerance', value)

    def set_srf_mesh_gradation(self, value: float):
        self.invoke_method('Set', 'SrfMeshGradation', value)

    def set_srf_mesh_optimization(self, flag: bool = True):
        self.invoke_method('Set', 'SrfMeshOptimization', 1 if flag else 0)

    def set_use_materials(self, flag: bool = True):
        self.invoke_method('Set', 'UseMaterials', 1 if flag else 0)

    def set_move_mesh(self, flag: bool = True):
        self.invoke_method('Set', 'MoveMesh', 1 if flag else 0)

    def set_automatic_edge_refinement(self, flag: bool = True):
        self.invoke_method('Set', 'AutomaticEdgeRefinement', 1 if flag else 0)

    def set_use_aniso_curve_refinement(self, flag: bool = True):
        self.invoke_method('Set', 'UseAnisoCurveRefinement', 1 if flag else 0)

    def set_use_same_srf_and_vol_mesh_gradation(self, flag: bool = True):
        self.invoke_method('Set', 'UseSameSrfAndVolMeshGradation', 1 if flag else 0)

    def set_vol_mesh_gradation(self, value: float):
        self.invoke_method('Set', 'VolMeshGradation', value)

    def set_vol_mesh_optimization(self, flag: bool = True):
        self.invoke_method('Set', 'VolMeshOptimization', 1 if flag else 0)

    def set_small_feature_size(self, value: float):
        self.invoke_method('Set', 'SmallFeatureSize', value)

    def set_coincidence_tolerance(self, value: float):
        self.invoke_method('Set', 'CoincidenceTolerance', value)

    def set_self_intersection_check(self, flag: bool = True):
        self.invoke_method('Set', 'SelfIntersectionCheck', 1 if flag else 0)

    def set_optimize_for_planar_structures(self, flag: bool = True):
        self.invoke_method('Set', 'OptimizeForPlanarStructures', 1 if flag else 0)