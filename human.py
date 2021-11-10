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
