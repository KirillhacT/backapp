import quopri
from typing import Union

class User:
    pass

class Teacher:
    pass

class Student:
    pass

class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()

class Course:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)

class InteractiveCourse(Course):
    pass

class RecordCourse(Course):
    pass

class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        "record": RecordCourse,
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)

class Category:
    auto_id = 0
    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.courses_count()
        return result

class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_) -> Union[Teacher, Student]:
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None) -> Category:
        return Category(name, category)

    @staticmethod
    def create_course(type_, name, category) -> Union[InteractiveCourse, RecordCourse]:
        return CourseFactory.create(type_, name, category)

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace('+', ' '), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode("utf-8")

    def find_category_by_id(self, id):
        for item in self.categories:
            print("item", item.id)
            if item.id == id:
                return item
        raise Exception(f"��� ��������� � id = {id}")

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None


