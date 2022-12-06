from Interface.ICommand import ICommand
from Model.Book import Book
from Model.Library import Library
from Model.Terminal import Terminal


class CommandAdd(ICommand):
    def __init__(self):
        self.name = 'add'
        self.arguments = '<название>, <автор>, <год выхода>'
        self.description = 'Добавить книгу в библиотеку'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:

        if args.count(',') != 2:
            return False

        args_split = args.split(',')
        title = args_split[0].strip()
        author = args_split[1].strip()
        year = args_split[2]

        try:
            year = int(year)
        except:
            return False

        book = Book(title, author, year)
        self.__library.add_book(book)

        self.__terminal.writeln_ok('Книга добавлена в библиотеку')
        return True
