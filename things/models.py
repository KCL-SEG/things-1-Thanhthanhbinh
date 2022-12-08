from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)