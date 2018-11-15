from django.http import HttpResponse
from django.shortcuts import render

def post_create(request):
    context = {
        "title": "Create"
    }
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    context = {
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