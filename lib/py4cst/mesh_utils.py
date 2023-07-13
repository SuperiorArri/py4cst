from py4cst.CST import Project, Mesh, MeshSettings

def set_hexahedral_type(project: Project):
    mesh = Mesh(project)
    mesh.set_mesh_type(Mesh.TYPE_PBA)
    mesh_settings = MeshSettings(project)
    mesh_settings.set_mesh_type(MeshSettings.MESH_TYPE_HEX)
