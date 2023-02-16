import datetime

from simba_framework.templator import render
from components.models import Engine

site = Engine()
class Index:
    def __call__(self, request: dict):
        return "200 OK", render('index.html', objects_list=site.categories)

class About:
    def __call__(self, request: dict):
        return "200 OK", render("about.html")

#
class StudyPrograms :
    def __call__(self, request: dict):
        return "200 OK", render("study-programs.html", date=datetime.date.today())


class NotFound404:
    def __call__(self, request: dict):
        return "404 WHAT", "404 PAGE NOT FOUND"


class Course_list:
    """Находит в памяти нужную категорию по id из get запроса
    и отправляет в шаблон курсы, относящиеся к категории, имя
    категории и ее id
    """
    def __call__(self, request: dict):
        try:
            category = site.find_category_by_id(
                int(request.get('request_params')["id"])
            )
            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'

class Create_course:
    """Cоздает новый курс"""
    category_id = -1

    def __call__(self, request: dict):
        if request["method"] == 'POST':
            data = request.get("data")
            name = data["name"]
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course('record', name, category)
                site.courses.append(course)
            return '200 OK', render('course_list.html', objects_list=category.courses,
                                    name=name,
                                    id=category.id)
        else:
            try:
                self.category_id = int(request["request_params"]["id"])
                print(f"axx {request}")
                category = site.find_category_by_id(int(self.category_id))
                return "200 OK", render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return "200 OK", "No categories"

class CreateCategory:
    def __call__(self, request):
        if request["method"] == "POST":
            data = request['data']
            name = site.decode_value(data)
            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category) #!!!
            site.categories.append(new_category)
            return "200 OK", render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return "200 OK", render('create_category.html', categories=categories)
class Category_list:
    def __call__(self, request):
        categories = site.categories
        return "200 OK", render("category_list.html", objects_list=categories)

