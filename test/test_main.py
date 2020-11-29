from pyliwcbr.src.liwc import liwc as pyliwc

def liwc_class():
    liwc = pyliwc.Liwc("data/dictionaries/liwc_2015_pt2_sem_pulo_linhas.dic")

    sentence = liwc.process_sentence("Ola tudo bem?")
    print(sentence.get_words())
    print(sentence.get_categories())
    print(sentence.get_raw_words())
    print(sentence.get_raw_value())



liwc_class()