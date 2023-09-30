from . import Project
from . import ComObjectWrapper

class ProjectUnits(ComObjectWrapper):
    def __init__(self, project: Project) -> None:
        self.project = project
        self.com_object = project.com_object.Units

    def invoke_method(self, name, *args, **kwargs):
        self.project.ensure_active()
        return super().invoke_method(name, *args, **kwargs)

    def set_geometry_unit(self, unit: str):
        self.invoke_method('Geometry', unit)

    def get_geometry_unit(self) -> str:
        return self.invoke_method('GetGeometryUnit')

    def get_geometry_unit_to_si_factor(self) -> float:
        return self.invoke_method('GetGeometryUnitToSI')

    def get_geometry_si_to_unit_factor(self) -> float:
        return self.invoke_method('GetGeometrySIToUnit')

    def set_time_unit(self, unit: str):
        self.invoke_method('Time', unit)

    def get_time_unit(self) -> str:
        return self.invoke_method('GetTimeUnit')

    def get_time_unit_to_si_factor(self) -> float:
        return self.invoke_method('GetTimeUnitToSI')

    def get_time_si_to_unit_factor(self) -> float:
        return self.invoke_method('GetTimeSIToUnit')

    def set_frequency_unit(self, unit: str):
        self.invoke_method('Frequency', unit)

    def get_frequency_unit(self) -> str:
        return self.invoke_method('GetFrequencyUnit')

    def get_frequency_unit_to_si_factor(self) -> float:
        return self.invoke_method('GetFrequencyUnitToSI')

    def get_frequency_si_to_unit_factor(self) -> float:
        return self.invoke_method('GetFrequencySIToUnit')

    def set_temperature_unit(self, unit: str):
        self.invoke_method('TemperatureUnit', unit)

    def get_temperature_unit(self) -> str:
        return self.invoke_method('GetTemperatureUnit')