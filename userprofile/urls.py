from userprofile.views import UserLoginview, usersignupview, logout_view
from django.urls import path

app_name = "userprofile"

urlpatterns = [
    path("login/", UserLoginview.as_view(), name="login"),
    path("register/", usersignupview.as_view(), name="register"),
    path("logout/", logout_view, name="logout"),
]
