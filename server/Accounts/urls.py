from django.urls import path

from Accounts.views import test_view

app_name = 'Accounts'

urlpatterns = [
    path('test/', test_view, name='test'),
]