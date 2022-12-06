import hashlib
from datetime import datetime

from fpdf import FPDF

from Interface.ICommand import ICommand
from Model.Library import Library
from Model.Terminal import Terminal


class CommandList(ICommand):
    def __init__(self):
        self.name = 'list'
        self.arguments = ''
        self.description = 'Получить список всех книг'
        self.__terminal = Terminal()
        self.__library = Library()

    def parse(self, args: str) -> bool:
        # Запрос данных
        report = self.__library.get_report()

        # Настройка документа
        pdf = FPDF()
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 14)
        pdf.add_page()

        # Заполнение документа
        line_index = 1
        for string in report:
            pdf.cell(200, 10, txt=string, ln=line_index, align="L")
            line_index += 1

        # Сохранение документа
        datetime_str = datetime.now().strftime('%Y-%m-%d_%H:%M:%S').encode('utf-8')
        hash_str = hashlib.sha1(datetime_str).hexdigest()
        filename = hash_str + '.pdf'
        pdf.output('Reports/' + filename)

        self.__terminal.writeln_ok(f'Отчет сохранен в файле {filename}')
        return True
