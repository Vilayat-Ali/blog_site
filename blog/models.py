from django.db import models

# Create your blog model here

class blogModel(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="blog-img/", blank=False, null=False)
    subtitle = models.CharField(max_length=250)
    text = models.TextField(max_length=2500)
    def __str__(self):
        return self.title