from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import Comments_form, New_post, Update_post

def post_handle(request, id):
    
    try:
        post = Post.objects.get(id=id)
    except:
        post = None
    if request.method == 'POST':
        form = Comments_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            print(f"User: {request.user}")  # Debugging: print user

            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_handle', id=id)
    else:
        form = Comments_form()
    return render(request, "post_main.html", {'post': post, 'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        print('idzie')

        form = New_post(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            print('jest')
            id = post.id
            print('za')
            return redirect('post_handle', id=id)
    else:
        form = New_post()
    return render(request, 'post_create.html', {'form': form})



@login_required
def post_delete(request, id):

    post = get_object_or_404(Post, id=id)
    print('start')
    if request.method == 'POST':
        if 'Delete' in request.POST:
            post.delete()
            posts = Post.objects.all().values()
            return render ( request,'index.html', {'mydata':posts})
    
                
    posts = Post.objects.all().values()
    return render (request, 'index.html', {'mydata':posts})


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST' and 'Edit' in request.POST:
        form = Update_post(instance=post)
        return render(request, 'post_edit.html', {'post': post, 'form': form})
    if request.method == 'POST':
        form = Update_post(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_handle', id=id)
    