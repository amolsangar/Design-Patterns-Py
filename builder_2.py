# https://www.youtube.com/watch?v=4ff_KZdvJn8&list=PLTCrU9sGybupCpY20eked6blbHI4zZ55k&index=14
# This flavor gives control to client to decide the inputs for complex object creation
# In this pattern flavor, order of execution steps doesn't matter

from abc import ABC, abstractmethod


class Builder():
    def __init__(self) -> None:
        self._protocol = None
        self._hostname = None
        self._port = None
        self._pathParam = None
        self._queryParam = None

    @property
    def protocol(self):
        return self._protocol

    @property
    def hostname(self):
        return self._hostname

    @property
    def port(self):
        return self._port

    @property
    def pathParam(self):
        return self._pathParam

    @property
    def queryParam(self):
        return self._queryParam

    def set_protocol(self, value):
        self._protocol = value
        return self

    def set_hostname(self, value):
        self._hostname = value
        return self

    def set_port(self, value):
        self._port = value
        return self

    def set_pathParam(self, value):
        self._pathParam = value
        return self
    
    def set_queryParam(self, value):
        self._queryParam = value
        return self

    def build(self):
        return URLBuilder(self)

class URLBuilder:
    def __init__(self, builder) -> None:
        self._protocol = builder.protocol
        self._hostname = builder.hostname
        self._port = builder.port
        self._pathParam = builder.pathParam
        self._queryParam = builder.queryParam
            
    @property
    def protocol(self):
        return self._protocol

    @property
    def hostname(self):
        return self._hostname

    @property
    def port(self):
        return self._port

    @property
    def pathParam(self):
        return self._pathParam

    @property
    def queryParam(self):
        return self._queryParam

    def __str__ (self):
        url = ""

        if self._protocol:
            url += self._protocol + "://"
        if self._hostname:
            url += self._hostname
        if self._port:
            url += ":" + self._port
        if self._pathParam:
            url += self._pathParam
        if self._queryParam:
            url += self._queryParam
            
        return url

# Director decides the series and order of execution steps
class Director():
    def __init__(self, builder) -> None:
        self._builder = builder

    def construct_url(self):
        self._builder.set_protocol('http').set_hostname('website').set_port('80')
        return self._builder.build()

# Client
builder = Builder()
# director = Director(builder)
# url = director.construct_url()
url = builder.set_protocol('http').set_hostname('website').set_port('80').build()
print(url)