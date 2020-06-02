from django.urls import path, register_converter

from app.views import file_content, file_list

from datetime import datetime

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

class DateConverctor:

    regex = r'\d{4}-\d{2}-\d{2}'
    str_format = r'%Y-%m-%d'

    def to_python(self, value):
        date = datetime.strptime(self.str_format, value)
        print(date)
        return date

    def to_url(self, value):
        date = value.strftime(self.str_format)
        print(date)
        return date

register_converter(DateConverctor, 'dt')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('<dt:date>/', file_list, name='file_list'),
    path('', file_list),
    # задайте необязательный параметр "date"
    # для детальной информации смотрите HTML-шаблоны в директории templates
    path('<str:name>', file_content, name='file_content'),
]
