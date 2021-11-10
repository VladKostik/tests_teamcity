import pytest
from .human import Human


def test_grow_method(human_1):
    human_1.grow()
    assert human_1.age == 34


def test_change_gender_method(human_1, monkeypatch):
    monkeypatch.setattr(human_1, '_Human__gender', 'male')
    human_1.change_gender('female')
    assert human_1.gender == 'female'


def test_change_gender_exception(human_1):
    with pytest.raises(Exception):
        human_1.change_gender('male')
    assert Exception  # excessive assert


def test_gender_method(human_1):
    assert human_1.gender == 'male'


def test_age_method(human_1):
    assert human_1.age == 33


def test_gender_validation_method():
    human2 = Human('Anton', 26, 'fucking fagot')
    with pytest.raises(Exception):
        human2._Human__validate_gender(human2.gender)
    assert Exception


def test_is_alive_method_for_dead(human_1):
    with pytest.raises(Exception):
        for i in range(100):
            human_1.grow()
    assert human_1._Human__status == 'dead'


def test_is_alive_method_for_alive(human_1):
    for i in range(67):
        human_1.grow()
    assert human_1._Human__status == 'alive'

class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__status = "alive"
        self.__age_limit = 100

    def grow(self):
        self.__is_alive()
        if self.__age < self.__age_limit:
            self.__age += 1
        else:
            self.__status = "dead"

    def __is_alive(self):
        if self.__status == "alive":
            return True
        else:
            raise Exception(f"{self.__name} is already dead...")

    def change_gender(self, gender: str):
        self.__is_alive()
        self.__validate_gender(gender)

        if self.__gender != gender:
            self.__gender = gender
        else:
            raise Exception(f"{self.__name} already has gender '{gender}'")

    @staticmethod
    def __validate_gender(gender: str):
        if gender not in ["male", "female"]:
            raise Exception("Not correct name of gender")

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender
