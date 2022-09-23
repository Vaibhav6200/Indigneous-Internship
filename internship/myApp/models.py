from django.db import models


class Asgard(models.Model):
    geography = models.CharField(max_length=255)
    history = models.CharField(max_length=255)
    culture = models.CharField(max_length=255)
    language = models.CharField(max_length=255)