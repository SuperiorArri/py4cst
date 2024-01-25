from . import IVBAProvider, VBAObjWrapper

class Mesh(VBAObjWrapper):
    TYPE_PBA = 'PBA'
    TYPE_STAIRCASE = 'Staircase'
    TYPE_TETRAHEDRAL = 'Tetrahedral'
    TYPE_SURFACE = 'Surface'
    TYPE_SURFACE_ML = 'SurfaceML'

    PBA_TYPE_PBA = 'PBA'
    PBA_TYPE_FAST_PBA = 'Fast PBA'

    PARALLEL_MESHER_TYPE_HEX = 'Hex'
    PARALLEL_MESHER_TYPE_TET = 'Tet'

    PARALLEL_MESHER_MODE_MAXIMUM = 'maximum'
    PARALLEL_MESHER_MODE_CUSTOM = 'user-defined'
    PARALLEL_MESHER_MODE_NONE = 'none'

    AUTOMESH_REFINE_DIELECTRICS_NONE = 'None'
    AUTOMESH_REFINE_DIELECTRICS_WAVE = 'Wave'
    AUTOMESH_REFINE_DIELECTRICS_STATIC = 'Static'

    SURFACE_MESH_METHOD_GENERAL = 'General'
    SURFACE_MESH_METHOD_FAST = 'Fast'

    SURFACE_TOLERANCE_TYPE_RELATIVE = 'Relative'
    SURFACE_TOLERANCE_TYPE_ABSOLUTE = 'Absolute'

    VOLUME_MESH_METHOD_DELAUNAY = 'Delaunay'
    VOLUME_MESH_METHOD_ADVANCING_FRONT = 'Advancing Front'

    PICK_TYPE_MIDPOINT = 'Midpoint'
    PICK_TYPE_FACE_CENTER = 'Facecenter'
    PICK_TYPE_CENTERPOINT = 'Centerpoint'
    PICK_TYPE_ENDPOINT = 'Endpoint'
    PICK_TYPE_CIRCLE_ENDPOINT = 'CircleEndpoint'
    PICK_TYPE_CIRCLEPOINT = 'Circlepoint'

    SPATIAL_VAR_NONE = 'none'
    SPATIAL_VAR_SPHERICAL = 'spherical'
    SPATIAL_VAR_CURVE = 'curve'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Mesh')

    def set_mesh_type(self, mesh_type: str):
        self.record_method('MeshType', mesh_type)

    def set_creator(self, creator: str):
        # undocumented, found in the history list
        self.record_method('SetCreator', creator)

    def set_connectivity_check(self, flag: bool = True):
        # undocumented, found in the history list
        self.record_method('ConnectivityCheck', flag)

    def set_cad_processing_method(self, method: str, undocumented_param: int = -1):
        # undocumented, found in the history list
        self.record_method('SetCADProcessingMethod', method, undocumented_param)

    def set_gpu_for_matrix_calculation_disabled(self, flag: bool = True):
        # undocumented, found in the history list
        self.record_method('SetGPUForMatrixCalculationDisabled', flag)

    def set_tst_version(self, version: str):
        self.record_method('TSTVersion', version)

    def set_pba_version(self, version: str):
        self.record_method('PBAVersion', version)

    def set_pba_type(self, pba_type: str):
        self.record_method('PBAType', pba_type)

    def set_automatic_pba_type(self, flag: bool = True):
        self.record_method('AutomaticPBAType', flag)

    def set_number_of_lines_per_wavelength(self, number: int):
        self.record_method('LinesPerWavelength', number)

    def set_min_number_of_steps(self, number: int):
        self.record_method('MinimumStepNumber', number)

    def set_ratio_limit(self, value: float):
        self.record_method('RatioLimit', value)

    def set_use_ratio_limit(self, flag: bool = True):
        self.record_method('UseRatioLimit', flag)

    def set_smallest_mesh_step(self, value: float):
        self.record_method('SmallestMeshStep', value)

    def set_steps_per_wavelength_tet(self, value: float):
        self.record_method('StepsPerWavelengthTet', value)

    def set_steps_per_wavelength_srf(self, value: float):
        self.record_method('StepsPerWavelengthSrf', value)

    def set_steps_per_wavelength_srf_ml(self, value: float):
        self.record_method('StepsPerWavelengthSrfML', value)

    def set_minimum_step_number_tet(self, value: float):
        self.record_method('MinimumStepNumberTet', value)

    def set_minimum_step_number_srf(self, value: float):
        self.record_method('MinimumStepNumberSrf', value)

    def set_minimum_step_number_srf_ml(self, value: float):
        self.record_method('MinimumStepNumberSrfML', value)

    def set_automesh(self, flag: bool = True):
        self.record_method('Automesh', flag)

    def set_material_refinement_tet(self, flag: bool = True):
        self.record_method('MaterialRefinementTet', flag)

    def set_equilibrate_mesh(self, flag: bool = True):
        self.record_method('EquilibrateMesh', flag)

    def set_equilibrate_mesh_ratio(self, value: float):
        self.record_method('EquilibrateMeshRatio', value)

    def set_use_cell_aspect_ratio(self, flag: bool = True):
        self.record_method('UseCellAspectRatio', flag)

    def set_cell_aspect_ratio(self, value: float):
        self.record_method('CellAspectRatio', value)

    def set_use_pec_edge_model(self, flag: bool = True):
        self.record_method('UsePecEdgeModel', flag)

    def set_point_acc_enhancement(self, value: float):
        self.record_method('PointAccEnhancement', value)

    def set_fast_pba_accuracy(self, value: float):
        self.record_method('FastPBAAccuracy', value)

    def set_fast_pba_gap_detection(self, flag: bool = True):
        self.record_method('FastPBAGapDetection', flag)

    def set_fast_pba_gap_tolerance(self, value: float):
        self.record_method('FPBAGapTolerance', value)

    def set_area_fill_limit(self, value: float):
        self.record_method('AreaFillLimit', value)

    def set_convert_geometry_data_after_meshing(self, flag: bool = True):
        self.record_method('ConvertGeometryDataAfterMeshing', flag)

    def set_consider_space_for_lower_mesh_limit(self, flag: bool = True):
        self.record_method('ConsiderSpaceForLowerMeshLimit', flag)

    def set_ratio_limit_governs_local_refinement(self, flag: bool = True):
        self.record_method('RatioLimitGovernsLocalRefinement', flag)

    def update(self):
        self.record_method('Update')

    def force_update(self):
        self.record_method('ForceUpdate')

    def calculate_matrices(self):
        self.record_method('CalculateMatrices')

    def set_view_mesh_mode(self, flag: bool = True):
        self.record_method('ViewMeshMode', flag)

    def set_small_feature_size(self, value: float):
        self.record_method('SmallFeatureSize', value)

    def set_parallel_mesher_mode(self, mesher_type: str, mesher_mode: str):
        self.record_method('SetParallelMesherMode', mesher_type, mesher_mode)

    def set_max_number_of_parallel_mesher_threads(self, mesher_type: str, number: int):
        self.record_method('SetMaxParallelMesherThreads', mesher_type, number)

    def set_automesh_straight_lines(self, flag: bool = True):
        self.record_method('AutomeshStraightLines', flag)

    def set_automesh_elliptical_lines(self, flag: bool = True):
        self.record_method('AutomeshEllipticalLines', flag)

    def enable_automesh_at_ellipse_bounds(self, factor: float):
        self.record_method('AutomeshAtEllipseBounds', True, factor)

    def disable_automesh_at_ellipse_bounds(self):
        self.record_method('AutomeshAtEllipseBounds', False, 0)

    def set_automesh_at_wire_end_points(self, flag: bool = True):
        self.record_method('AutomeshAtWireEndPoints', flag)

    def set_automesh_at_probe_points(self, flag: bool = True):
        self.record_method('AutomeshAtProbePoints', flag)

    def set_automesh_limit_shape_faces(self, flag: bool = True):
        self.record_method('AutoMeshLimitShapeFaces', flag)

    def set_automesh_number_of_shape_faces(self, number: int):
        self.record_method('AutoMeshNumberOfShapeFaces', number)

    def set_merge_thin_pec_layer_fixpoints(self, flag: bool = True):
        self.record_method('MergeThinPECLayerFixpoints', flag)

    def set_automesh_fixpoints_for_background(self, flag: bool = True):
        self.record_method('AutomeshFixpointsForBackground', flag)

    def enable_automesh_refine_at_pec_lines(self, factor: int):
        self.record_method('AutomeshRefineAtPecLines', True, factor)

    def disable_automesh_refine_at_pec_lines(self):
        self.record_method('AutomeshRefineAtPecLines', False, 0)

    def set_automesh_refine_pec_along_axes_only(self, flag: bool = True):
        self.record_method('AutomeshRefinePecAlongAxesOnly', flag)

    def set_automesh_refine_dielectrics_type(self, dielectrics_type: str):
        self.record_method('SetAutomeshRefineDielectricsType', dielectrics_type)

    def set_automesh_fixpoints_for_background(self, flag: bool = True):
        self.record_method('AutomeshFixpointsForBackground', flag)

    def set_surface_mesh_geometry_accuracy(self, value: float):
        self.record_method('SurfaceMeshGeometryAccuracy', value)

    def set_surface_mesh_method(self, method: str):
        self.record_method('SurfaceMeshMethod', method)

    def set_surface_tolerance(self, value: float):
        self.record_method('SurfaceTolerance', value)

    def set_surface_tolerance_type(self, surface_tolerance_type: str):
        self.record_method('SurfaceToleranceType', surface_tolerance_type)

    def set_normal_tolerance(self, value: float):
        self.record_method('NormalTolerance', value)

    def set_anisotropic_curvature_refinement_fsm(self, flag: bool = True):
        self.record_method('AnisotropicCurvatureRefinementFSM', flag)

    def set_surface_mesh_enrichment(self, level: int):
        self.record_method('SurfaceMeshEnrichment', level)

    def set_surface_optimization(self, flag: bool = True):
        self.record_method('SurfaceOptimization', flag)

    def set_surface_smoothing(self, flag: bool = True):
        self.record_method('SurfaceSmoothing', flag)

    def set_curvature_refinement_factor(self, value: float):
        self.record_method('CurvatureRefinementFactor', value)

    def set_min_curvature_refinement(self, value: float):
        self.record_method('MinimumCurvatureRefinement', value)

    def set_anisotropic_curvature_refinement(self, flag: bool = True):
        self.record_method('AnisotropicCurvatureRefinement', flag)

    def set_volume_optimization(self, flag: bool = True):
        self.record_method('VolumeOptimization', flag)

    def set_volume_smoothing(self, flag: bool = True):
        self.record_method('VolumeSmoothing', flag)

    def set_density_transitions(self, value: float):
        self.record_method('DensityTransitions', value)

    def set_volume_mesh_method(self, method: str):
        self.record_method('VolumeMeshMethod', method)

    def set_delaunay_optimization_level(self, value: int):
        self.record_method('DelaunayOptimizationLevel', value)

    def set_delaunay_propagation_factor(self, value: float):
        self.record_method('DelaunayPropagationFactor', value)

    def snap_to_surface_mesh(self, file_path_in: str, file_path_out: str):
        self.record_method('SnapToSurfaceMesh', file_path_in, file_path_out)

    def set_self_intersecting_check(self, flag: bool = True):
        self.record_method('SelfIntersectingCheck', flag)

    def find_fixpoint_from_position(self, x: float, y: float, z: float) -> int:
        return self.query_method_int('FindFixpointFromPosition', x, y, z)

    def add_fixpoint(self, x: float, y: float, z: float):
        self.record_method('AddFixpoint', x, y, z)

    def add_fixpoint_relative(self, ref_fixpoint_id: int, x: float, y: float, z: float):
        self.record_method('RelativeAddFixpoint', ref_fixpoint_id, x, y, z)

    def delete_fixpoint(self, fixpoint_id: int):
        self.record_method('DeleteFixpoint', fixpoint_id)

    def add_intermediate_fixpoints(self, id1: int, id2: int, number_of_points: int):
        self.record_method('AddIntermediateFixpoint', id1, id2, number_of_points)

    def add_automesh_fixpoint(
            self, use_x: bool, use_y: bool, use_z: bool, x: float, y: float, z: float):
        self.record_method('AddAutomeshFixpoint', use_x, use_y, use_z, x, y, z)

    def delete_automesh_fixpoint(self, x: float, y: float, z: float):
        self.record_method('DeleteAutomeshFixpoint', x, y, z)

    def modify_automesh_fixpoint(self, use_x: bool, use_y: bool, use_z: bool, fixpoint_id: int):
        self.record_method('ModifyAutomeshFixpointFromId', use_x, use_y, use_z, fixpoint_id)

    def add_automesh_fixpoints_from_pick(
            self, use_x: bool, use_y: bool, use_z: bool, pick_type: str, solid_name: str,
            pick_id: int, face_id: int, number: int):
        self.record_method(
            'AddAutomeshFixpointFromId', use_x, use_y, use_z, pick_type, solid_name,
            pick_id, face_id, number)

    def delete_automesh_fixpoint(self, fixpoint_id: int):
        self.record_method('DeleteAutomeshFixpointFromId', fixpoint_id)

    def clear_spatial_variation(self):
        self.record_method('ClearSpatialVariation')

    def clear_spatial_variation_for_shape(self, solid_name: str):
        self.record_method('ClearSpatialVariationForShape', solid_name)

    def set_spatial_variation_type_for_shape(self, solid_name: str, var_type: str):
        self.record_method('SetSpatialVariationTypeForShape', solid_name, var_type)