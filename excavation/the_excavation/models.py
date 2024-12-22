from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Excavation(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        ('pottery', 'Pottery'),
        ('tools', 'Tools'),
        ('bones', 'Bones'),
        ('jewelry', 'Jewelry'),
        ('samples', 'Samples'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excavation = models.ForeignKey(Excavation, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    depth = models.FloatField()
    coordinates_north = models.FloatField(blank=True, null=True)
    coordinates_east = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_item_type_display()} at {self.coordinates_north}, {self.coordinates_east}"