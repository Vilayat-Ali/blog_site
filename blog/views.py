from django.shortcuts import render
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
    for blog in blogs:
        if(blog.title == blogname):
            requiredBlog = blog
            break
    context = {
            "title": "Blogs",
            "keywords": "",
            "description": "",
            "blog": requiredBlog
            }
    return render(request, 'blog/specificblog.html', context)

