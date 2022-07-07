from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    
    #this make the objects in database appear. order_by is how you order the objects.
    blogs = Blog.objects.order_by('-date')

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html',{'blog':blog})


