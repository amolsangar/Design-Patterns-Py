# https://springframework.guru/gang-of-four-design-patterns/adapter-pattern/
# Target (TextFormattable): The existing interface that clients communicate with.
# Adaptee (CsvFormattable): The new incompatible interface that needs adapting.
# Adapter (CsvAdapterImpl): A class that adapts the Adaptee to the Target.
# Client: Communicates with the Target.

# Adapter Pattern: Make incompatible interfaces work together
# Converts multiple outputs into one single unified output which can be consumed by the client

from abc import ABC, abstractmethod

# =============================================

class TextFormattable(ABC):
    @abstractmethod
    def format_text(self):
        pass

class NewLineFormatter(TextFormattable):
    def format_text(self,text):
        return text.replace(".","\n")

# =============================================

class CSVFormattable(ABC):
    @abstractmethod
    def format_csv_text(self):
        pass

class CSVFormatter(CSVFormattable):
    def format_csv_text(self,text):
        return text.replace(".",",")

# =============================================

class CSVAdapter(TextFormattable):
    def __init__(self, csv_formatter) -> None:
        self.csv_formatter = csv_formatter

    def format_text(self,text):
        return self.csv_formatter.format_csv_text(text)


# Client
test_string = " Formatting line 1. Formatting line 2. Formatting line 3."
newline_formatter = NewLineFormatter()
result = newline_formatter.format_text(test_string)
print(result)

csv_formatter = CSVFormatter()
csv_adapter = CSVAdapter(csv_formatter)
result2 = csv_adapter.format_text(test_string)
print(result2)