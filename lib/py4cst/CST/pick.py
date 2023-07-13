from . import Project
from . import ComObjectWrapper

class Pick(ComObjectWrapper):
    PICK_TYPE_END_POINT = 'EndPoint'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Pick

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def add_edge(self, u1: int, v1: int, w1: int, u2: int, v2: int, w2: int):
        self.invoke_method('AddEdge', u1, v1, w1, u2, v2, w2)

    def delete_edge(self, index: int):
        self.invoke_method('DeleteEdge', index)

    def add_mean_edge(self, indices: list[int]):
        self.invoke_method('MeanEdge', ','.join(str(s) for s in indices))

    def move_edge(self, index: int, dx: float, dy: float, dz: float, keep_original: bool = False):
        self.invoke_method('MoveEdge', index, dx, dy, dz, keep_original)

    def move_edge_in_plane(self, index: int, offset: float, keep_original: bool = False):
        self.invoke_method('MoveEdgeInPlane', index, offset, keep_original)

    def pick_edge_from_picked_points(self, index1: int, index2: int):
        self.invoke_method('PickEdgeFromPickedPoints', index1, index2)

    def clear_all_picks(self):
        self.invoke_method('ClearAllPicks')

    def write_next_pick_to_database(self, id: int):
        self.invoke_method('NextPickToDataBase', id)

    def snap_last_point_to_drawplane(self):
        self.invoke_method('SnapLastPointToDrawplane')

    def pick_point_from_id_on(self, name: str, pick_type: str, id: int):
        self.invoke_method('PickPointFromIdOn', name, pick_type, id)

    def pick_point_from_point_on(self, name: str, pick_type: str, x: float, y: float, z: float):
        self.invoke_method('PickPointFromPointOn', name, pick_type, x, y, z)

    def pick_edge_from_id_on(self, name: str, edge_id: int, vertex_id: int):
        self.invoke_method('PickEdgeFromIdOn', name, edge_id, vertex_id)

    def pick_edge_from_point_on(self, name: str, x: float, y: float, z: float):
        self.invoke_method('PickEdgeFromPointOn', name, x, y, z)

    def pick_face_from_id_on(self, name: str, face_id: int):
        self.invoke_method('PickFaceFromIdOn', name, face_id)

    def pick_face_from_point_on(self, name: str, x: float, y: float, z: float):
        self.invoke_method('PickFaceFromPointOn', name, x, y, z)

    def pick_dangling_edge_chain_from_id(self, shape_name: str, id: int):
        self.invoke_method('PickDanglingEdgeChainFromId', shape_name, id)

    def pick_edge_from_id(self, shape_name: str, edge_id: int, vertex_id: int):
        self.invoke_method('PickEdgeFromId', shape_name, edge_id, vertex_id)

    def pick_edge_from_point(self, shape_name: str, x: float, y: float, z: float):
        self.invoke_method('PickEdgeFromPoint', shape_name, x, y, z)

    def pick_solid_edge_chain_from_id(self, shape_name: str, edge_id: int, face_id: int):
        self.invoke_method('PickSolidEdgeChainFromId', shape_name, edge_id, face_id)

    def pick_face_chain_from_id(self, shape_name: str, face_id: int):
        self.invoke_method('PickFaceChainFromId', shape_name, face_id)

    def pick_face_from_id(self, shape_name: str, id: int):
        self.invoke_method('PickFaceFromId', shape_name,id)

    def pick_face_from_point(self, shape_name: str, x: float, y: float, z: float):
        self.invoke_method('PickFaceFromPoint', shape_name, x, y, z)

    def change_face_id(self, shape_name: str, change_statement: str, version_number: str):
        self.invoke_method('ChangeFaceId', shape_name, change_statement, version_number)

    def change_edge_id(self, shape_name: str, change_statement: str, version_number: str):
        self.invoke_method('ChangeEdgeId', shape_name, change_statement, version_number)

    def change_vertex_id(self, shape_name: str, change_statement: str, version_number: str):
        self.invoke_method('ChangeVertexId', shape_name, change_statement, version_number)

    def delete_face(self, index: int):
        self.invoke_method('DeleteFace', index)

    def delete_point(self, index: int):
        self.invoke_method('DeletePoint', index)

    def add_mean_point(self, indices: list[int]):
        self.invoke_method('MeanPoint', ','.join(str(s) for s in indices))

    def add_mean_from_last_two_points(self):
        self.invoke_method('MeanLastTwoPoints')

    def move_point(self, index: int, dx: float, dy: float, dz: float, keep_original: bool = False):
        self.invoke_method('MovePoint', index, dx, dy, dz, keep_original)

    def pick_point_from_coordinates(self, x: float, y: float, z: float):
        self.invoke_method('PickPointFromCoordinates', x, y, z)

    #TODO: implement missing methods

    def get_edge_id_from_point(self, shape_name: str, x: float, y: float, z: float) -> int:
        return self.invoke_method('GetEdgeIdFromPoint', shape_name, x, y, z)

    def get_face_id_from_point(self, shape_name: str, x: float, y: float, z: float) -> int:
        return self.invoke_method('GetFaceIdFromPoint', shape_name, x, y, z)

    def get_number_of_picked_points(self) -> int:
        return self.invoke_method('GetNumberOfPickedPoints')

    def get_number_of_picked_edges(self) -> int:
        return self.invoke_method('GetNumberOfPickedEdges')

    def get_number_of_picked_facess(self) -> int:
        return self.invoke_method('GetNumberOfPickedFaces')

    #TODO: implement missing methods