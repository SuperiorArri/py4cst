import win32com.client
import os.path
import shutil

class Interface:
    def clear_cache():
        cache_path = os.path.join(os.getenv('TMP'), 'gen_py')
        shutil.rmtree(cache_path, True)

    def __init__(self, version=None):
        self.stored_quiet_mode = False
        if(version is None):
            self.__open_app_latest_version()
        else:
            self.__open_app_specific_version(version)
        self.enable_quiet_mode()

    def __del__(self):
        self.disable_quiet_mode()

    def __open_app_latest_version(self):
        self.com_object = win32com.client.gencache\
            .EnsureDispatch('CSTStudio.Application')

    def __open_app_specific_version(self, version):
        self.com_object = win32com.client.gencache\
            .EnsureDispatch('CSTStudio.Application.'+str(version))

    def store_quiet_mode(self):
        self.stored_quiet_mode = self.is_in_quiet_mode()

    def restore_quiet_mode(self):
        self.set_quiet_mode(self.stored_quiet_mode)

    def store_and_disable_quiet_mode(self):
        self.store_quiet_mode()
        self.disable_quiet_mode()

    def store_and_enable_quiet_mode(self):
        self.store_quiet_mode()
        self.enable_quiet_mode()

    def open_3d_project(self, path):
        self.com_object.OpenFile(os.path.abspath(path))

    def open_ds_project(self, path):
        self.com_object.OpenFile(os.path.abspath(path))

    def create_new_mws_project(self):
        # Creates a new CST Microwave Studio project.
        self.com_object.NewMWS()

    def create_new_ems_project(self):
        # Creates a new CST EM Studio project.
        self.com_object.NewEMS()

    def create_new_ps_project(self):
        # Creates a new CST Particle Studio project.
        self.com_object.NewPS()

    def create_new_mps_project(self):
        # Creates a new CST Mphysics Studio project.
        self.com_object.NewMPS()

    def create_new_pcbs_project(self):
        # Creates a new CST PCB Studio project.
        self.com_object.NewPCBS()

    def create_new_ds_project(self):
        # Creates a new CST Design Studio project.
        self.com_object.NewDS()

    def enable_quiet_mode(self, flag: bool = True):
        self.com_object.SetQuietMode(flag)
        self.in_quiet_mode = flag

    def disable_quiet_mode(self):
        self.com_object.SetQuietMode(False)
        self.in_quiet_mode = False

    def set_quiet_mode(self, enabled=True):
        self.com_object.SetQuietMode(enabled)
        self.in_quiet_mode = enabled

    def is_in_quiet_mode(self):
        return self.in_quiet_mode

    def close(self):
        self.com_object.Quit()