# main_app/models.py

from django.db import models

class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.species

class Feeding(models.Model):
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    date = models.DateField()
    meal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.finch.species} - {self.date}"

class Toy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
