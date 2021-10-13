from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogListView, name="Blog List View"),
    path('<blogname>/', views.specificBlog, name="SpecificBlog")
]