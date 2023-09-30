from typing import Optional

class Schematic:
    def __init__(self, native_obj) -> None:
        self.native_obj = native_obj

    def execute_vba_code(self, vba_code: str) -> None:
        self.native_obj.execute_vba_code(vba_code)