from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=150)
    category=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    rating=models.FloatField()

    def __str__(self):
        return self.name