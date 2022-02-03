# file name does not important
from django.urls import path
from .views import *


# django search for urlpatterns variable
urlpatterns = [
    path('hello/', say_hello),
    path('hello2/', say_hello_with_template),
]
