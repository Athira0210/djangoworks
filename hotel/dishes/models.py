from django.db import models

class Dishes(models.Model):
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=150)
    rating=models.FloatField()

    def __str__(self):
        return self.name
