from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandExit(ICommand):
    def __init__(self):
        self.name = 'exit'
        self.arguments = ''
        self.description = 'Закрыть программу'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str):
        quit()
