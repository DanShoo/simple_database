from model.terminal import Terminal
from model.command import AvailableCommands


Terminal.clear()

while True:

    input = Terminal.read()

    if input == 'help':
        Terminal.writeln('Доступные действия:')
        for command in AvailableCommands:
            Terminal.writeln('-> ' + command.description + ' - ' + command.name + ' ' + command.arguments)
        continue

    commandFound = False

    for command in AvailableCommands:

        # Если названия команды нет в строке
        if command.name not in input: continue

        # Если название команды относится к аргументам
        if input.find(command.name) > 0: continue

        args = input[len(command.name):]

        # Если аргументы не соответствуют требованиям
        if not command.parse(args): command.hint()

        commandFound = True
        break

    if not commandFound:
        Terminal.writeln_warning("Введена некорректная команда. Введите \'help\' для получения списка доступных команд")