from django.db import models

class services(models.Model):
    name_servive = models.CharField(max_length=100)
    price_service = models.CharField(max_length=20)

