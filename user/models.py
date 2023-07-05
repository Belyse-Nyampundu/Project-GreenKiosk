from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    def __str__(self):
        return self.first_name
