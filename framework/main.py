from quopri import decodestring

class PostRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'строка после декод - {data_str}')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data


class GetRequest:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequest.parse_input_data(query_string)
        return request_params
    
    
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


