from wsgiref.simple_server import make_server

from .main import Application
from urls import routes, fronts


application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Run on port 8080...")
    httpd.serve_forever()