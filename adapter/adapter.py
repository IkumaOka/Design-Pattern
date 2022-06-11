from abc import ABCMeta, abstractmethod


class Banner:
    def __init__(self, string):
        self.string = string
    
    def show_with_paren(self):
        print(f'({self.string})')
    
    def show_with_aster(self):
        print(f'*{self.string}*')


class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak():
        pass

    @abstractmethod
    def print_strong():
        pass


class PrintBanner(Banner, Print):
    def __init__(self, string):
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


if __name__ == '__main__':
    p = PrintBanner('Hello')
    p.print_weak()
    p.print_strong()