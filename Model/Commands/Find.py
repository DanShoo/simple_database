from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandFind(ICommand):
    def __init__(self):
        self.name = 'find'
        self.arguments = '<номер/автор/год>, <значение>'
        self.description = 'Найти книгу по номеру, автору или году выпуска'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:

        if args.count(',') != 1:
            return False

        args_split = args.split(',')
        name = args_split[0].strip()
        value = args_split[1]

        if name == 'номер':
            try:
                index = int(value)
            except:
                return False

            success, book_list = self.__library.get_books_by_id(index)

            if success:
                for book in book_list:
                    self.__terminal.write(f'Книга ID:{book[0]} - ')
                    self.__terminal.writeln(book[1])
            else:
                self.__terminal.writeln_warning('Книга с заданным номером не существует')

            return True

        elif name == 'автор':

            success, book_list = self.__library.get_books_by_author(value)

            if success:
                for book in book_list:
                    self.__terminal.write(f'Книга ID:{book[0]} - ')
                    self.__terminal.writeln(book[1])
            else:
                self.__terminal.writeln_warning('Книг указанного автора нет в базе данных')

            return True

        elif name == 'год':
            try:
                year = int(value)
            except:
                return False

            success, book_list = self.__library.get_books_by_year(year)

            if success:
                for book in book_list:
                    self.__terminal.write(f'Книга ID:{book[0]} - ')
                    self.__terminal.writeln(book[1])
            else:
                self.__terminal.writeln_warning('Книг с указанным годом выпуска нет в базе данных')

            return True

        else:
            return False
