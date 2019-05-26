from django.db import models


class Plate(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Menu(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    plates = models.ManyToManyField(Plate)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
