from abc import ABC, abstractmethod

# =============================================

class ILogisticsFactory(ABC):
    @abstractmethod
    def get_delivery_method(self):
        pass

    @abstractmethod
    def get_storage_method(self):
        pass

class GroundLogisticsFactory(ILogisticsFactory):
    def get_delivery_method(self,type):
        if type == 1:
            return Car()
        elif type == 2:
            return Truck()
        else:
            return None 
    
    def get_storage_method(self,type):
        if type == 1:
            return Box()
        elif type == 2:
            return BigBox()
        else:
            return None 
    
class SeaLogisticsFactory(ILogisticsFactory):
    def get_delivery_method(self,type):
        if type == 3:
            return Ship()
        elif type == 4:
            return Boat()
        else:
            return None
    
    def get_storage_method(self,type):
        if type == 3:
            return Container()
        elif type == 4:
            return BigBox()
        else:
            return None 
    
# =============================================

class IStorage(ABC):
    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def get_capacity(self):
        pass

    @abstractmethod
    def get_charges(self):
        pass
    
class Box(IStorage):
    def store(self):
        return "Box Storage!"

    def get_capacity(self):
        return 20

    def get_charges(self):
        return 20

class BigBox(IStorage):
    def store(self):
        return "Big Box Storage!"
    
    def get_capacity(self):
        return 50

    def get_charges(self):
        return 50

class Container(IStorage):
    def store(self):
        return "Container Storage!"
    
    def get_capacity(self):
        return 1000

    def get_charges(self):
        return 1000

# =============================================

class IDeliveryMethod(ABC):
    @abstractmethod
    def deliver(self):
        pass

    @abstractmethod
    def get_charges(self):
        pass

class Car(IDeliveryMethod):
    def deliver(self):
        return "Car Delivery!"

    def get_charges(self):
        return 200        

class Truck(IDeliveryMethod):
    def deliver(self):
        return "Truck Delivery!"

    def get_charges(self):
        return 500 

class Ship(IDeliveryMethod):
    def deliver(self):
        return "Ship Delivery!"

    def get_charges(self):
        return 300 

class Boat(IDeliveryMethod):
    def deliver(self):
        return "Boat Delivery!"

    def get_charges(self):
        return 100 

# =============================================

class LogisticsAbstractFactory():
    @staticmethod
    def get_delivery_factory(type):
        if type ==  1 or type == 2:
            return GroundLogisticsFactory()
        elif type == 3 or type == 4:
            return SeaLogisticsFactory()
        else:
            return None 

# =============================================

# Client
for type in range(1,5):
    factory = LogisticsAbstractFactory.get_delivery_factory(type)
    delivery = factory.get_delivery_method(type)
    print(delivery.deliver(), delivery.get_charges())
    storage = factory.get_storage_method(type)
    print(storage.store(), storage.get_charges())
    print()