import re


class Sentence:
    regex_to_split_word = "\w+"
    __raw_value: ""
    __raw_words = []
    __words: None
    __categories: None

    def __init__(self, sentence_string):
        self.__set_raw_value(sentence_string)
        self.__handle_sequence(sentence_string)
        pass

    def __set_raw_words(self, raw_words):
        self.__raw_words = raw_words

    def __set_raw_value(self, raw_value):
        self.__raw_value = raw_value

    def __handle_raw_words_in_sentence(self):
        regex = Sentence.regex_to_split_word
        sentence = self.__raw_value
        r_words = re.findall(regex, sentence)
        return r_words

    def get_raw_words(self):
        return self.__raw_words

    def __handle_sequence(self, sentence):
        raw_words = self.__handle_raw_words_in_sentence()
        self.__set_raw_words(raw_words)

    def set_words(self, words):
        self.__words = words

    def set_categories(self, categories):
        self.__categories = categories


def __test_class():
    msg = "Olá,,,, tudo bem?"
    s = Sentence(msg)


__test_class()
