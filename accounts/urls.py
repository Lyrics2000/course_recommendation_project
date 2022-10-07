from django.urls import path
from .views import (
    signIn,
    signUp,
    logout
)

app_name = "accounts"


urlpatterns = [
    path("",signIn,name="signIn"),
    path("signUp/",signUp,name="signUp"),
    path("logout/user",logout,name="logout")
]