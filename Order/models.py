from django.db import models


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
