"""

Este módulo é responsável pela classe de Categoria do liwc, informando id, tag e palavras que cada categoria é responsável.

"""
import re

__author__ = "Wesley Ferreira - @ovvesley "
__copyright__ = "Copyright 2020, Chat Analyse Project"
__email__ = "ovvesley@protonmail.com"


class Category:
    __tag = ""
    __id = 0
    __raw_tag = ""
    __child_category = None
    __parent_category = None
    __words = []
    __level = 0

    def __init__(self, line_string):
        self.__handle_line_string_category(line_string)
        pass

    def __handle_tag(self, string_name):
        tag = re.search('\(([^)]+)', string_name).group(1)
        tag = "".join(tag.split(" "))
        return tag

    def __set_level(self, level):
        self.__level = level

    def __set_id(self, id):
        self.__id = id

    def __set_raw_tag(self, raw_tag):
        self.__raw_tag = raw_tag

    def __set_tag(self, tag):
        self.__tag = tag

    def __handle_line_string_category(self, line):
        level = line.count("\t") - 1
        line_spl = [c for c in line.split("\t") if c]
        id = line_spl[0]
        tag = self.__handle_tag(line_spl[1])
        raw_tag = line_spl[1]

        self.__set_id(id)
        self.__set_level(level)
        self.__set_tag(tag)
        self.__set_raw_tag(raw_tag)

    def get_id(self):
        return self.__id

    def get_tag(self):
        return self.__tag

    def __str__(self):
        return self.__id + "-" + self.__tag

    def set_words(self, words):
        self.__words = words

    def get_words(self):
        return self.__words

def _test_class():
    Category("	2	pronoun (Pronouns)\n")
    Category("	2	pronoun (Pronouns)\n")
    Category("90	focuspast (Past Focus)\n")


# _test_class()
