from quopri import decodestring
from .requests import GetRequest, PostRequest

    
    
class Application:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_list = routes_obj
        self.fronts_list = fronts_obj
        
    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        method = environ['REQUEST_METHOD']
        request['method'] = method
        
        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = Application.decode_value(data)
            print('Post', Application.decode_value(data))
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = Application.decode_value(request_params)
            print('Get', Application.decode_value(request_params))
            
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


