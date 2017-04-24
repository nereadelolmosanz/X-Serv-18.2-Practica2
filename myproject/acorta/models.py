from django.db import models

# Create your models here.
class Pages(models.Model):
    url = models.CharField(max_length=128)

    def __str__(self):
        return str(self.url)
