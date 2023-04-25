from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return(render(request,'/home/guruprasath/Desktop/Blog_django_proj/blog/templates/home.html',{}))