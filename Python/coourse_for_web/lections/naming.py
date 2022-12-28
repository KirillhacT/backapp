#говнокод
def pv(p, v):
    if p == "f":
        return v >= 56.5
    elif p == "m":
        return v >= 61.5

# print(pv("m", 54))


#норм код (комментарий не читается интерпретатором)
def is_person_retiree(age: int, sex: str) -> bool:
    """документация о функции - возвращет True, если человек пенсионер, 
    в противном случае False"""
    if sex == "female":
        return age >= 56.5
    elif sex == "male":
        return age >= 61.5
print(is_person_retiree(sex="female", age=57))
print(is_person_retiree.__annotations__) #аннотации
print(is_person_retiree.__doc__) #документация функции


