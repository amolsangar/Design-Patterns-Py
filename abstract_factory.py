from abc import ABC, abstractmethod

# =============================================

class IFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

class WinFactory(IFactory):
    def create_button(self):
        return WinButton()
    
    def create_textbox(self):
        return WinTextbox()
    

class MacFactory(IFactory):
    def create_button(self):
        return MacButton()
    
    def create_textbox(self):
        return MacTextbox()
    
# =============================================

class IButton(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(IButton):
    def paint(self):
        return "Windows button pressed!"
    
class MacButton(IButton):
    def paint(self):
        return "Mac button pressed!"

# =============================================

class ITextbox():
    @abstractmethod
    def paint(self):
        pass

class WinTextbox(ITextbox):
    def paint(self):
        return "Windows textbox pressed!"
    
class MacTextbox(ITextbox):
    def paint(self):
        return "Mac textbox pressed!"
    
# =============================================

class GUIAbstractFactory():
    @staticmethod
    def create_factory(os_type):
        if os_type == "mac":
            return MacFactory()
        elif os_type == "windows":
            return WinFactory()
        else:
            return WinFactory()
        

# =============================================

# Client
factory = GUIAbstractFactory.create_factory('mac')
print(factory.create_button())
print(factory.create_textbox())
print()

factory = GUIAbstractFactory.create_factory('windows')
print(factory.create_button())
print(factory.create_textbox())
print()