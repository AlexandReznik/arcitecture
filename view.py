from .render import render


class Index:
    def __call__(self, request):
        return '200 OK', render('./colour_perpule/index.html', date=request.get('date', None))


class Page:
    def __call__(self, request):
        return '200 OK', render('./colour_perpule/page.html', date=request.get('date', None))