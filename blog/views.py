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
    Post = blogModel.objects.all()
    context = {
            "title": Post.filter(title=blogname).title,
            "keywords": "",
            "description": Post.filter(title=blogname).text,
            "blog": Post.filter(title=blogname)
        }
    return render(request, 'blog/specificblog.html', context)

