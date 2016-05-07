from django.db import models
#from django.db.models import Model

# Create your models here.
class Colors(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=40)
    hex = models.CharField(unique=True, max_length=7)
    red = models.PositiveSmallIntegerField(null=True)
    green = models.PositiveSmallIntegerField(null=True)
    blue = models.PositiveSmallIntegerField(null=True)


    def __str__(self):
        return  self.name