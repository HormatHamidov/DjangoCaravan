from django.urls import path

from .views import *

app_name = 'colorapp'

urlpatterns = [
    path("list", meyve_view, name="meyve_view"),
]
