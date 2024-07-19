from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import Comments_form
@login_required
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