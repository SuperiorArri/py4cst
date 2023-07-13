from win32com.client import VARIANT
import pythoncom

def create_ref_double() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, -1)

def create_ref_long() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I8, -1)

def create_ref_int() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1)

def create_ref_str() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BSTR, -1)

def create_ref_bool() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BOOL, -1)

def create_ref_variant() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, -1)

def create_ref_variant_array() -> VARIANT:
    return VARIANT(pythoncom.VT_BYREF | pythoncom.VT_ARRAY | pythoncom.VT_VARIANT, -1)

def create_str_array(arr: list[any]) -> VARIANT:
    arr = list(map(lambda x: str(x), arr))
    return VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_BSTR, arr)