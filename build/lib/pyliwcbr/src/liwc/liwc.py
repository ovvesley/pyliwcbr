"""

Este módulo é responsável pelo processamento das categorias e palavras do liwc, para assim montar a estrutura
de dados de acesso.

"""
from pyliwcbr.src.liwc.category import Category
from pyliwcbr.src.liwc.word import Word
from pyliwcbr.src.liwc.sentence import Sentence
from pyliwcbr.src.liwc.utils import handle_string
from collections import defaultdict
import itertools


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

    __words = dict()
    __words_sn = dict()
    __process_words_complete = False

    def __init__(self, path_to_file, encoding=__encoding):

        if not self.__is_clear():
            self.clear()

        print(path_to_file)
        file = self.__open_file(path_to_file, encoding)
        self.__handle_file(file)
        self.__handle_calculate_dict()
        file.close()

    def __set_absolute_path(self, path):
        self.__absolute_path_file = path

    def __set_raw_file(self, file):
        self.__raw_file = file

    def __is_clear(self):
        words = self.get_words()
        categories = self.get_categories()

        if not words and not categories:
            return True

    def __open_file(self, path, encoding):

        file = open(path, "r", encoding=encoding)
        self.__set_raw_file(file)

        return file

    def __handle_file(self, file):
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

    @staticmethod
    def __handle_line_string(line_string):
        return str(line_string.strip())

    def __processing_categories_add_mark(self, string):
        line_string = self.__handle_line_string(string)
        categories_mark = self.__categories_mark
        count_mark_categories = self.__process_categories_count_mark
        new_count_mark = count_mark_categories

        if  line_string.strip() == categories_mark:
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
        self.__words[word.get_value()] = word
        new_string = handle_string.strip_accents(word.get_value())
        if '*' in new_string:
            new_string = new_string.replace('*', '')
            self.__words_sn[new_string] = word

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

    def get_word(self, word):
        new_str_raw_word = word.lower()
        try:
            return self.__words[new_str_raw_word]
        except:
            return self.__get_word_normalize(new_str_raw_word)

    def __get_word_normalize(self, word):
        for word_key in self.__words_sn:
            if word.startswith(word_key):
                return self.__words_sn[word_key]
        return None

    def get_words(self):
        return self.__words.values()

    def find_id_category(self, identifier):
        identifier = str(identifier)
        categories = self.get_categories()
        for category in categories:
            if category.get_id() == identifier:
                return category
        raise NameError(
            "Categoria com id {} não definida. Verifique o dicionário e veja se a categoria foi definida.".format(id))

    def __handle_calculate_dict(self):
        words = self.get_words()
        categories = self.get_categories()

        self.__link_reference_words_and_categories(words, categories)

    def __link_reference_words_and_categories(self, words, categories):
        dict_word_category = defaultdict(list)
        dict_category_word = defaultdict(set)

        for word in words:
            word_categories = self.get_categories_by_word(word)
            dict_word_category[word] = word_categories
            word.set_categories(word_categories)
            for category_word in word_categories:
                dict_category_word[category_word].add(word)

        for category in categories:
            category_words = dict_category_word[category]
            category.set_words(category_words)

    def get_categories_by_word(self, word):
        categories_ids = word.get_categories_ids()
        categories = []
        for category_id in categories_ids:
            new_category = self.find_id_category(category_id)
            categories.append(new_category)
        return categories

    def __handle_proccess_sentences(self, sentence):
        raw_words = sentence.get_raw_words()
        sentence_words = []
        sentence_categories = []

        for raw_word in raw_words:
            word = self.find_word_by_raw_word(raw_word)
            if word:
                sentence_words.append(word)

        for word in sentence_words:
            categories = word.get_categories()
            sentence_categories.append(categories)


        sentence_categories = list(itertools.chain.from_iterable(sentence_categories))

        sentence.set_words(sentence_words)
        sentence.set_categories(sentence_categories)

        return sentence

    def find_word_by_raw_word(self, str_word):
        word = self.get_word(str_word)
        return word

    def process_sentence(self, sentence):
        sentence = Sentence(sentence)
        self.__handle_proccess_sentences(sentence)
        return sentence

    def clear(self):
        self.__words = dict()
        self.__categories = set()
        del self

