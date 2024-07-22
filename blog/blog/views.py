from django.shortcuts import render
from django.template import loader, TemplateDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
import os
from posts.models import Post

def home_view(request):
    posts = Post.objects.all()
    content = {'mydata': posts}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(content, request))




def post(request):
    pass

