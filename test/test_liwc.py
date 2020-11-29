from pyliwcbr.src.liwc import liwc as pyliwc
import os


LIWC_PATH_DIRETORY = "data/dictionaries/"
LIWC_FILENAME = "liwc_2015_pt2_sem_pulo_linhas.dic"
LIWC_PATH_TO_DIC = LIWC_PATH_DIRETORY + LIWC_FILENAME
LIWC_NUMBER_CATEGORIES = 73
LIWC_NUMBER_WORDS = 14460

LIWC_CATEGORY_ID = 1
LIWC_CATEGORY_TAG = "FunctionWords"
LIWC_CATEGORY_SIZE_WORDS = 1426



def test_tc01_get_categories_size():
    liwc = pyliwc.Liwc(LIWC_PATH_TO_DIC)

    categories = liwc.get_categories()
    size_categories = len(categories)

    ERR_MESSAGE = "Quantidade de categorias não condiz com o definido. Tamanho definido {}; Tamanho existente {}".format(LIWC_NUMBER_CATEGORIES, size_categories)

    assert size_categories == LIWC_NUMBER_CATEGORIES, ERR_MESSAGE



def test_tc02_get_words_size():
    liwc = pyliwc.Liwc(LIWC_PATH_TO_DIC)

    words = liwc.get_words()
    words_size = len(words)

    ERR_MESSAGE = "Quantidade de palavras não condiz com o definido. Tamanho definido {}; Tamanho existente {}".format(
        LIWC_NUMBER_WORDS, words_size)

    assert words_size == LIWC_NUMBER_WORDS, ERR_MESSAGE


def test_tc03_find_category_by_id():
    liwc = pyliwc.Liwc(LIWC_PATH_TO_DIC)


    category = liwc.find_id_category(LIWC_CATEGORY_ID)

    ERR_MESSAGE = "Não foi possível encontrar a categoria pelo ID"

    assert category.get_id() == str(LIWC_CATEGORY_ID), ERR_MESSAGE




