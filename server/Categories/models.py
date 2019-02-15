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
    # user = models.ForeignKey(
    #     Account,
    #     on_delete = models.CASCADE,
    #     unique=True,
    #     )
    user = models.CharField(
        max_length = 250,
        unique = True,
        )
    husband = models.BooleanField(
        blank = True,
        null = True
    )
    wife = models.BooleanField(
        blank = True,
        null = True
    )
    friend_m = models.BooleanField(
        blank = True,
        null = True
    )
    friend_w = models.BooleanField(
        blank = True,
        null = True
    )
    baby = models.BooleanField(
        blank = True,
        null = True
    )
    teenager_m = models.BooleanField(
        blank = True,
        null = True
    )
    teenager_w = models.BooleanField(
        blank = True,
        null = True
    )
    son = models.BooleanField(
        blank = True,
        null = True
    )
    daughter = models.BooleanField(
        blank = True,
        null = True
    )
    mother = models.BooleanField(
        blank = True,
        null = True
    )
    father = models.BooleanField(
        blank = True,
        null = True
    )
    cat = models.BooleanField(
        blank = True,
        null = True
    )
    dog = models.BooleanField(
        blank = True,
        null = True
    )
    bird = models.BooleanField(
        blank = True,
        null = True
    )
    fish = models.BooleanField(
        blank = True,
        null = True
    )
    lizard = models.BooleanField(
        blank = True,
        null = True
    )
    snail = models.BooleanField(
        blank = True,
        null = True
    )
    snake = models.BooleanField(
        blank = True,
        null = True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
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
    # user = models.ForeignKey(
    #     Account,
    #     on_delete = models.CASCADE,
    #     unique = True,
    #     )
    user = models.CharField(
        max_length = 250,
        unique = True,
        )
    introvert = models.BooleanField(
        blank = True,
        null = True
    )
    ambivert = models.BooleanField(
        blank = True,
        null = True
    )
    extravert = models.BooleanField(
        blank = True,
        null = True
    )
    racionalnyi = models.BooleanField(
        blank = True,
        null = True
    )
    emocionalnyi = models.BooleanField(
        blank = True,
        null = True
    )
    optimist = models.BooleanField(
        blank = True,
        null = True
    )
    pessimist = models.BooleanField(
        blank = True,
        null = True
    )
    domosed = models.BooleanField(
        blank = True,
        null = True
    )
    neposeda = models.BooleanField(
        blank = True,
        null = True
    )
    serieznyi = models.BooleanField(
        blank = True,
        null = True
    )
    bezzabotnyi = models.BooleanField(
        blank = True,
        null = True
    )
    perfeczianist = models.BooleanField(
        blank = True,
        null = True
    )
    optimalist = models.BooleanField(
        blank = True,
        null = True
    )
    trebovatelnyi = models.BooleanField(
        blank = True,
        null = True
    )
    snishoditelnyi = models.BooleanField(
        blank = True,
        null = True
    )
    molchalivyi = models.BooleanField(
        blank = True,
        null = True
    )
    razgovorchivyi = models.BooleanField(
        blank = True,
        null = True
    )
    lenivyi = models.BooleanField(
        blank = True,
        null = True
    )
    trudolybivyi = models.BooleanField(
        blank = True,
        null = True
    )
    ambicioznyi = models.BooleanField(
        blank = True,
        null = True
    )
    neprityazatelnyi = models.BooleanField(
        blank = True,
        null = True
    )
    spokoynyi = models.BooleanField(
        blank = True,
        null = True
    )
    ishyshyi = models.BooleanField(
        blank = True,
        null = True
    )
    analitycheskyi = models.BooleanField(
        blank = True,
        null = True
    )
    gumanitarnyi = models.BooleanField(
        blank = True,
        null = True
    )

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name


class Hobby(models.Model):
    # user = models.ForeignKey(
    #     Account,
    #     on_delete = models.CASCADE,
    #     unique=True,
    #     )
    user = models.CharField(
        max_length = 250,
        unique = True,
        )
    sport = models.BooleanField(
        blank = True,
        null = True
    )
    music = models.BooleanField(
        blank = True,
        null = True
    )
    cinema = models.BooleanField(
        blank = True,
        null = True
    )
    cooking = models.BooleanField(
        blank = True,
        null = True
    )
    shoping = models.BooleanField(
        blank = True,
        null = True
    )
    theater = models.BooleanField(
        blank = True,
        null = True
    )
    traveling = models.BooleanField(
        blank = True,
        null = True
    )
    camping = models.BooleanField(
        blank = True,
        null = True
    )
    reading = models.BooleanField(
        blank = True,
        null = True
    )
    drawing = models.BooleanField(
        blank = True,
        null = True
    )
    handiwork = models.BooleanField(
        blank = True,
        null = True
    )
    doing_music = models.BooleanField(
        blank = True,
        null = True
    )
    collecting = models.BooleanField(
        blank = True,
        null = True
    )
    museums = models.BooleanField(
        blank = True,
        null = True
    )
    hunting = models.BooleanField(
        blank = True,
        null = True
    )
    fishing = models.BooleanField(
        blank = True,
        null = True
    )
    photo = models.BooleanField(
        blank = True,
        null = True
    )
    dancing = models.BooleanField(
        blank = True,
        null = True
    )
    magician = models.BooleanField(
        blank = True,
        null = True
    )
    herbalism = models.BooleanField(
        blank = True,
        null = True
    )
    learning_languages = models.BooleanField(
        blank = True,
        null = True
    )
    learning_history = models.BooleanField(
        blank = True,
        null = True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
