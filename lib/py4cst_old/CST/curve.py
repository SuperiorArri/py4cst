from . import Project
from . import ComObjectWrapper
from . import w32com

class Curve(ComObjectWrapper):
    ITERATION_ALL = 'all'
    ITERATION_OPEN = 'open'
    ITERATION_CLOSED = 'closed'

    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Curve

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def create_curve(self, name: str):
        self.invoke_method('NewCurve', name)

    def delete_curve(self, name: str):
        self.invoke_method('DeleteCurve', name)

    def rename_curve(self, old_name: str, new_name: str):
        self.invoke_method('RenameCurve', old_name, new_name)

    def delete_curve_item(self, curve_name: str, item_name: str):
        self.invoke_method('DeleteCurveItem', curve_name, item_name)

    def rename_curve_item(self, curve_name: str, old_item_name: str, new_item_name: str):
        self.invoke_method('RenameCurveItem', curve_name, old_item_name, new_item_name)

    def delete_curve_item_segment(self, curve_name: str, edge_id: int):
        self.invoke_method('DeleteCurveItemSegment', curve_name, edge_id)

    def move_curve_item(self, item_name: str, old_curve_name: str, new_curve_name: str):
        self.invoke_method('MoveCurveItem', item_name, old_curve_name, new_curve_name)

    def start_curve_name_iteration(self, it_type: str):
        self.invoke_method('StartCurveNameIteration', it_type)

    def get_next_curve_name(self) -> str:
        return self.invoke_method('GetNextCurveName')

    def get_point_coordinates(self, item_name: str, pid: str):
        x = w32com.create_ref_double()
        y = w32com.create_ref_double()
        z = w32com.create_ref_double()
        success = self.invoke_method('GetPointCoordinates', item_name, pid, x, y, z)
        return (x.value, y.value, z.value) if success else None

    def get_number_of_points(self) -> int:
        return self.invoke_method('GetNumberOfPoints')

    def is_closed(self, item_name: str) -> bool:
        return self.invoke_method('IsClosed', item_name)
