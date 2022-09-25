from os import name
from django.urls import path

app_name = "homepage"

from .views import (
    index,
    courses,
    raisec
)

urlpatterns = [
    path('', index,name="homepage"),
    path('courses/',courses,name='courses'),
    path('raisec/',raisec,name="raisec")
 
]