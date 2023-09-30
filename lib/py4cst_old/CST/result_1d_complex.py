from . import ComObjectWrapper
import numpy as np

class Result1DComplex(ComObjectWrapper):
    def __init__(self, com_object) -> None:
        self.com_object = com_object

    def get_num_elements(self) -> int:
        return self.invoke_method('GetN')

    def get_x_at(self, index: int) -> float:
        return self.invoke_method('GetX', index)

    def get_y_at(self, index: int) -> complex:
        y_re = self.invoke_method('GetYRe', index)
        y_im = self.invoke_method('GetYIm', index)
        return y_re + 1j*y_im

    def get_array(self, component: str):
        return np.array(self.invoke_method('GetArray', component))

    def get_x_values(self):
        return self.get_array('x')

    def get_y_values(self):
        re_vals = self.get_array('yre')
        im_vals = self.get_array('yim')
        return re_vals + 1j*im_vals