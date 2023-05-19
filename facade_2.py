# Facade - Simplifies client interaction with subsystems
# https://github.com/gennad/Design-Patterns-in-Python/blob/master/facade.py

from abc import ABC, abstractmethod

# =============================================
# Complex parts
class CPU:
    def freeze(self):
        print("CPU Freeze!")

    def jump(self, position):
        print("Jump to memory position!")

    def execute(self):
        print("Executing CPU instructions!")

class Memory:
    def load(self, position, data): 
        print("Loading memory!")

class HardDrive:
    def read(self, lba, size):
        print("Reading harddrive!")

# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()

# Client
facade = Computer()
facade.start_computer()