from . import ComObjectWrapper
import numpy as np

#TODO: activate project when used

class Result1D(ComObjectWrapper):
    def __init__(self, com_object) -> None:
        self.com_object = com_object

    def get_num_elements(self) -> int:
        return self.invoke_method('GetN')

    def get_x_at(self, index: int) -> float:
        return self.invoke_method('GetX', index)

    def get_y_at(self, index: int) -> float:
        return self.invoke_method('GetY', index)

    def get_array(self, component: str):
        return np.array(self.invoke_method('GetArray', component))

    def get_x_values(self):
        return self.get_array('x')

    def get_y_values(self):
        return self.get_array('y')