from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class ZodiacSign(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Companion(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    human_or_pet = models.CharField(
        max_length = 5,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class WorkMode(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Alcohol(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Smoking(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Chronotype(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class PersonalityFeature(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        )
    description = models.CharField(
        max_length = 250,
        blank = True,
        null = True
        )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.name
