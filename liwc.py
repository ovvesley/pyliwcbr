"""

Este módulo é responsável pelo processamento das categorias e palavras do liwc e montar a estrutura
de dados de acesso.

"""
import os


class Liwc():
    _absolute_path_file = ""
    _raw_file = None
    _encoding = "utf-8"

    _categories = {}
    _process_categories_complete = False
    _process_categories_count_mark = 0
    _process_categories_length_mark = 2
    categories_mark = "%"

    def __init__(self, path_to_file):
        file = self._open_file(self._absolute_path_file + path_to_file)
        self._handle_file(file)

    def _set_absolute_path(self, path):
        self._absolute_path_file = path

    def _set_raw_file(self, file):
        self._raw_file = file

    def _open_file(self, path):
        encoding = self._encoding

        file = open(path, "r", encoding=encoding)
        self._set_raw_file(file)

        return file

    def _handle_file(self, file):
        file = self._raw_file
        for line in file:
            self._processing_categories(line)
            # print(line)

    def _set_process_categories_count_mark(self, n):
        self._process_categories_count_mark = n

    def _set_process_categories_complete(self, value):
        self._process_categories_complete = value

    def _handle_line_string(self, line_string):
        return str(line_string.strip())

    def _processing_categories_add_mark(self, string):
        line_string = self._handle_line_string(string)
        categories_mark = self.categories_mark
        count_mark_categories = self._process_categories_count_mark
        new_count_mark = count_mark_categories

        if line_string.strip() == categories_mark:
            new_count_mark = new_count_mark + 1
            print(line_string, categories_mark)
            self._set_process_categories_count_mark(new_count_mark)
        return new_count_mark

    def _processing_categories(self, line_string):
        process_categories_complete = self._process_categories_complete
        if process_categories_complete:
            return
        else:
            length_mark = self._process_categories_length_mark
            count_mark = self._processing_categories_add_mark(line_string)
            if length_mark != count_mark:
                print(line_string)
            else:
                self._set_process_categories_complete(True)
                return True


def _test_class():
    print(os.path.dirname(__file__))
    liwc = Liwc("resources/dictionaries/liwc_2015_pt2_sem_pulo_linhas.dic")


_test_class()
