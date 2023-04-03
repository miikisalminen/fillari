from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField(null = True)

    def _str_(self):
        return self.name


class Journey(models.Model):
    departure_station = models.CharField(max_length=30)
    return_station = models.CharField(max_length=30)
    distance = models.FloatField(null = True)
    duration = models.IntegerField(null = True)

    def __str__(self):
        return(self.departure_station + " - " + self.return_station)