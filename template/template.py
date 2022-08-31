from abc import ABCMeta, abstractmethod
from sys import _clear_type_cache

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open():
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.ch, end='')

    def close(self):
        print('>>')

class StringDisplay(AbstractDisplay):
    def __init__(self, string) -> None:
        self.string :str = string
        self.width :int = len(string)

    def open(self):
        self.printLine()

    def print(self):
        print('|' + self.string + '|')

    def close(self):
        self.printLine()

    def printLine(self):
        print('+', end='')
        for i in range(self.width):
            print("-", end='')
        print("+", end='')

if __name__ == '__main__':
    d1: AbstractDisplay = CharDisplay('H')
    d2: AbstractDisplay = StringDisplay('Hello, world.')
    d3: AbstractDisplay = StringDisplay('こんにちは。')
    d1.display()
    print("")
    d2.display()
    print("")
    d3.display()
