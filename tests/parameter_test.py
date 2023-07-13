import lib_test
from py4cst.CST import Interface, Project
import pythoncom
from win32com.client import VARIANT

cst = Interface()
cst.create_new_mws_project()
proj = Project(cst)

proj.store_parameters(['test', 'test2', 'test3'], [10, 20.1, True])
proj.save_as(lib_test.get_output_file_path('param_tst2.cst'))

lib_test.finalize()