# lights/models.py

from django.db import models
from django.contrib.auth.models import User

class Lamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    wattage = models.FloatField()
    hours_used = models.FloatField(default=0)
    estimated_lifetime_hours = models.FloatField()

    def power_consumed(self):
        return self.wattage * self.hours_used

    def remaining_lifetime(self):
        return max(0, self.estimated_lifetime_hours - self.hours_used)

    def __str__(self):
        return self.name
