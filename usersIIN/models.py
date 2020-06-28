from django.db import models


class Person(models.Model):
    IIN = models.IntegerField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    age = models.IntegerField()