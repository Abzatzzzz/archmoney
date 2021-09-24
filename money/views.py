from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from . import services
from django.views.generic import CreateView
from . import models
from .forms import (
    DepositForm,
    WithdrawForm,
    UserRegisterForm,
    UserLoginForm,
    DepCategoryCreateForm,
)

from datetime import date


@login_required(login_url="login/")
def index(request):
    # year = int(t[0:4])
    t = str(date.today())
    month = int(t[5:7])
    positive_balance = models.Deposit.objects.filter(
        date__month=month
    ).aggregate(Sum("uan"))["uan__sum"]
    negative_balance = models.Withdraw.objects.filter(
        date__month=month
    ).aggregate(Sum("uan"))["uan__sum"]
    context = {
        "all_deposits": models.Deposit.objects.filter(
            date__month=month
        ).order_by("-date"),
        "all_withdraws": models.Withdraw.objects.filter(
            date__month=month
        ).order_by("-date"),
        "positive_balance": positive_balance,
        "negative_balance": negative_balance,
    }
    if positive_balance and negative_balance:
        context["total_balance"] = positive_balance - negative_balance
    else:
        context["total_balance"] = "0"
    return render(request, "money/index.html", context)


# @login_required(login_url="login/")
# def create_dep_category(request):
#    if request.method == "POST":
#        form = DepCategoryForm(request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, "Category added !")
#            return redirect("money:create_dep_category")
#    form = DepCategoryForm()
#    context = {"form": form, "categories": models.DepCategory.objects.all()}
#    return render(request, "money/create_dep_category.html", context)
class DepCategoryCreateView(CreateView):
    template_name = "money/create_dep_category.html"
    form_class = DepCategoryCreateForm

    def form_valid(self, form):
        service = services.DepCategoryModelService(self.request)
        service.create(form.cleaned_data)
        return redirect("money:index")


@login_required(login_url="login/")
def create_with_category(request):
    if request.method == "POST":
        form = DepCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added !")
            return redirect("money:create_with_category")
    form = DepCategoryForm()
    context = {"form": form, "categories": models.WithCategory.objects.all()}
    return render(request, "money/create_with_category.html", context)


def deposit(request):
    if request.method == "POST":
        # Создаём экземпляр формы и заполняем данными из запроса:
        form = DepositForm(request.POST)
        # Проверка валидности данных формы:
        if form.is_valid():
            # Добавляем запись в базу
            update_balance = models.Deposit(
                uan=form.cleaned_data.get("uan"),
                category=form.cleaned_data.get("categories")[0],
                title=form.cleaned_data.get("title"),
            )
            update_balance.save()
            messages.success(request, "Transaction completed")
            return redirect("money:index")
    # Если это GET, создать форму по умолчанию.
    form = DepositForm()
    return render(request, "money/deposit.html", {"form": form})


def withdraw(request):
    # форма несвязана c моделью
    # чем продиктована необходимость
    # создания переменной 'update_balance'
    # уместно переписать
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            update_balance = models.Withdraw(
                uan=form.cleaned_data.get("uan"),
                category=form.cleaned_data.get("categories")[0],
                title=form.cleaned_data.get("title"),
            )
            update_balance.save()
            messages.success(request, "Transaction completed")
            return redirect("money:index")
        messages.error(request, "Error")
    form = WithdrawForm()
    return render(request, "money/withdraw.html", {"form": form})


def register(request):
    # форма связана c моделью
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # работает без 'data'
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration completed")
            return redirect("money:index")
        messages.error(request, "Error")
    form = UserRegisterForm()

    return render(request, "money/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)  # !data
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("money:index")
        messages.error(request, "Error")
    form = UserLoginForm()
    return render(request, "money/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("money:index")
