from time import time

# В обих классах используется структурный паттерн - Декоратор.
# Этот паттерн динамически добавляет объекту новфый функционал,
# что в данной ситуации упрощает добавление урлов, как по мне.
# То есть аналогия как во Flask, теперь урлы просто добалсяются в файле view.py
# посредством декорирования самого вью. Примерно так же работает
# декоратор Debug, который выводит в терминал время выполнения определенной функции, которая была задекорирована,
# и ее название

class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        
        def timeit(method):
            def timed(*args, **kw):
                ts = time()
                result = method(*args, **kw)
                te = time()
                delta = te - ts

                print(f'{self.name} completed in {delta:2.2f} ms')
                return result
            return timed

        return timeit(cls)