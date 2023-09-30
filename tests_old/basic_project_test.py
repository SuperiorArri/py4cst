import lib_test

from py4cst.CST import Interface, Project
# use the latest installed version of CST Studio Suite
interface = Interface()
# or use a specific version:
# interface = Interface(version=2023)

interface.create_new_mws_project()
project = Project(interface)
# project.close_without_saving()

lib_test.finalize()