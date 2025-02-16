
from django.urls import path
from .views import * # To connect different files we write .files_name import function_name


urlpatterns = [
path('home/',home),
# path('index/',index),
path('contacts/',contact)
]