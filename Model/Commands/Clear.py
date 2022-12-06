from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandClear(ICommand):
    def __init__(self):
        self.name = 'clear'
        self.arguments = ''
        self.description = 'Очистить консоль'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:
        self.__terminal.clear()
        return True
