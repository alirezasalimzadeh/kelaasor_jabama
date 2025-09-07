from django.urls import path
from .views import list_my_reservations

urlpatterns = [
    path('', list_my_reservations),
]