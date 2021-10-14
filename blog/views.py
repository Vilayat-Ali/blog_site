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
    Post = blogModel.objects.all().filter(title=blogname)[0]
    print(Post)
    context = {
            "title": Post.title,
            "keywords": "",
            "description": Post.text,
            "blog": Post
        }
    return render(request, 'blog/specificblog.html', context)

