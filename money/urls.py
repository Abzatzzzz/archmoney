from django.urls import path

from . import views


app_name = "money"

urlpatterns = [
    path("", views.index, name="index"),
    path("deposit/", views.deposit, name="deposit"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("withdraw/", views.withdraw, name="withdraw"),
]
