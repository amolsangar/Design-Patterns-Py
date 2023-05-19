# Classic Singleton in Python - 1
class Singleton1(object):
    def __new__(cls):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance

a = Singleton1()
a.toto = 12

b = Singleton1()
print(b.toto)
print(id(a) == id(b))  # The same !!

print()

# Classic Singleton in Python - 2
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.single_variable = "Singleton Variable"
print(new_singleton.single_variable)
