from django.db import models


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ShopItem(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0, blank=True)
    price = models.IntegerField(default=0)
    is_exists = models.BooleanField(default=True)
