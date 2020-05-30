from django.db import models

# Create your models here.

from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    vkID = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    adID = None

    def generateID(self):
        self.adID = hash(self.name) + hash(self.location) + hash(self.time)


