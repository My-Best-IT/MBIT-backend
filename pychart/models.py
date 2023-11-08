from django.db import models

# Create your models here.
class Mbit(models.Model):
    backend = models.IntegerField()
    frontend = models.IntegerField()
    game = models.IntegerField()
    data = models.IntegerField()
    security = models.IntegerField()