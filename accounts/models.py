from django.db import models


# Create your models here.
class HostRiskRating(models.Model):
    os_name = models.TextField()
    risk_lvl = models.CharField(max_length=20)
    nr_incidents = models.IntegerField()
