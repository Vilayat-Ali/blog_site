from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home page"),
    path('blogs/', include('blog.urls'), name="Blog page"),
    path('projects/', include('project.urls'), name="Project")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
