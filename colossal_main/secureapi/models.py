from django.db import models

# Create your models here.


class SecdataModel(models.Model):
    securetext = models.CharField()
    owner = models.ForeignKey()

    def __str__(self):
        return self.securetext
    

