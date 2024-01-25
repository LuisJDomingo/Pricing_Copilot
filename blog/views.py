from django.shortcuts import render
from blog.models import Post

# Create your views here.

def blog(request):
    # tu lógica de vista aquí
    posts=Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})