"""

Este módulo é responsável pelo processamento das categorias e palavras do liwc, para assim montar a estrutura
de dados de acesso.

"""
import os
# noinspection PyUnresolvedReferences
from category import Category
# noinspection PyUnresolvedReferences
from word import Word

__author__ = "Wesley Ferreira - @ovvesley "
__copyright__ = "Copyright 2020, Chat Analyse Project"
__email__ = "ovvesley@protonmail.com"


class Liwc:
    __absolute_path_file = ""
    __raw_file = None
    __encoding = "utf-8"

    __categories = set()
    __process_categories_complete = False
    __process_categories_count_mark = 0
    __process_categories_length_mark = 2
    __categories_mark = "%"

    __words = set()
    __process_words_complete = False



    def __init__(self, path_to_file):
        file = self.__open_file(self.__absolute_path_file + path_to_file)
        self.__handle_file(file)
        self.__handle_calculate_dict()

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
        processing_words_complete = self.__process_words_complete
        for line in file:
            if not processing_categories_complete:
                self.__processing_categories(line)
                processing_categories_complete = self.__process_categories_complete

            if not processing_words_complete and processing_categories_complete:
                self.__processing_words(line)


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
            category = Category(line_string)
            self.__add_categories(category)

    def __processing_words(self, line_string):
        word = Word(line_string)
        self.__add_word(word)
        pass

    def __add_word(self, word):
        self.__words.add(word)

    def __add_categories(self, category):
        self.__categories.add(category)

    def __processing_categories(self, line_string):
        length_mark = self.__process_categories_length_mark
        count_mark = self.__processing_categories_add_mark(line_string)
        if length_mark != count_mark:
            self.__handle_category(line_string)
        else:
            self.__set_process_categories_complete(True)
            return True

    def get_categories(self):
        return self.__categories

    def get_words(self):
        return self.__words

    def find_id_category(self, id):
        id = str(id)
        categories = self.get_categories()
        for category in categories:
            if category.get_id() == id:
                return category
        raise NameError(
            "Categoria com id {} não definida. Verifique o dicionário e veja se a categoria foi definida.".format(id))

    def __handle_calculate_dict(self):
        words = self.get_words()
        categories = self.get_categories()

        self.__link_reference_words_and_categories(words, categories)

    def __link_reference_words_and_categories(self, words, categories):
        for word in words:
            word_categories = self.get_categories_by_word(word)
            for category in word_categories:
                category.add_word(word)
            word.set_categories(word_categories)

    def get_categories_by_word(self, word):
        categories_ids = word.get_categories_ids()
        categories = []
        for category_id in categories_ids:
            new_category = self.find_id_category(category_id)
            categories.append(new_category)
        return categories



def test_class():
    print(os.path.dirname(__file__))
    liwc = Liwc("resources/dictionaries/liwc_2015_pt2_sem_pulo_linhas.dic")
    print(liwc.get_words())
    print(liwc.get_categories())


test_class()
