# Classic decorater - dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects
# https://www.geeksforgeeks.org/decorator-method-python-design-patterns/

from abc import ABC, abstractmethod

# =============================================
# Component
class IWrittenText(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Component
class WrittenText(IWrittenText):
	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

# Concrete Decorators
class UnderlineWrapper(IWrittenText):
	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(IWrittenText):
	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(IWrittenText):
	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

# =============================================
# Client
before_gfg = WrittenText("GeeksforGeeks")
after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

print("before :", before_gfg.render())
print("after  :", after_gfg.render())
