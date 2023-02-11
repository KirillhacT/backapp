from datetime import datetime
from dataclasses import dataclass
from typing import Iterable, Sequence, Mapping, TypeVar, Callable
#Optional
def print_hello(name: str | None = None) -> None:
    print(f"hello {name}" if name is not None else "hello anon!")

print_hello("asd")

#Контейнеры
@dataclass
class User:
    birthday: datetime
users = [
    User(birthday=datetime.fromisoformat("1988-01-01")),
    User(birthday=datetime.fromisoformat("1985-07-29")),
    User(birthday=datetime.fromisoformat("2000-10-10")),
]

# def get_younger_user(users: Iterable[User]) -> User:
#Iterable - то, по чему мы можем итерироваться
def get_younger_user(users: Sequence[User]) -> User:
    #Sequence - итерация + обращение по индексу
    if not users:
        raise ValueError("Empty users!")
    sorted_users = sorted(users, key=lambda x: x.birthday)
    return sorted_users[0]
print(get_younger_user(users))

def smth(some_users: Mapping[str, User]) -> None:
    #Mapping - тип обращения как к словарю (в качества ключа и значения указываем отдельно)
    print(some_users["alex"])

smth({
    "alex": User(birthday=datetime.fromisoformat("1988-01-01")),
    "petr": User(birthday=datetime.fromisoformat("2000-10-10"))
})

#Типизация кортежей
three = tuple[int, int, int] #Кортеж из 3 intов
infinity_int = tuple[int, ...] #Кортеж из произвольного кол-ва intов

#Дженерики
T = TypeVar("T")

def first(iterable: Iterable[T]) -> T | None:
    # T - экземляр любого типа (int, float, str, ...)
    for element in iterable:
        return element
print(first(["one", "two"]))
print(first([1, 2, 3]))
print(first([]))

#Callable
def my_sum(a: int, b: int) -> int:
    return a + b
def process_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    #Callable - то, что мы можем вызвать
    return operation(a, b)
print(process_operation(my_sum, 1, 5))

my_book: str = "Kek"



