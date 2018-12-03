from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm

def post_create(request):
    form = PostForm()
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance
    }
    return render(request, "post_detail.html", context)
def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request):
    context = {
        "title": "Update"
    }
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    context = {
        "title": "Delete"
    }
    return HttpResponse("<h1>Delete</h1>")