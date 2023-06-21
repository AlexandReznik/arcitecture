from framework.templates_render import render
from framework.requestss import PostRequest

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Page:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))

class Contacts:
    def __call__(self, request, environ, method):
        if method == 'GET':
            return '200 OK', render('contact.html', date=request.get('date', None))
        elif method == 'POST':
            params = PostRequest().get_request_params(environ)
            with open('messages.txt', 'a') as file:
                file.write(f'Message: {params}\n')
                file.write('---------------------------\n')
            return '200 OK', render('contact.html', date=request.get('date', None))
        else:
            return {
                'status': '405 Method Not Allowed',
                'headers': [('Content-type', 'text/html')],
                'content': '405 Method Not Allowed'
            }