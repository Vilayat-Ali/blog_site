from django.db import models

# project model
class projectModel(models.Model):
    title = models.CharField(max_length=150)
    pic = models.ImageField(upload_to="project-img/", blank=False, null=False)
    description = models.CharField(max_length=200)
    github = models.URLField(max_length=500, blank=True, null=True)
    webapp = models.URLField(max_length=500, blank = True, null = True)
    def __str__(self):
        return self.title
