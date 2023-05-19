from abc import ABC, abstractmethod

class ICache(ABC):
    connection_url = "http://localhost:7777"
    def connect(self):
        return "Connecting to Cache Server X.X.X.X"

    @abstractmethod
    def get_key(self,key):
        pass

    @abstractmethod
    def set_key(self,key):
        pass

    @abstractmethod
    def remove_key(self,key):
        pass

class Memcached(ICache):
    def get_key(self,key):
        return f"Memcached Get Key!"

    def set_key(self,key):
        return f"Memcached Set Key!"

    def remove_key(self,key):
        return f"Memcached Remove Key!"

class Redis(ICache):
    def get_key(self,key):
        return f"Redis Get Key!"

    def set_key(self,key):
        return f"Redis Set Key!"

    def remove_key(self,key):
        return f"Redis Remove Key!"

# If statement can be replaced with a dictionary/map
class CacheFactory():
    @staticmethod
    def get_cache(cache):
        if cache == "Memcached":
            return Memcached()
        elif cache == "Redis":
            return Redis()
        else:
            return None

# Client Code
# The list can be fetched by an API call
# The client code is not changed
cache_name = ["Memcached","Redis"]
for name in cache_name:
    cache = CacheFactory().get_cache(name)
    print(cache.connect())
    print(cache.set_key("One"))
    print(cache.get_key("One"))
    print(cache.remove_key("One"))
    print()
