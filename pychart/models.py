from django.db import models

# Create your models here.
class Mbit(models.Model): #우리가 받고/보내야할 5개 모델 생성(int 형식)
    backend = models.IntegerField()
    frontend = models.IntegerField()
    game = models.IntegerField()
    data = models.IntegerField()
    security = models.IntegerField()