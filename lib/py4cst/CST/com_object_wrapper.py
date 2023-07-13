from pywintypes import com_error

class ComObjectWrapper:
    def invoke_method(self, name, *args, **kwargs):
        try:
            self.com_object._FlagAsMethod(name)
            method = self.invoke_attribute(name)
            return method(*args, **kwargs)
        except com_error as e:
            # raise RuntimeError(e.args[2][2])
            raise RuntimeError(e)

    def invoke_attribute(self, name):
        return getattr(self.com_object, name)