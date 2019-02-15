from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):

    GENDER_CHOICES = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
