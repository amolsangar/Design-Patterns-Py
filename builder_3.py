# Same as builder.py
from abc import ABC, abstractmethod

class Desktop:
    def __init__(self) -> None:
        self._monitor = None
        self._keyboard = None
        self._mouse = None
        self._speaker = None
        self._ram = None
        self._processor = None
        self._motherboard = None

    def set_monitor(self,value):
        self._monitor = value

    def set_keyboard(self,value):
        self._keyboard = value

    def set_mouse(self,value):
        self._mouse = value

    def set_speaker(self,value):
        self._speaker = value

    def set_ram(self,value):
        self._ram = value

    def set_processor(self,value):
        self._processor = value

    def set_motherboard(self,value):
        self._motherboard = value

    def __str__ (self):
        return 'Desktop(\nMonitor=' + str(self._monitor) + \
            ', \nKeyboard=' + str(self._keyboard) + \
            ', \nMouse=' + str(self._mouse) + \
            ', \nSpeaker=' + str(self._speaker) + \
            ', \nRam=' + str(self._ram) + \
            ', \nProcessor=' + str(self._processor) + \
            ', \nMotherboard=' + str(self._motherboard) + \
            '\n)'
    

class IBuilder(ABC):
    @abstractmethod
    def build_monitor(self):
        pass

    @abstractmethod
    def build_keyboard(self):
        pass

    @abstractmethod
    def build_mouse(self):
        pass
    
    @abstractmethod
    def build_speaker(self):
        pass
    
    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_processor(self):
        pass

    @abstractmethod
    def build_motherboard(self):
        pass

    @abstractmethod
    def get_desktop(self) -> Desktop:
        pass

class DellDesktopBuilder(IBuilder):
    def __init__(self) -> None:
        self._desktop = Desktop()

    def build_monitor(self):
        self._desktop.set_monitor('DELL Monitor')

    def build_keyboard(self):
        self._desktop.set_keyboard('DELL Keyboard')

    def build_mouse(self):
        self._desktop.set_mouse('DELL Mouse')
    
    def build_speaker(self):
        self._desktop.set_speaker('DELL Speaker')
    
    def build_ram(self):
        self._desktop.set_ram('DELL Ram')

    def build_processor(self):
        self._desktop.set_processor('DELL Processor')

    def build_motherboard(self):
        self._desktop.set_motherboard('DELL Motherboard')

    def get_desktop(self) -> Desktop:
        return self._desktop
    

class HPDesktopBuilder(IBuilder):
    def __init__(self) -> None:
        self._desktop = Desktop()

    def build_monitor(self):
        self._desktop.set_monitor('HP Monitor')

    def build_keyboard(self):
        self._desktop.set_keyboard('HP Keyboard')

    def build_mouse(self):
        self._desktop.set_mouse('HP Mouse')
    
    def build_speaker(self):
        self._desktop.set_speaker('HP Speaker')
    
    def build_ram(self):
        self._desktop.set_ram('HP Ram')

    def build_processor(self):
        self._desktop.set_processor('HP Processor')

    def build_motherboard(self):
        self._desktop.set_motherboard('HP Motherboard')

    def get_desktop(self) -> Desktop:
        return self._desktop
    

class Director:
    def __init__(self, builder) -> None:
        self._builder = builder
    
    def get_desktop(self):
        return self._builder.get_desktop()
    
    def build_desktop(self):
        self._builder.build_monitor()
        self._builder.build_keyboard()
        self._builder.build_mouse()
        self._builder.build_speaker()
        self._builder.build_ram()
        self._builder.build_processor()
        self._builder.build_motherboard()
        return self._builder.get_desktop()
        
        
# Client
dell_desktop_builder = DellDesktopBuilder()
director = Director(dell_desktop_builder)
dell_desktop = director.build_desktop()
print(dell_desktop)

hp_desktop_builder = HPDesktopBuilder()
director = Director(hp_desktop_builder)
hp_desktop = director.build_desktop()
print(hp_desktop)