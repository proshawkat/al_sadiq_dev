from django.urls import path
from .views import get_must_pay

urlpatterns = [
    path('get_must_pay/', get_must_pay, name='get_must_pay'),
]
