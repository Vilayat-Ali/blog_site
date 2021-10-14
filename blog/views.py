from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import blogModel

# Create your blog views here:
 
def blogListView(request):
    blogs = blogModel.objects.all()
    context = {
                "title": "Blogs",
                "keywords": "",
                "description": "",
                "blogs": blogs
              }
    return render(request, 'blog/index.html', context)

def specificBlog(request, blogname):
    blogs = blogModel.objects.all()
    requiredBlog = blogModel.objects.get(title=blogname)
    context = {
            "title": "Blogs",
            "keywords": "",
            "description": "",
            "blog": requiredBlog
        }
    return render(request, 'blog/specificblog.html', context)

