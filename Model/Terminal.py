import os


class Terminal:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Terminal, cls).__new__(cls)
        return cls.instance

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Библиотека")

    def write(self, string: str) -> None:
        print(string, end='')

    def writeln(self, string: str) -> None:
        print(string)

    def writeln_ok(self, message: str) -> None:
        print("\033[92m" + message + "\033[0m")

    def writeln_warning(self, message: str) -> None:
        print("\033[93m" + message + "\033[0m")

    def read(self) -> str:
        user_input = None
        while True:
            try:
                user_input = str(input('>> '))
                return user_input
            except Exception as e:
                print(e)
