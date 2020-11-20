"""

Este módulo é responsável pelo processamento das categorias e palavras do liwc, para assim montar a estrutura
de dados de acesso.

"""
import os
# noinspection PyUnresolvedReferences
from category import Category


class Liwc:
    __absolute_path_file = ""
    __raw_file = None
    __encoding = "utf-8"

    __categories = {}
    __process_categories_complete = False
    __process_categories_count_mark = 0
    __process_categories_length_mark = 2
    __categories_mark = "%"

    def __init__(self, path_to_file):
        file = self.__open_file(self.__absolute_path_file + path_to_file)
        self.__handle_file(file)

    def __set_absolute_path(self, path):
        self.__absolute_path_file = path

    def __set_raw_file(self, file):
        self.__raw_file = file

    def __open_file(self, path):
        encoding = self.__encoding

        file = open(path, "r", encoding=encoding)
        self.__set_raw_file(file)

        return file

    def __handle_file(self, file):
        file = self.__raw_file
        processing_categories_complete = self.__process_categories_complete
        for line in file:
            if not processing_categories_complete:
                self.__processing_categories(line)
                processing_categories_complete = self.__process_categories_complete
            else:

                pass

    def __set_process_categories_count_mark(self, n):
        self.__process_categories_count_mark = n

    def __set_process_categories_complete(self, value):
        self.__process_categories_complete = value

    def __handle_line_string(self, line_string):
        return str(line_string.strip())

    def __processing_categories_add_mark(self, string):
        line_string = self.__handle_line_string(string)
        categories_mark = self.__categories_mark
        count_mark_categories = self.__process_categories_count_mark
        new_count_mark = count_mark_categories

        if line_string.strip() == categories_mark:
            new_count_mark = new_count_mark + 1
            self.__set_process_categories_count_mark(new_count_mark)
        return new_count_mark

    def __handle_category(self, line_string):
        categories_mark = self.__categories_mark
        if categories_mark == line_string.strip():
            pass
        else:
            # Category(line_string)

            pass

    def __add_categories(self):
        pass
    def __processing_categories(self, line_string):
        length_mark = self.__process_categories_length_mark
        count_mark = self.__processing_categories_add_mark(line_string)
        if length_mark != count_mark:
            self.__handle_category(line_string)
        else:
            self.__set_process_categories_complete(True)
            return True


def test_class():
    print(os.path.dirname(__file__))
    liwc = Liwc("resources/dictionaries/liwc_2015_pt2_sem_pulo_linhas.dic")


test_class()
