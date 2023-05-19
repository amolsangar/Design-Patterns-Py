# Classic Decorator
# https://springframework.guru/gang-of-four-design-patterns/decorator-pattern/
# Component (FlowerBouquet): Is an abstract base class that can be decorated with responsibilities dynamically.
# ConcreteComponent(RoseBouquet and OrchidBouquet): Are concrete classes that extends Component to represent objects to which additional responsibilities can be attached.
# Decorator (FlowerBouquetDecorator): Is an abstract class that extends Component and acts as the base class for concrete decorator classes.
# ConcreteDecorator (PapperWrapper, RibbonBow, and Glitter): Are concrete classes that extends Decorator to decorate Components with responsibilities.

from abc import ABC, abstractmethod

# =============================================
# Component
class IFlowerBouquet(ABC):
    def __init__(self) -> None:
        self.description = ""
    
    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Components
class RoseBouquet(IFlowerBouquet):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Rose bouquet"

    def cost(self) -> float:
        return 12.0
    
class OrchidBouquet(IFlowerBouquet):
    def __init__(self) -> None:
        super().__init__()
        self.description = "Orchid bouquet"

    def cost(self) -> float:
        return 29.0
    
# =============================================
# Decorator
class IFlowerBouquetDecorator(IFlowerBouquet):
    @abstractmethod
    def get_description(self):
        pass

# ConcreteDecorator
class PaperWrapper(IFlowerBouquetDecorator):
    def __init__(self, bouquet) -> None:
        self.bouquet = bouquet

    def get_description(self):
        return self.bouquet.get_description() + ", paper wrap"
    
    def cost(self) -> float:
        return self.bouquet.cost() + 3
    
class Glitter(IFlowerBouquetDecorator):
    def __init__(self, bouquet) -> None:
        self.bouquet = bouquet

    def get_description(self):
        return self.bouquet.get_description() + ", glitter"
    
    def cost(self) -> float:
        return self.bouquet.cost() + 4
    
class RibbonBow(IFlowerBouquetDecorator):
    def __init__(self, bouquet) -> None:
        self.bouquet = bouquet

    def get_description(self):
        return self.bouquet.get_description() + ", ribbon bow"
    
    def cost(self) -> float:
        return self.bouquet.cost() + 6.5
    
# =============================================
# Client
rose_bouquet = RoseBouquet()
print(rose_bouquet.get_description() + " $" + str(rose_bouquet.cost()))

# Rose bouquet with paper wrapper, ribbon bow, and glitter
decorated_rose_bouquet = RoseBouquet()
decorated_rose_bouquet = Glitter(RibbonBow(PaperWrapper(decorated_rose_bouquet)))
print(decorated_rose_bouquet.get_description() + " $" + str(decorated_rose_bouquet.cost()))

# Orchid bouquet with double paper wrapper and ribbon bow
decorated_orchid_bouquet = OrchidBouquet()
decorated_orchid_bouquet = RibbonBow(PaperWrapper(PaperWrapper(decorated_orchid_bouquet)))
print(decorated_orchid_bouquet.get_description() + " $" + str(decorated_orchid_bouquet.cost()))