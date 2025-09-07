from django.urls import path
from .views import list_transactions

urlpatterns = [
    path('', list_transactions)
]