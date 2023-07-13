from . import ResultTree

class ResultTreeItem:
    # Types:
    #   _TET indicates tetrahedral
    #   _SRF indicates triangular surface
    #   _TD indicates time monitors
    TYPE_EFIELD_3D = 'Efield3D' # 3D electric field plot
    TYPE_EFIELD_3D_TD = 'Efield3DTD'
    TYPE_EFIELD_3D_TET = 'Efield3D_tet'
    TYPE_EFIELD_3D_SRF = 'Efield3D_srf'
    TYPE_DFIELD_3D = 'Dfield3D' # 3D electric flux plot
    TYPE_DFIELD_3D_TET = 'Dfield3D_tet'
    TYPE_DFIELD_3D_SRF = 'Dfield3D_srf'
    TYPE_HFIELD_3D = 'Hfield3D' # 3D magnetic field plot
    TYPE_HFIELD_3D_TD = 'Hfield3DTD'
    TYPE_HFIELD_3D_TET = 'Hfield3D_tet'
    TYPE_HFIELD_3D_SRF = 'Hfield3D_srf'
    TYPE_BFIELD_3D = 'Bfield3D' # 3D magnetic flux plot
    TYPE_BFIELD_3D_TET = 'Bfield3D_tet'
    TYPE_BFIELD_3D_SRF = 'Bfield3D_srf'
    TYPE_SURFACE_CURRENT = 'SurfaceCurrent' # 3D surface current plot
    TYPE_SURFACE_CURRENT_TD = 'SurfaceCurrentTD'
    TYPE_SURFACE_CURRENT_TET = 'SurfaceCurrent_tet'
    TYPE_SURFACE_CURRENT_SRF = 'SurfaceCurrent_srf'
    TYPE_PFIELD_3D = 'Pfield3D' # 3D power flow plot
    TYPE_PFIELD_3D_TD = 'Pfield3DTD'
    TYPE_PFIELD_3D_TET = 'Pfield3D_tet'
    TYPE_EFIELD_2D = 'Efield2D' # 2D electric field plot
    TYPE_EFIELD_2D_TD = 'Efield2DTD'
    TYPE_HFIELD_2D = 'Hfield2D' # 2D magnetic field plot
    TYPE_HFIELD_2D_TD = 'Hfield2DTD'
    TYPE_PFIELD_2D = 'Pfield2D' # 2D power flow plot
    TYPE_PFIELD_2D_TD = 'Pfield2DTD'
    TYPE_CURRENT_3D = 'Current3D' # Current density
    TYPE_CURRENT_3D_TD = 'Current3DTD'
    TYPE_CURRENT_3D_TET = 'Current3D_tet'
    TYPE_POWER_LOSS_3D = 'PowerLoss3D' # Power loss density
    TYPE_POWER_LOSS_3D_TD = 'PowerLoss3DTD'
    TYPE_POWER_LOSS_3D_TET = 'PowerLoss3D_tet'
    TYPE_EENERGY_3D = 'EEnergy3D' # Electric energy
    TYPE_EENERGY_3D_TD = 'EEnergy3DTD'
    TYPE_EENERGY_3D_TET = 'EEnergy3D_tet'
    TYPE_HENERGY_3D = 'HEnergy3D' # Magnetic energy
    TYPE_HENERGY_3D_TD = 'HEnergy3DTD'
    TYPE_HENERGY_3D_TET = 'HEnergy3D_tet'
    TYPE_SAR_3D = 'SAR3D' # SAR field
    TYPE_FARFIELD = 'Farfield' # Farfield plot
    TYPE_COLOURMAP = 'Colourmap' # Colourmap plot
    TYPE_XY_SIGNAL = 'XYSignal' # General 1D result, needs additional definition by the Subtype method.
    TYPE_NOTEFILE = 'Notefile' # A generic ASCII text file
    TYPE_MACRO = 'Macro' # Visual Basic Macro

    SUBTYPE_COMPLEX = 'Complex'
    SUBTYPE_LINEAR = 'Linear'
    SUBTYPE_DB = 'dB'
    SUBTYPE_PHASE = 'Phase'
    SUBTYPE_TIME = 'Time'
    SUBTYPE_POSITION = 'Position'
    SUBTYPE_ENERGY = 'Energy'
    SUBTYPE_BALANCE = 'Balance'
    SUBTYPE_USER = 'User'

    DELETE_AT_NEVER = 'never'
    DELETE_AT_REBUILD = 'rebuild'
    DELETE_AT_SOLVER_START = 'solverstart'
    DELETE_AT_TRUE_MODEL_CHANGE = 'truemodelchange'

    def __init__(self, result_tree: ResultTree) -> None:
        self.result_tree = result_tree

    def reset(self):
        self.result_tree.invoke_method('Reset')

    def add(self):
        self.result_tree.invoke_method('Add')

    def delete(self):
        self.result_tree.invoke_method('Delete')

    def set_name(self, name: str):
        self.result_tree.invoke_method('Name', name)

    def set_type(self, item_type: str):
        self.result_tree.invoke_method('Type', item_type)

    def set_subtype(self, subtype: str):
        self.result_tree.invoke_method('Subtype', subtype)

    def set_title(self, title: str):
        self.result_tree.invoke_method('Title', title)

    def set_x_label(self, label: str):
        self.result_tree.invoke_method('Xlabel', label)

    def set_y_label(self, label: str):
        self.result_tree.invoke_method('Ylabel', label)

    def set_file(self, file: str):
        self.result_tree.invoke_method('File', file)

    def delete_at(self, when: str):
        self.result_tree.invoke_method('DeleteAt', when)

    def set_as_result(self, flag: bool = True):
        self.result_tree.invoke_method('IsResult', flag)

    def get_result_type(self, item_name: str) -> str:
        return self.result_tree.invoke_method('GetResultTypeFromItemName', item_name)

    def get_file(self, item_name: str) -> str:
        return self.result_tree.invoke_method('GetFileFromTreeItem', item_name)

    def get_result_ids(self, item_name: str):
        return self.result_tree.invoke_method('GetResultIDsFromTreeItem', item_name)

    def get_result(self, item_name: str, result_id: str):
        # TODO: check the result and return corresponding wrapper class
        return self.result_tree.invoke_method('GetResultFromTreeItem', item_name, result_id)

    def get_impedance_result(self, item_name: str, result_id: str):
        # TODO: check the result and return corresponding wrapper class
        return self.result_tree.invoke_method('GetImpedanceResultFromTreeItem', item_name, result_id)

    def has_impedance(self, item_name: str, result_id: str) -> bool:
        return self.result_tree.invoke_method('TreeItemHasImpedance', item_name, result_id)