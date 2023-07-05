from datetime import date
from view import Index, Page, CoursesList, CreateCourse, CreateCategory, CategoryList, CopyCourse, \
    AddStudentByCourseCreateView, StudentListView, StudentCreateView, CourseApi


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page/': Page(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse(),
    '/student-list/': StudentListView(),
    '/create-student/': StudentCreateView(),
    '/add-student/': AddStudentByCourseCreateView(),
    '/api/': CourseApi(),
}
