from django.shortcuts import render
from .models import projectModel

# Create your views for projects are: 

def projectListView(request):
    projects = projectModel.objects.all()
    context = {
                "title": "Projects",
                "keywords": "",
                "description": "",
                "projects": projects
    }
    return render(request, 'projects/index.html', context)

def specificProject(request, projectname):
    projects = projectModel.objects.all()

    for project in projects:
        if(project.title == projectname):
            requiredProject = project
            break

    context = {
                "title": project.title,
                "keywords": "",
                "description": "",
                "project": requiredProject
    }
    return render(request, 'projects/projectspecific.html', context)
              