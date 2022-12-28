from string import ascii_letters
class Person:
    S_RUS = "ёйцукенгшщзхъфывапролджэячсмитьбю"
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, fio: str, old: int, ps: str, weight: int) -> None:
        self.verify_fio(fio)
        self.verify_int_values(old, int, 14, 120)
        self.verify_int_values(weight, float, 20, 1000)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio: str) -> None:
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        list_fio_words = fio.split()
        if len(list_fio_words) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for word in list_fio_words:
            if len(word) < 1:
                raise TypeError("В фио должен быть хотябы один символ")
            if len(word.strip(letters)) != 0:  #!!!!!!!!!!!!!!!!
                raise TypeError("Можно использовать только буквенные символы")

    # @classmethod
    # def verify_old(cls, old: int) -> None:
    #     if type(old) != int or old < 14 or old > 120:
    #         raise TypeError("Указано неверное значение")

    # @classmethod
    # def verify_weight(cls, weight: float) -> None:
    #     if type(weight) != float or weight < 20 or weight > 1000:
    #         raise TypeError("Указано неверное значение")

    @classmethod
    def verify_int_values(cls, value: int, type_value, x: int, y: int) -> None:
        if type(value) != type_value or value < x or value > y:
            raise TypeError("Указано неверное значение")

    @classmethod
    def verify_ps(cls, ps: str) -> None:
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        passport_split = ps.split()
        if passport_split != 2 or len(passport_split[0]) != 4 or len(passport_split[1]) != 6:
            raise TypeError("Неверная запись паспорта")
        for ps_part in passport_split:
            if not ps_part.isdigit():
                raise TypeError("Серия и номер должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_int_values(old, int, 14, 120)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_int_values(weight, float, 20, 1000)
        self.__weight = weight

#Имя в данном случае будет неизменяемым
pers = Person("Еболон Какашевич епеп", 1, "1", 1)

