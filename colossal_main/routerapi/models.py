from django.db import models

# Create your models here.


class Routerapi(models.Model):
    title = models.CharField()
    desc = models.CharField()

    def __str__(self):
        return self.title

