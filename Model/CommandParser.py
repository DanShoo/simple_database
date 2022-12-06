from Model.Commands.Add import CommandAdd
from Model.Commands.Clear import CommandClear
from Model.Commands.Exit import CommandExit
from Model.Commands.Find import CommandFind
from Model.Commands.List import CommandList
from Model.Commands.Remove import CommandRemove

from Model.Terminal import Terminal


class CommandParser:

    def __init__(self):
        self._commands = [CommandAdd(),
                          CommandFind(),
                          CommandRemove(),
                          CommandList(),
                          CommandClear(),
                          CommandExit()]

    def print_commands_info(self) -> None:
        Terminal().writeln('Доступные действия:')
        for command in self._commands:
            Terminal().writeln('-> ' + command.description + ' - ' + command.name + ' ' + command.arguments)

    def try_command(self, input_command) -> None:
        success = False

        for command in self._commands:
            # Если названия команды нет в строке
            if command.name not in input_command:
                continue
            # Если название команды относится к аргументам
            if input_command.find(command.name) > 0:
                continue
            # Выделение аргументов команды
            args = input_command[len(command.name):]
            # Если аргументы не соответствуют требованиям
            if not command.parse(args):
                command.hint()
            success = True
            break

        if not success:
            Terminal().writeln_warning(
                "Введена некорректная команда. Введите \'help\' для получения списка доступных команд")
