from django.db import models

# Create your models here.
class BusDetails(models.Model):
    busName = models.CharField(max_length=40)
    busFrom = models.CharField(max_length=40)
    busTo = models.CharField(max_length=40)
    busTime = models.TimeField()
    busTicket = models.IntegerField(default=None)


    def __str__(self):
        return self.busName


