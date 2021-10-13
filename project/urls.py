from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectListView, name="Project List View"),
    path('<projectname>/', views.specificProject, name="Specific Project View"),
]
