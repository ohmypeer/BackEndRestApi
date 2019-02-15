from Accounts.models import Account
from Categories.models import (
    Companion, PersonalityFeature, Hobby,
)
from rest_framework.viewsets import ModelViewSet
from Accounts.serializers import (
    AccountSerializer, CompanionSerializer,
    HobbySerializer, PersonalityFeatureSerializer,
)


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.filter(name='test')
    serializer_class = AccountSerializer


class CompanionViewSet(ModelViewSet):
    queryset = Companion.objects.filter(user='test')
    serializer_class = CompanionSerializer


class PersonalityFeatureViewSet(ModelViewSet):
    queryset = PersonalityFeature.objects.filter(user='test')
    serializer_class = PersonalityFeatureSerializer


class HobbyViewSet(ModelViewSet):
    queryset = Hobby.objects.filter(user='test')
    serializer_class = HobbySerializer