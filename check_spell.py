from pyaspeller import YandexSpeller


def check(st_words: str) -> str:
    spell = YandexSpeller()
    st: str = spell.spelled(st_words)
    return st.strip()
