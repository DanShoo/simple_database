from Model.CommandParser import CommandParser
from Model.Terminal import Terminal


terminal = Terminal()
terminal.clear()

commandParser = CommandParser()

while True:

    inputCommand = terminal.read()

    if inputCommand == 'help':
        commandParser.print_commands_info()
        continue

    commandParser.try_command(inputCommand)
