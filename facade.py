# Facade - Simplifies client interaction with subsystems

from abc import ABC, abstractmethod

# =============================================
class Product:
    def __init__(self) -> None:
        self.product_id = None
        self.name = None

    # def __init__(self, productId, name) -> None:
    #     self.product_id = productId
    #     self.name = name

# =============================================
# Services or subsystems
class InventoryService:
    @staticmethod
    def is_available(product):
        ''' Check Warehouse database for product availability '''
        return True

class PaymentService:
    @staticmethod
    def make_payment():
        ''' Connect with payment gateway for payment '''
        return True

class ShippingService:
    @staticmethod
    def ship_product(product):
        ''' Connect with external shipment service to ship product '''
        pass

# =============================================
# Facade Interface
class IOrderServiceFacade(ABC):
    @abstractmethod
    def place_order(self,productId):
        pass

# Facade Concrete Class - consolidates all subsystem interactions
class OrderServiceFacadeImpl(IOrderServiceFacade):
    def place_order(self, pid):
        order_fulfilled = False
        product = Product()
        product.product_id = pid
        product.name = "Soap"

        if InventoryService.is_available(product):
            print("Product with ID: " + product.product_id + " is available.")
            payment_confirmed = PaymentService.make_payment()
            if payment_confirmed:
                print("Payment confirmed...")
                ShippingService.ship_product(product)
                print("Product shipped...")
                order_fulfilled = True

        return order_fulfilled

# =============================================
# Client Controller                
class OrderFulfillmentController:
    def __init__(self) -> None:
        self.facade = None
        self.order_fulfilled = False
    
    def order_product(self, pid):
        self.order_fulfilled = self.facade.place_order(pid)
        print("OrderFulfillmentController: Order fulfillment completed.")


controller = OrderFulfillmentController()
controller.facade = OrderServiceFacadeImpl()
controller.order_product('1')
print(controller.order_fulfilled)