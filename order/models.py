from django.db import models

# Create your models here.

class Order(models.Model):

   
    user_id = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_address = models.CharField(max_length=90)
    order_date = models.DateField()
    def __str__(self):
        return self.user_id