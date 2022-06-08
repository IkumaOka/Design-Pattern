from abc import ABCMeta, abstractmethod
from unicodedata import name


class Aggregate(metaclass=ABCMeta):
    def iterator():
        pass

class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class Book:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class BookShelf(Aggregate):
    def __init__(self):
        self.books = []
        self.last = 0

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books.append(book)
        self.last += 1

    def get_length(self):
        return self.last

    def iterator(self):
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def has_next(self):
        if self.index < self.book_shelf.get_length():
            return True
        else:
            return False

    def next(self):
        book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book


if __name__ == '__main__':
    book_shelf = BookShelf()
    book_shelf.append_book(Book('Around the World in 80 Days'))
    book_shelf.append_book(Book('Bible'))
    book_shelf.append_book(Book('Cinderella'))
    book_shelf.append_book(Book('Daddy-Long-Legs'))
    it = BookShelf.iterator(book_shelf)
    while it.has_next():
        book = it.next()
        print(book.get_name())
