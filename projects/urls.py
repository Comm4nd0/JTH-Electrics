from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:project_title>', views.project_detail, name='single_project'),
]
