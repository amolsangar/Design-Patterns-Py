# Observer Pattern - Used for alerting a group of users/subscribers who are monitoring a common subject/publisher
from abc import ABC, abstractmethod

# =============================================

class ISubscriber(ABC):
    @abstractmethod
    def notify(self):
        pass

class User(ISubscriber):
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def notify(self, event):
        print(self.user_id, "received event", event)
        
# =============================================

class IPublisher(ABC):
    @abstractmethod
    def register(self, listener):
        raise NotImplementedError("Must subclass me")

    @abstractmethod
    def unregister(self, listener):
        raise NotImplementedError("Must subclass me")

    @abstractmethod
    def notify_subscribers(self, event):
        raise NotImplementedError("Must subclass me")
    
class Group(IPublisher):
    def __init__(self):
        self.users = []

    def register(self, user):
        self.users.append(user)

    def unregister(self, user):
        self.users.remove(user)

    def notify_subscribers(self, event):
        for user in self.users:
            user.notify(event)

# =============================================
# Client

user1 = User(1)
user2 = User(2)
user3 = User(3)

group = Group()
group.register(user1)
group.register(user2)
group.register(user3)
group.notify_subscribers("new msg!")

group.unregister(user1)
group.notify_subscribers("new new msg!")