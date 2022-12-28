from dataclasses import dataclass, asdict

#Датакласс автоматически и прописывает специальные методы по умолчанию
# Прописывать внутри датакласса функционал считается плохой практикой
#Нужкен исключительно для хранения данных

@dataclass
class User:
    name: str
    age: int = 0

    # def get_name(self):
    #     return f"Name is {self.name}"

# a = User("Pysh", 12)
# print(a.get_name(), a.age)

class UserHandler:
    def __init__(self, name, age):
        self.user: User = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, value):
        self.user.__dict__[key] = value

b = UserHandler("Egor", 5)
print(b.get_dataclass())
b.edit("name", "gay")
print(b.get_dataclass())
