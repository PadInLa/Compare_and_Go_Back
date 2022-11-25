from django.db import models


# Create your models here.
class ProductoRandom(models.Model):
    indice = models.IntegerField()
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    tienda = models.CharField(max_length=100)

    def get_precio(self):
        if self.precio:
            return self.precio[2:]