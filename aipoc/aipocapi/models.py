from django.db import models

# Create your models here.
class robo(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField()
    temp = models.IntegerField()
    con_speed = models.IntegerField()
    cpu = models.IntegerField()
    camera = models.BooleanField()
    ir = models.BooleanField()
    def __str__(self):
        return "aipoc"
