class Point:
    #cls - ссылка на класс, внутри которого он объявлен
    #__new__ - вызывается перед созданием экземпляра
    def __new__(cls, *args, **kwargs):
        print(f"вызов __new__ для {str(cls)}")
        return super().__new__(cls) #Здесь мы возвращаем ссылку на наш класс

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def geniuos(self, string: str) -> None:
        return self.x + self.y
pt = Point(1, 2)
#Экземпляр еще не создан
#Все классы наследуются от класса object

print(pt)
#Паттерн Singleton - класс может иметь только 1 объект

class DataBase:
    __instance = None #Ссылка на экземляр класса, если его нет None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) #super().__new__(cls) ссылка на созданный объект
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = Noned

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")













































