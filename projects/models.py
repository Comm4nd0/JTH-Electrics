from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete='CASCADE')
    image = models.ImageField()