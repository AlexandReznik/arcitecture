# arcitecture
To start framework make file uwsgi.ini and add content like that:
[uwsgi]
module = simple_wsgi:app
master = true
processes = 5
socket = 127.0.0.1:8000
chmod-socket = 660
vacuum = true
die-on-term = true
Then you can run this framework
uwsgi --ini uwsgi.ini
