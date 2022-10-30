import os


class Terminal:

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Домашняя библиотека")

    @staticmethod
    def write(string: str) -> None:
        print(string, end = '')

    @staticmethod
    def writeln(string: str) -> None:
        print(string)

    @staticmethod
    def writeln_ok(message: str) -> None:
        print("\033[92m" + message + "\033[0m")

    @staticmethod
    def writeln_warning(message: str) -> None:
        print("\033[93m" + message + "\033[0m")

    @staticmethod
    def read() -> str:
        user_input = None
        while True:
            try:
                user_input = str(input('>> '))
                return user_input
            except Exception as e:
                print(e)
