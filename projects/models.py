from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that this field will be automatically added when the object is created

    def __str__(self):
        return self.title