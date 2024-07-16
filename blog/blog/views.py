from django.shortcuts import render
from django.template import loader, TemplateDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
import os
from posts.models import Post
from .forms import Register

def home_view(request):
    posts = Post.objects.all().values()
    content = {'mydata': posts}
    template = loader.get_template('index.html')
    # return render(request, 'index.html')
    print(content)
    return HttpResponse(template.render(content, request))


def login(request):
    pass

def register(request):
    form = Register()
    return render(request, 'register.html', {'form': form})

def post(request):
    pass

