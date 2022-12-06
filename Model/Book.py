class Book:

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return '\'{}\' - {}, {} г.'.format(self.title, self.author, self.year)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        assert isinstance(title, str), 'Заголовок книги должен быть строкой'
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        assert isinstance(author, str), 'Автор книги должен быть строкой'
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        assert isinstance(year, int), 'Год выхода книги должен быть числом'
        self.__year = year
