from Accounts.models import Account
from rest_framework.viewsets import ModelViewSet
from Accounts.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.filter(name='test')
    serializer_class = AccountSerializer
