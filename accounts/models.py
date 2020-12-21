from django.db import models


# Create your models here.
class HostRiskRating(models.Model):
    os_name = models.TextField()
    risk_lvl = models.CharField(max_length=20)
    nr_incidents = models.IntegerField()


class SecurityRiskOrigin(models.Model):
    risk_name = models.TextField()
    nr_incidents = models.IntegerField()


class SecurityBrowsers(models.Model):
    browser_name = models.TextField()
    market_trust = models.FloatField()
