from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=1000)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    def __str__(self):
        return self.title