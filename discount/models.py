from django.db import models

# Create your models here.

class Discount (models.Model):
    products = models.CharField(max_length=70)
    expiry_date = models.DateField()
    code_discount = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=6, decimal_places=2)
    minimum_purchase = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.products
