from . import Project
from . import ComObjectWrapper

class STL(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.STL

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def reset(self):
        self.invoke_method('Reset')

    def set_file_name(self, file_name: str):
        self.invoke_method('FileName', file_name)

    def set_name(self, name: str):
        self.invoke_method('Name', name)

    def set_component(self, name: str):
        self.invoke_method('Component', name)

    def set_scale_to_unit(self, flag: bool = True):
        self.invoke_method('ScaleToUnit', flag)

    def set_import_file_units(self, units: str):
        self.invoke_method('ImportFileUnits', units)

    def set_export_from_active_coordinate_system(self, flag: bool = True):
        self.invoke_method('ExportFromActiveCoordinateSystem', flag)

    def set_import_to_active_coordinate_system(self, flag: bool = True):
        self.invoke_method('ImportToActiveCoordinateSystem', flag)

    def set_export_file_units(self, units: str):
        self.invoke_method('ExportFileUnits', units)

    def set_normal_tolerance(self, tolerance: float):
        self.invoke_method('NormalTolerance', tolerance)

    def set_surface_tolerance(self, tolerance: float):
        self.invoke_method('SurfaceTolerance', tolerance)

    def read(self):
        self.invoke_method('Read')

    def write(self):
        self.invoke_method('Write')