from datetime import date
from view import Index, Page


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page/': Page(),
    # '/contacts/': Contacts(),
}
