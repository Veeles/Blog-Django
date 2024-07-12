from django.shortcuts import render
from django.template import loader, TemplateDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
import os
def home_view(request):
    return render(request, 'base.html')


def login(request):
    pass

def register(request):
    pass

def post(request):
    pass

def test_view(request):
    templates_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'blog', 'templates')
    output = f'BASE_DIR: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\n'
    output += f'Templates directory path: {templates_dir}\n'
    if os.path.exists(templates_dir):
        output += 'Templates directory exists'
    else:
        output += 'Templates directory does not exist'
    return HttpResponse(output.replace('\n', '<br>'))
