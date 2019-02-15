from rest_framework import serializers

from Categories.models import *
from Accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    career = serializers.SerializerMethodField()
    profession = serializers.SerializerMethodField()
    zodiac_sign = serializers.SerializerMethodField()
    originally_from = serializers.SerializerMethodField()
    companion = serializers.SerializerMethodField()
    work_mode = serializers.SerializerMethodField()
    alcohol = serializers.SerializerMethodField()
    smoking = serializers.SerializerMethodField()
    chronotype = serializers.SerializerMethodField()
    religion = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()
    personality_features = serializers.SerializerMethodField()
    hobbies = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'avatar',
            'name',
            'surname',
            'birth_date',
            'gender',
            'ten_words_about_me',
            'career',
            'profession',
            'zodiac_sign',
            'originally_from',
            'created',
            'modified',
            'phone',
            'companion',
            'work_mode',
            'alcohol',
            'smoking',
            'chronotype',
            'religion',
            'food',
            'personality_features',
            'hobbies',
            'more_about_me',
            ]

    def get_avatar(self, obj):
        return obj.avatar.url

    def get_career(self, obj):
            return obj.career.name

    def get_profession(self, obj):
            return obj.profession.name

    def get_zodiac_sign(self, obj):
            return obj.zodiac_sign.name

    def get_originally_from(self, obj):
            return obj.originally_from.name

    def get_companion(self, obj):
            return obj.companion.name

    def get_work_mode(self, obj):
            return obj.work_mode.name

    def get_alcohol(self, obj):
            return obj.alcohol.name

    def get_smoking(self, obj):
            return obj.smoking.name

    def get_chronotype(self, obj):
            return obj.chronotype.name

    def get_religion(self, obj):
            return obj.religion.name

    def get_food(self, obj):
            return obj.food.name

    def get_personality_features(self, obj):
            return obj.personality_features.name

    def get_hobbies(self, obj):
            return obj.hobbies.name
