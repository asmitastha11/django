
from django.urls import path
from .views import * # To connect different files we write .files_name import function_name


urlpatterns = [
path('home/',home),
# path('index/',index),
# path('contacts/',contact)
path('task/',task),
path('task/create/',task_create),
path('task/<pk>/',mark_complete),
path('task/<pk>/edit/',mark_edit),
path('task/<pk>/delete/',mark_delete),
]