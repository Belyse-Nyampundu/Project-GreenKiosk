from django.db import models

class Cart(models.Model):
    products = models.CharField(max_length=90)
    id_number = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.products

# Create your models here.
