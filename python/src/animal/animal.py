import unicodedata


class Animal:
    def __init__(self, animal_kind):
        self._animal_kind = animal_kind

    def get_animal_kind(self):
        return self._animal_kind

    def get_is_japanese(self):
        for ch in self._animal_kind:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
                return True
        return False


class TwoCats(Animal):
    def __init__(self):
        Animal.__init__(self, 'ねこ')
        self._str_animal_count = '二匹'

    def get(self):
        return f'{self._animal_kind}{self._str_animal_count}'
