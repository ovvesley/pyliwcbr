"""

Este módulo é responsável pela classe de Palavra(Word) do liwc, informando texto da palavra e as categorias que a palavra pertence.

"""
from pyliwcbr.src.liwc.utils import handle_string

__author__ = "Wesley Ferreira - @ovvesley "
__copyright__ = "Copyright 2020, Chat Analyse Project"
__email__ = "ovvesley@protonmail.com"


class Word:
    __raw_text = ""
    __categories_ids = set()
    __value = ""
    __categories = set()

    def __init__(self, line_string):
        self.__handle_line_string_word(line_string)

    def __set_raw_text(self, raw_text):
        self.__raw_text = raw_text

    def __set_categories_ids(self, categories):
        self.__categories_ids = categories

    def __set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def __handle_categories_id(self, categories_split):
        new_categories = []
        for category in categories_split:
            new_category = category.strip("\n")
            if new_category:
                new_categories.append(new_category)
        return new_categories

    def set_categories(self, categories):
        self.__categories = categories

    def get_categories(self):
        return self.__categories

    def __handle_line_string_word(self, line):
        line_split = line.split("\t")

        raw_text = line
        value_word = line_split.pop(0)
        categories = self.__handle_categories_id(line_split)

        self.__set_categories_ids(categories)
        self.__set_raw_text(raw_text)
        self.__set_value(value_word)

    def get_categories_ids(self):
        return self.__categories_ids

    def is_equals(self, raw_word):
        new_str_obj_word = handle_string.strip_accents(self.get_value()).lower()
        new_str_raw_word = handle_string.strip_accents(raw_word).lower()

        if new_str_obj_word == new_str_raw_word:
            return True
        else:
            return False


def __test_class():
    word1 = Word("empurrarei	20	92	100	101")
    word2 = Word("encardido	30	32	120	121")
    word3 = Word(":\	30	32	120	122")


__test_class()
