from django.db import models
from django.contrib.auth.models import AbstractUser
from Categories.models import (
    Career, Profession, ZodiacSign, Country, Companion,
    WorkMode, Alcohol, Smoking, Chronotype, Religion, Food,
    PersonalityFeature, Hobby
)
from images.models import Image


class Account(AbstractUser):

    avatar = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=255,
        blank = True,
        null = True,
    )

    surname = models.CharField(
        max_length=255,
        blank = True,
        null = True,
    )

    birth_date = models.DateField(
        blank = True,
        null = True,
    )

    GENDER_CHOICES = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
        )

    ten_words_about_me = models.CharField(
        max_length=255,
        blank = True,
        null = True,
    )

    career = models.ForeignKey(
        Career,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    profession = models.ForeignKey(
        Profession,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    originally_from = models.ForeignKey(
        Country,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    created = models.DateTimeField(
        auto_now_add=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    phone = models.CharField(
        max_length=20,
        blank = True,
        null = True,
    )

    companion = models.ForeignKey(
        Companion,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    work_mode = models.ForeignKey(
        WorkMode,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    alcohol = models.ForeignKey(
        Alcohol,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    smoking = models.ForeignKey(
        Smoking,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    chronotype = models.ForeignKey(
        Chronotype,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    religion = models.ForeignKey(
        Religion,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    food = models.ForeignKey(
        Food,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    personality_features = models.ForeignKey(
        PersonalityFeature,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    hobbies = models.ForeignKey(
        Hobby,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        )

    more_about_me = models.TextField(
        max_length=600,
        blank = True,
        null = True,
        default='more about me...'
    )


    def __str__(self):
        return self.username


class VkProfile(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )

    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    def __str__(self):
        return self.age


class FbProfile(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )

    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    def __str__(self):
        return self.age
