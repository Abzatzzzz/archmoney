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
    path(
        "create_dep_category/",
        views.DepCategoryCreateView.as_view(),
        name="create_dep_category",
    ),
    path(
        "create_with_category/",
        views.create_with_category,
        name="create_with_category",
    ),
]
