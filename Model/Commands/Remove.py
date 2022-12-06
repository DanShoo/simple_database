from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandRemove(ICommand):
    def __init__(self):
        self.name = 'remove'
        self.arguments = '<номер>'
        self.description = 'Удалить книгу из библиотеки'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:

        try:
            index = int(args)
        except:
            return False

        if self.__library.remove_book(index):
            self.__terminal.writeln_ok('Книга удалена из библиотеки')
        else:
            self.__terminal.writeln_warning('Невозможно удалить книгу с заданным номером')

        return True
