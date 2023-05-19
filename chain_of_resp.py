# Chain of responsibility - Delegates commands to a chain of processing objects.
# https://www.youtube.com/watch?v=FafNcoBvVQo

from abc import ABC, abstractmethod

# =============================================
class Database:
    def __init__(self) -> None:
        self.users = {}
        self.users['user_username'] = "user_password"
        self.users['admin_username'] = "admin_password"

    def is_valid_user(self, username):
        if username in self.users:
            return True
        return False
    
    def is_valid_password(self, username, password):
        if self.users[username] == password:
            return True
        return False
    
# =============================================
class Handler(ABC):
    def __init__(self) -> None:
        self.next = None
    
    def set_next_handler(self, next):
        self.next = next
        return self.next
    
    @abstractmethod
    def handle(self,username,password):
        if self.next == None:
            return True
        return self.next.handle(username,password)

class ValidUserExistsHandler(Handler):
    def __init__(self, database) -> None:
        super().__init__()
        self.database = database

    def handle(self, username, password):
        if not self.database.is_valid_user(username):
            print("This username is not registered!")
            print("Please sign-up to our app!")
            return False
        print("User Exists!")
        return super().handle(username,password)
    
class ValidPasswordHandler(Handler):
    def __init__(self, database) -> None:
        super().__init__()
        self.database = database

    def handle(self, username, password):
        if not self.database.is_valid_password(username,password):
            print("Wrong password!")
            return False
        print("Password Matches!")
        return super().handle(username,password)
    
class RoleCheckHandler(Handler):
    def handle(self, username, password):
        if username == "admin_username":
            print("Loading Admin Page!")
        else:
            print("Loading Default Page!")
        return super().handle(username,password)

# =============================================
class AuthService:
    def __init__(self, handler) -> None:
        self.handler = handler

    def login(self, username, password):
        if self.handler.handle(username,password):
            print("Authentication Successful!")
            return True
        return False

# Client    
db = Database()
user_exists_handler = ValidUserExistsHandler(db)
password_handler = ValidPasswordHandler(db)
role_check_handler = RoleCheckHandler()

user_exists_handler.set_next_handler(password_handler).set_next_handler(role_check_handler)

auth_service = AuthService(user_exists_handler)

auth_service.login("admin_username","admin_password")
print()
auth_service.login("user_username","user_password")
print()
auth_service.login("wrong_username","user_password")
print()
auth_service.login("user_username","wrong_password")