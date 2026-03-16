from django.db import models

# Create your models here.
class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    muallif = models.CharField(max_length=100)
    nashr_yili = models.IntegerField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom