# We can now summarize the components of the builder pattern in the context of the house building example as:
# Product (House): A class that represents the product to create.
# Builder (HouseBuilder): Is an interface to build the parts of a product.
# ConcreteBuilder(ConcreteHouseBuilder and PrefabricatedHouseBuilder): Are concrete classes that implement Builder to construct and assemble parts of the product and return the finished product.
# Director (ConstructionEngineer): A class that directs a builder to perform the steps in the order that is required to build the product.
# https://springframework.guru/gang-of-four-design-patterns/builder-pattern/

from abc import ABC, abstractmethod

# Product that is to be built
class House:
    def __init__(self) -> None:
        self._foundation = None
        self._structure = None
        self._roof = None
        self._furnished = None
        self._painted = None
    
    def set_foundation(self,value):
        self._foundation = value

    def set_structure(self,value):
        self._structure = value

    def set_roof(self,value):
        self._roof = value

    def set_furnished(self,value):
        self._furnished = value

    def set_painted(self,value):
        self._painted = value
    
    def __str__ (self):
        return 'House(\nFoundation=' + str(self._foundation) + ', \nStructure=' + str(self._structure) + ', \nRoof=' + str(self._roof) + ', \nFurnished=' + str(self._furnished) + ', \nPainted=' + str(self._painted) + '\n)'

# Interface
class IHouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass
    
    @abstractmethod
    def build_roof(self):
        pass
    
    @abstractmethod
    def paint_house(self):
        pass

    @abstractmethod
    def furnish_house(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass


class ConcreteHouseBuilder(IHouseBuilder):
    def __init__(self) -> None:
        self._house = House()

    def build_foundation(self):
        self._house.set_foundation("Concrete, brick, and stone")
        print("ConcreteHouseBuilder: Foundation complete!")

    def build_structure(self):
        self._house.set_structure("Concrete, mortar, brick, and reinforced steel")
        print("ConcreteHouseBuilder: Structure complete!")
    
    def build_roof(self):
        self._house.set_roof("Concrete and reinforced steel")
        print("ConcreteHouseBuilder: Roof complete!")
    
    def paint_house(self):
        self._house.set_painted(True)
        print("ConcreteHouseBuilder: Painting complete!")

    def furnish_house(self):
        self._house.set_furnished(True)
        print("ConcreteHouseBuilder: Furnishing complete!")

    def get_house(self) -> House:
        print("ConcreteHouseBuilder: Concrete house complete!")
        return self._house
    

class PrefabricatedHouseBuilder(IHouseBuilder):
    def __init__(self) -> None:
        self._house = House()

    def build_foundation(self):
        self._house.set_foundation("Wood, laminate, and PVC flooring")
        print("PrefabricatedHouseBuilder: Foundation complete!")

    def build_structure(self):
        self._house.set_structure("Structural steels and wooden wall panels")
        print("PrefabricatedHouseBuilder: Structure complete!")
    
    def build_roof(self):
        self._house.set_roof("Roofing sheets")
        print("PrefabricatedHouseBuilder: Roof complete!")
    
    def paint_house(self):
        self._house.set_painted(False)
        print("PrefabricatedHouseBuilder: Painting complete!")

    def furnish_house(self):
        self._house.set_furnished(True)
        print("PrefabricatedHouseBuilder: Furnishing complete!")

    def get_house(self) -> House:
        print("PrefabricatedHouseBuilder: Prefabricated house complete!")
        return self._house
    
# Director decides the series and order of execution steps
class Director:
    def __init__(self, builder) -> None:
        self._builder = builder
    
    def construct_house(self):
        self._builder.build_foundation()
        self._builder.build_structure()
        self._builder.build_roof()
        self._builder.paint_house()
        self._builder.furnish_house()
        return self._builder.get_house()

# Client
concrete_builder = ConcreteHouseBuilder()
director = Director(concrete_builder)
concrete_house = director.construct_house()
print(concrete_house)
print()

prefabricated_builder = PrefabricatedHouseBuilder()
director = Director(prefabricated_builder)
prefabricated_house = director.construct_house()
print(prefabricated_house)

    