from __future__ import unicode_literals

from django.db import models


class Survey(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    innodation = models.BooleanField()
    argile = models.BooleanField()
    mouvement_terrain = models.BooleanField()
    cavite = models.BooleanField()
    seisme = models.BooleanField()
    sites_pollues = models.BooleanField()
    installations_classees = models.BooleanField()
    canalisation = models.BooleanField()
    nucleair = models.BooleanField()