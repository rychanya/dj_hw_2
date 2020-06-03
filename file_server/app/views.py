import datetime
import os

from django.conf import settings

from django.shortcuts import render


def file_list(request, date=None):

    def parse_stat(file):
        path = os.path.join(settings.FILES_PATH, file)
        stat = os.stat(path)
        return {
            'name': file,
            'ctime': datetime.datetime.fromtimestamp(stat.st_ctime),
            'mtime': datetime.datetime.fromtimestamp(stat.st_mtime)
        }
    

    template_name = 'index.html'
    files = [parse_stat(file) for file in os.listdir(settings.FILES_PATH)]
    if date:
        files = [file for file in files if file['ctime'].date() == date.date()]
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = os.path.join(settings.FILES_PATH, name)
    context = {
        'file_name': path,
        'file_content': 'NOT FOUND!!!'
    }
    if os.path.isfile(path):
        with open(path, mode='r') as file:
            context['file_content'] = file.read()
    return render(
        request,
        'file_content.html',
        context=context
    )

