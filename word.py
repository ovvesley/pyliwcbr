class Word:
    __raw_text = ""
    __categories_ids = set()
    __value = ""

    def __init__(self, line_string):
        self.__handle_line_string_word(line_string)

    def __set_raw_text(self, raw_text):
        self.__raw_text = raw_text

    def __set_categories_ids(self, categories):
        self.__categories_ids = categories

    def __set_value(self, value):
        self.__value = value

    def __handle_line_string_word(self, line):
        line_split = line.split("\t")

        raw_text = line
        value_word = line_split.pop(0)
        categories = line_split

        self.__set_categories_ids(categories)
        self.__set_raw_text(raw_text)
        self.__set_value(value_word)





def __test_class():
    word1 = Word("empurrarei	20	92	100	101")
    word2 = Word("encardido	30	32	120	121")
    word3 = Word(":\	30	32	120	122")

__test_class()