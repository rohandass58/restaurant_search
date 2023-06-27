from django.db import models
import jsonfield


class Restaurants(models.Model):
    id = models.IntegerField(primary_key=True, null = False,)
    name = models.CharField(max_length=100, null = False,)
    location = models.CharField(max_length=100, null =False,)
    items = jsonfield.JSONField(default = dict)




