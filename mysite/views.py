from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import contactForm

# Models
from blog.models import blogModel
from project.models import projectModel

def home(request):
    numberOfBlogs = str(len(blogModel.objects.all()))
    numberofProjects = str(len(projectModel.objects.all()))
    context = {
                "title": "Home",
                "keywords": "",
                "description": "",
                "blogNo": numberOfBlogs, # Number of blogs
                "projectNo": numberofProjects # Number of Projects

              }
    if(request.method == "POST"):
        thisContactForm = contactForm(request.POST)
        print(request.POST)
        if(thisContactForm.is_valid()):
            # Form info
            info = {
                    "name": thisContactForm.cleaned_data["name"],
                    "email": thisContactForm.cleaned_data["email"],
                    "subject": thisContactForm.cleaned_data["subject"],
                    "message": thisContactForm.cleaned_data["message"]
                   }
            # Sending mail
            send_mail(
                    info["subject"],
                    info["message"],
                    info["email"],
                    ['vilayatcodemysite@gmail.com'],
                    fail_silently=False,
                    )
        else:
            HttpResponseRedirect("/")
        
    return render(request, 'website/index.html', context)