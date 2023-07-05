from django.db import models

# Create your models here.

class Review (models.Model):
    product = models.CharField(max_length= 90)
    user_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    ratings = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.product
