from django.db import models
from django.conf import settings
from datetime import datetime

class Plate(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="uploads/plates/", null=True, blank=True)

    def __str__(self):
        return self.name

    def actual_cost(self):
        qs = self.platecost_set.exclude(end_period=datetime.now())
        return qs[0]

    class Meta:
        ordering = ("name",)


class DaySpecial(models.Model):

    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date.day) + '/' + str(self.date.month) + '/' + str(self.date.year)

    class Meta:
        ordering = ("date",)


class PlateCost(models.Model):

    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    cost = models.FloatField()
    since = models.DateTimeField(auto_now=True)
    end_period = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.plate.name + " = " + str(self.cost)


class Menu(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    plates = models.ManyToManyField(Plate)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Order(models.Model):

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    payed = models.BooleanField(default=False)
    plates = models.ManyToManyField(Plate, through='OrderHasPlate', through_fields=('order', 'plate'))
    ready = models.BooleanField(default=False)

    def __str__(self):
        client_name = self.client.first_name + " " + self.client.last_name
        datetime = self.datetime.__str__()
        return client_name + " - " + datetime


class OrderHasPlate(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
