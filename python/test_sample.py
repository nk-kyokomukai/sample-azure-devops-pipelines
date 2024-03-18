from animal.animal import Animal
import pytest


class TestAnimal:
    params = [
        {'test': 1, 'args': '犬'},
        {'test': 2, 'args': 'Gorilla'}
    ]

    @pytest.fixture(scope='class', params=params)
    def preprocessing(self, request):
        # 前処理を記述
        #  ////
        # テスト
        yield request.param
        # 後処理を記述
        # ////

    def test_get(self, preprocessing):
        sample_animal = Animal(preprocessing['args'])

        if preprocessing['test'] == 1:
            assert sample_animal.get_animal_kind() == '犬'
            assert sample_animal.get_is_japanese()

        elif preprocessing['test'] == 2:
            assert sample_animal.get_animal_kind() == 'Gorilla'
            assert not sample_animal.get_is_japanese()
