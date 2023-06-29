from typing import Any
from framework.templates_render import render
from patterns.create_patterns import Engine, Logger
from patterns.structure_patterns import AppRoute, Debug

site = Engine()
logger = Logger("main")
routes = {}

@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 Ok', render('index.html', objects_list=site.categories)

@AppRoute(routes=routes, url='/page/')
class Page:
    @Debug(name='About')
    def __call__(self, request):
        return '200 Ok', render('page.html', date=request.get('date', None))

@AppRoute(routes=routes, url='/courses-list/')
class CoursesList:
    @Debug(name='CoursesList')
    def __call__(self, request):
        logger.log('Courses list')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 Ok', render('courses_list.html',
                                    objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 Ok', 'No courses yet'
        
@AppRoute(routes=routes, url='/create-course/')  
class CreateCourse:
    
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category = None
            
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                course = site.create_course('record', name, category)
                site.courses.append(course)
            return '200 Ok', render('courses_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))
                return '200 Ok', render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 Ok', 'No categories have been added yet'

@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    @Debug(name='CreateCategory')
    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None
            
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 Ok', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 Ok', render('create_categories.html',
                                    categories=categories)

@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logger.log('Category list')
        return '200 OK', render('category_list.html',
                                objects_list=site.categories)

@AppRoute(routes=routes, url='/copy-course/')
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']

            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 Ok', render('courses_list.html',
                                    objects_list=site.courses,
                                    name=new_course.category.name)
        except KeyError:
            return '200 Ok', 'No courses have been added yet'
