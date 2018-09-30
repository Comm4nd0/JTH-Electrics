from django.shortcuts import render
from .models import Project, ProjectImage
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    images = ProjectImage.objects.all()

    return render(request, 'projects.html', {'projects': projects,
                                             'images': images,
                                             })


def project_detail(request, project_title):
    project = Project.objects.get(title=project_title)
    return render(request, 'single-project.html', {'project': project,
                                                   })

