from abc import abstractmethod

from model.terminal import Terminal
from model.book import Book
from model.library import library


class ICommand:
    name = None
    arguments = None
    description = None

    @classmethod
    def hint(cls) -> None:
        Terminal.writeln_warning('Используйте: ' + cls.name + ' ' + cls.arguments)

    @abstractmethod
    def parse(args: str) -> bool:
        pass


class CommandAdd(ICommand):
    name = 'add'
    arguments = '\'название\' \'автор\' \'год выхода\''
    description = 'Добавить книгу в библиотеку'

    def parse(args: str) -> bool:
        if args.count('\'') != 6: return False
        # Убираем символы до заголовка
        args = args[args.find('\'')+1:]
        # Выделяем заголовок
        title = args[:args.find('\'')]
        # Убираем кавычку после заголовка
        args = args[args.find('\'')+1:]
        # Убираем символы до автора
        args = args[args.find('\'')+1:]
        # Выделяем автора
        author = args[:args.find('\'')]
        # Убираем кавычку после автора
        args = args[args.find('\'')+1:]
        # Убираем символы до года
        args = args[args.find('\'')+1:]
        # Выделяем год
        try:
            year = int(args[:args.find('\'')])
        except:
            return False
        book = Book(title, author, year)
        library.add_book(book)
        Terminal.writeln_ok('Книга добавлена в библиотеку')
        return True


class CommandInfo(ICommand):
    name = 'info'
    arguments = 'номер'
    description = 'Получить информацию о книге'

    def parse(args: str) -> bool:

        # Конвертируем аргумент в число
        try:
            index = int(args)
        except:
            return False

        success, book = library.get_book(index)

        if success:
            Terminal.write(f'Книга №{index}: ')
            Terminal.writeln(book)
        else:
            Terminal.writeln_warning('Книга с заданным номером не существует')

        return True


class CommandRemove(ICommand):
    name = 'remove'
    arguments = 'номер'
    description = 'Удалить книгу из библиотеки'

    def parse(args: str) -> bool:

        # Конвертируем аргумент в число
        try:
            index = int(args)
        except:
            return False

        if library.remove_book(index):
            Terminal.writeln_ok('Книга удалена из библиотеки')
        else:
            Terminal.writeln_warning('Невозможно удалить книгу с заданным номером')

        return True


class CommandList(ICommand):
    name = 'list'
    arguments = ''
    description = 'Вывести список всех книг'

    def parse(args: str) -> bool:
        booksList = library.get_report()
        Terminal.writeln(booksList)
        return True


class CommandClear(ICommand):
    name = 'clear'
    arguments = ''
    description = 'Очистить консоль'

    def parse(args: str) -> bool:
        Terminal.clear()
        return True


class CommandExit(ICommand):
    name = 'exit'
    arguments = ''
    description = 'Закрыть программу'

    def parse(args: str):
        quit()


AvailableCommands = [CommandAdd, CommandInfo, CommandRemove, CommandList, CommandClear, CommandExit]