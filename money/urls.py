from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deposit/", views.deposit, name="deposit"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("withdraw/", views.withdraw, name="withdraw"),
]
