from py4cst.CST import Interface, Brick

ifc = Interface()
proj = ifc.new_microwave_studio_project()

brick = Brick(proj)
brick.set_name('brick')
brick.set_xyz_range((0,0,0), (1,1,1))
brick.create()

proj.save(r'C:\temp\test.cst', False)