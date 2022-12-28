class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        '''self - ссылка на экземпляр класса Integer (y)
        owner - ссылка на сам класс - Integer
        name - ссылка на имя экземпляра (x, y)'''
        self.name = "__" + name #__y

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        '''self - ссылается на экземпляр класса Integer (y)
        instance - на экземпляр Point3D
        value - значение, которое мы присваиваем'''
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        #Лучше будет обращаться через setattr или getattr не обращаясь к коллекции __dict__
        # instance.__dict__[self.name] = value
        return setattr(instance, self.name, value)


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "__x"


#Дескриптор - класс, который содержит в себе геттеры и сеттеры
class Point3D:
    x = Integer()
    y = Integer()
    xr = ReadIntX()

    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    #x
    # @property
    # def x(self):
    #     return self.__x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self.__x = coord


p = Point3D(1, 2)
print(p.__dict__)
print(p.y)
print(p.x)
p.x = 221
print(p.x)