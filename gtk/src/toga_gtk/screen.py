from toga.screen import Screen as ScreenInterface


class Screen:
    _instances = {}

    def __new__(cls, native):
        if native in cls._instances:
            return cls._instances[native]
        else:
            instance = super().__new__(cls)
            instance.interface = ScreenInterface(_impl=instance)
            instance.native = native
            cls._instances[native] = instance
            return instance

    def get_name(self):
        display = self.native.get_display()
        return display.get_name()

    def get_origin(self):
        geometry = self.native.get_geometry()
        return geometry.x, geometry.y
