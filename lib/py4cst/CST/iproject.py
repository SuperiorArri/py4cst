from . import Modeler, Schematic, InterfacePCBS, Parameters

class IProject:
    def get_modeler(self) -> Modeler:
        pass

    def get_schematic(self) -> Schematic:
        pass

    def get_interface_pcbs(self) -> InterfacePCBS:
        pass

    def get_parameters(self) -> Parameters:
        pass

    def get_messages(self) -> list:
        pass

    def get_last_message_text(self) -> str:
        pass