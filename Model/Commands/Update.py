from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandUpdate(ICommand):
    def __init__(self):
        self.name = 'update'
        self.arguments = '<номер>, <название/автор/год>, <значение>'
        self.description = 'Изменить книгу с указанным номером'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:

        if args.count(',') != 2:
            return False

        args_split = args.split(',')
        try:
            index = int(args_split[0])
        except:
            return False
        name = args_split[1].strip()
        value = args_split[2]

        success, book = self.__library.get_books_by_id(index)

        if not success:
            self.__terminal.writeln_warning('Книга с заданным номером не существует')
            return True

        book = book[0][1]

        if name == 'название':
            book.title = value
        elif name == 'автор':
            book.author = value
        elif name == 'год':
            try:
                book.year = int(value)
            except:
                self.__terminal.writeln_warning('Неправильно введен год')
                return True
        else:
            return False

        success = self.__library.update_book(index, book)

        if success:
            self.__terminal.writeln_ok('Книга успешно обновлена')
            return True
        else:
            self.__terminal.writeln_warning('Книга с заданным номером не существует')
            return True
