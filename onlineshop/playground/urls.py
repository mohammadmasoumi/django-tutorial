from django.urls import path
from .views import say_hello, say_bye

urlpatterns = [
    # trailing slash /
    # http://127.0.0.1:8000/playground/greeting  => say_hello
    # http://127.0.0.1:8000/playground/greeting/  => say_hello
    path('greeting/', say_hello),
    path('bye/', say_bye)
]
