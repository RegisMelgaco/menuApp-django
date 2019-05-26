from django.db import models
from django.conf import settings


class Plate(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    cost = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class DaySpecial(models.Model):

    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date.day) + '/' + str(self.date.month) + '/' + str(self.date.year)

    class Meta:
        ordering = ("date",)


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

    def __str__(self):
        client_name = self.client.first_name + " " + self.client.last_name
        datetime = self.datetime.__str__()
        return client_name + " - " + datetime


class OrderHasPlate(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
