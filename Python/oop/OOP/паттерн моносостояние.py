class ThreaData:
    __shared_attrs = {
        'name': "thread1",
        "data": {},
        'id': 1
    }
    def __init__(self):
        #__dict__ - список атрибутов, которые имеет экзкмпляр класса
        self.__dict__ = self.__shared_attrs

    def show_attr(self):
        return self.__shared_attrs


th1 = ThreaData()
print(th1.show_attr())
th2 = ThreaData()
print(th2.show_attr())
th1.name = "new_name"
print(th1.show_attr(), th2.show_attr())
#Кроме того мы можем создавать абсолютно новые атрибуты, которые все равно будут в моносостоянии
th1.gavn = "prived"
print(th1.show_attr(), th2.show_attr())












