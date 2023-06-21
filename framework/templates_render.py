from jinja2 import Template
import os

# def render(template_name, folder='coulour_purple', **kwargs):
#     file_path = os.path.join(folder, template_name)
#     with open(file_path, encoding='utf-8') as f:
#         template = Template(f.read())
#     return template.render(**kwargs)



def render(template_name, folder='templates', **kwargs):
    file_path = os.path.join(folder, template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)