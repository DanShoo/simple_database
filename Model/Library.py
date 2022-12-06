from peewee import MySQLDatabase

from Model.Book import Book
from Model.LibraryModel import LibraryModel


def get_books_with_id(query) -> list:
    book_list = []
    for book in query:
        book_list.append(
            [
                book.id,
                Book(
                    author=book.author,
                    title=book.title,
                    year=book.year
                )
            ]
        )
    return book_list


class Library:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Library, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.__dataBase = MySQLDatabase('library', user='admin', password='WyR-nH7-A54-cp4', host='localhost',
                                        port=3306)
        self.__dataBase.connect()
        self.__library_model = LibraryModel()
        self.__library_model._meta.database = self.__dataBase

    def add_book(self, book: Book) -> None:
        assert isinstance(book, Book), 'Объект должен быть книгой'
        self.__library_model.create(
            title=book.title,
            author=book.author,
            year=book.year
        )

    def remove_book(self, index: int) -> bool:
        assert isinstance(index, int), 'Номер книги должен быть целым числом'
        query = self.__library_model.select().where(LibraryModel.id == index)
        if not query.exists():
            return False
        else:
            self.__library_model.get_by_id(index).delete_instance()
            return True

    def get_books_by_id(self, index: int) -> tuple[bool, any]:
        assert isinstance(index, int), 'Номер книги должен быть целым числом'
        query = self.__library_model.select().where(LibraryModel.id == index)
        if not query.exists():
            return False, None
        else:
            return True, get_books_with_id(query)

    def get_books_by_author(self, author: str) -> tuple[bool, any]:
        assert isinstance(author, str), 'Номер книги должен быть целым числом'
        query = self.__library_model.select().where(LibraryModel.author.contains(author))
        if not query.exists():
            return False, None
        else:
            return True, get_books_with_id(query)

    def get_books_by_year(self, year: int) -> tuple[bool, any]:
        assert isinstance(year, int), 'Номер книги должен быть целым числом'
        query = self.__library_model.select().where(LibraryModel.year == year)
        if not query.exists():
            return False, None
        else:
            return True, get_books_with_id(query)

    def get_report(self) -> list[str]:
        query = self.__library_model.select()
        book_list = get_books_with_id(query)
        if not book_list:
            return ['В библиотеке нет книг']
        else:
            report = [f'В библиотеке находятся книги ({self.__count_books()}):']
            for book in book_list:
                report.append(f'ID:{book[0]} - ' + str(book[1]))
            return report

    def __count_books(self) -> int:
        return self.__library_model.select().count()
