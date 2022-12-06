from Model.Terminal import Terminal
from Model.Library import Library


class ICommand:
    name = None
    arguments = None
    description = None
    __terminal: Terminal
    __library: Library

    def hint(self) -> None:
        self.__terminal.writeln_warning('Используйте: ' + self.name + ' ' + self.arguments)

    def parse(self, args: str) -> bool:
        pass
