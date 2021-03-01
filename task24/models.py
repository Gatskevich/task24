from django.db import models
from django.contrib.postgres.fields import JSONField


class Storage(models.Model):
    name = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.name
