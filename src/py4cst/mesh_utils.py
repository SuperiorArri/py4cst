from .cst import IVBAProvider
from .cst.wrappers import Mesh, MeshSettings

def set_hexahedral_type(vbap: IVBAProvider):
    mesh = Mesh(vbap)
    mesh.set_mesh_type(Mesh.TYPE_PBA)
    mesh_settings = MeshSettings(vbap)
    mesh_settings.set_mesh_type(MeshSettings.MESH_TYPE_HEX)
