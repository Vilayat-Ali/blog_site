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
        if(thisContactForm.is_valid()):
            # Form info
            info = {
                    "name": thisContactForm.cleaned_data["name"],
                    "email": thisContactForm.cleaned_data["email"],
                    "subject": thisContactForm.cleaned_data["subject"],
                    "message": "From: "+thisContactForm.cleaned_data["name"]+"\n"+"Email: "+ thisContactForm.cleaned_data["email"]+"\n"+"\n"+"Message: "+"\n"+thisContactForm.cleaned_data["message"]
                   }
            # Sending mail to me
            send_mail(
                    info["subject"],
                    info["message"],
                    info["email"],
                    ['vilayatcodemysite@gmail.com'],
                    fail_silently=False,
                    )
            # Sending mail to the sender
            send_mail(
                    "Thanks for contacting me!",
                    """Hi!
It's Syed Vilayat Ali Rizvi here!
    Thankyou for visiting my website and contacting me. I have noted all your contcat information , which you can review down below:

Name: {}
Email: {}

I will be contacting you as soon as I get free time! For reading my blogs fo
Take care!

Ba-Bye""".format(info["name"], info["email"]),
                    "vilayatcodemysite@gmail.com",
                    [info["email"]],
                    fail_silently=False,
                    )
        else:
            HttpResponseRedirect("/")
        
    return render(request, 'website/index.html', context)