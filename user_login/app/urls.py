#app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('staff', staffView),
    path('user', userView),
    path('accounts/signup', signup),
    path('', index),
]
