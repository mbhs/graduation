from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Donation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tickets = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])

    def __str__(self):
        return 'Donation: ' + self.name

class Request(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    tickets = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])

    def __str__(self):
        return 'Request: ' + self.name