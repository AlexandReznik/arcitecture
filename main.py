

class Application:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_list = routes_obj
        self.fronts_list = fronts_obj

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')

        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            ValueError
        request = {}
        
        for front in self.fronts_list:
            front(request)
        
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
