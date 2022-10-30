from model.book import Book


class Library:

    def __init__(self) -> None:
        self.__books = []
        self.__count = 0

    def add_book(self, book:Book) -> None:
        assert isinstance(book, Book), 'Объект должен быть книгой'
        self.__books.append(book)
        self.__count += 1

    def remove_book(self, index:int) -> bool:
        assert isinstance(index, int), 'Номер книги должен быть целым числом'
        if index == 0 or index > self.__count:
            return False
        else:
            self.__books.pop(index-1)
            self.__count -= 1
            return True

    def get_book(self, index:int) -> tuple[bool, Book]:
        assert isinstance(index, int), 'Номер книги должен быть целым числом'
        if index == 0 or index > self.__count:
            return False, None
        else:
            return True, self.__books[index-1]

    def get_report(self) -> str:
        if self.__count >= 1:
            index = 1
            report = f'В библиотеке находятся книги ({self.__count}):\n'
            for book in self.__books:
                report += f'{index}. ' + str(book)
                if index < self.__count:
                    report += '\n'
                index += 1
            return report
        else:
            return 'В библиотеке нет книг'


library = Library()
books = [Book('Мастер и Маргарита','М. А. Булгаков', 1966),
         Book('Преступление и наказание','Ф. М. Достоевский', 1866),
         Book('Война и мир','Л. Н. Толстой', 1865)]
for book in books: library.add_book(book)