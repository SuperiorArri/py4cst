from . import Interface

class Design:
    def __init__(self, interface: Interface):
        self.interface = interface
        self.com_object = interface.com_object.ActiveDS()