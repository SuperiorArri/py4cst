from . import IVBAProvider, VBAObjWrapper, VBATypeName
from typing import Optional

class Curve(VBAObjWrapper):
    ITERATION_ALL = 'all'
    ITERATION_OPEN = 'open'
    ITERATION_CLOSED = 'closed'

    def __init__(self, vbap: IVBAProvider) -> None:
        super().__init__(vbap, 'Curve')

    def create_curve(self, name: str):
        self.record_method('NewCurve', name)

    def delete_curve(self, name: str):
        self.record_method('DeleteCurve', name)

    def rename_curve(self, old_name: str, new_name: str):
        self.record_method('RenameCurve', old_name, new_name)

    def delete_curve_item(self, curve_name: str, item_name: str):
        self.record_method('DeleteCurveItem', curve_name, item_name)

    def rename_curve_item(self, curve_name: str, old_item_name: str, new_item_name: str):
        self.record_method('RenameCurveItem', curve_name, old_item_name, new_item_name)

    def delete_curve_item_segment(self, curve_name: str, edge_id: int):
        self.record_method('DeleteCurveItemSegment', curve_name, edge_id)

    def move_curve_item(self, item_name: str, old_curve_name: str, new_curve_name: str):
        self.record_method('MoveCurveItem', item_name, old_curve_name, new_curve_name)

    def start_curve_name_iteration(self, it_type: str):
        self.record_method('StartCurveNameIteration', it_type)

    def get_next_curve_name(self) -> str:
        return self.query_method_str('GetNextCurveName')

    # returns: (x, y, z) or None
    def get_point_coordinates(self, item_name: str, pid: str) \
            -> Optional[tuple[float, float, float]]:
        B, D = VBATypeName.Boolean, VBATypeName.Double
        res = self.query_method_t('GetPointCoordinates', B, item_name, pid, D, D, D)
        return None if not res[0] else res[1:]

    def get_number_of_points(self) -> int:
        return self.query_method_int('GetNumberOfPoints')

    def is_closed(self, item_name: str) -> bool:
        return self.query_method_bool('IsClosed', item_name)
