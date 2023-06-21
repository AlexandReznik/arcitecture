from quopri import decodestring
from .requestss import GetRequest, PostRequest
# import requestss
    
    
class Application:
    # def __init__(self, routes_obj, fronts_obj):
    #     self.routes_list = routes_obj
    #     self.fronts_list = fronts_obj
        
    # @staticmethod
    # def decode_value(data):
    #     new_data = {}
    #     for k, v in data.items():
    #         val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
    #         val_decode_str = decodestring(val).decode('UTF-8')
    #         new_data[k] = val_decode_str
    #     return new_data

    # def __call__(self, environ, start_response):
        
    #     path = environ.get('PATH_INFO', '/')
    #     request = {}
    #     method = environ['REQUEST_METHOD']
    #     request['method'] = method
        
    #     if method == 'POST':
    #         data = PostRequest().get_request_params(environ)
    #         request['data'] = Application.decode_value(data)
    #         print('Post', Application.decode_value(data))
    #     if method == 'GET':
    #         request_params = GetRequest().get_request_params(environ)
    #         request['request_params'] = Application.decode_value(request_params)
    #         print('Get', Application.decode_value(request_params))
            
    #     if path in self.routes_list:
    #         view = self.routes_list[path]
    #     else:
    #         ValueError
    #     request = {}
        
    #     for front in self.fronts_list:
    #         front(request)
        
    #     code, body = view(request)
    #     start_response(code, [('Content-Type', 'text/html')])
    #     return [body.encode('utf-8')]


    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = Application.decode_value(data)
            print(f'Нам пришёл post-запрос: {Application.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = Application.decode_value(request_params)
            print(f'Нам пришли GET-параметры:'
                  f' {Application.decode_value(request_params)}')

        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = [b'404 Page not found']

        for front in self.fronts_lst:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

