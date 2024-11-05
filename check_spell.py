from pyaspeller import YandexSpeller
from pyaspeller import Word


def check_spell(word: str) -> str:
    spell = YandexSpeller()
    st: str = spell.spelled(word)
    return st
