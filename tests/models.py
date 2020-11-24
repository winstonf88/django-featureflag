from django.db import models


class BaseModel(models.Model):
    class Meta:
        app_label = "tests"
        abstract = True


class Person(BaseModel):
    name = models.CharField(max_length=50)


class Animal(BaseModel):
    species = models.CharField(max_length=50)
