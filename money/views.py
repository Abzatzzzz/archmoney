from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import services
from . import repositories
from . import models
from .forms import (
    DepositCreateForm,
    WithdrawForm,
    DepCategoryCreateForm,
    WithCategoryCreateForm,
)

from datetime import date


class DepCategoryListView(LoginRequiredMixin, ListView):
    template_name = "money/list_dep_categories.html"
    context_object_name = "categories"
    login_url = "/login/"

    def get_queryset(self):
        rep = repositories.DepCategoryModelRepository(self.request)
        return rep.get_user_depcategories()


class WithCategoryListView(LoginRequiredMixin, ListView):
    template_name = "money/list_with_categories.html"
    context_object_name = "categories"
    login_url = "/login/"

    def get_queryset(self):
        rep = repositories.WithCategoryModelRepository(self.request)
        return rep.get_user_withcategories()


class DepCategoryCreateView(CreateView):
    template_name = "money/create_dep_category.html"
    form_class = DepCategoryCreateForm

    def form_valid(self, form):
        service = services.DepCategoryModelService(self.request)
        service.create(form.cleaned_data)
        return redirect("money:depcategories")


class WithCategoryCreateView(CreateView):
    template_name = "money/create_with_category.html"
    form_class = WithCategoryCreateForm

    def form_valid(self, form):
        service = services.WithCategoryModelService(self.request)
        service.create(form.cleaned_data)
        return redirect("money:withcategories")


class DepositCreateView(CreateView):
    template_name = "money/deposit.html"
    form_class = DepositCreateForm

    def form_valid(self, form):
        service = services.DepositModelService(self.request)
        service.create(form.cleaned_data)
        return redirect("money:index")


def withdraw(request):
    """
    форма не связана c моделью
    чем продиктована необходимость
    создания переменной 'update_balance'
    уместно переписать

    """
    if request.method == "POST":
        # Создаём экземпляр формы и заполняем данными из запроса:
        form = WithdrawForm(request.POST)
        # Проверка валидности данных формы:
        if form.is_valid():
            # Добавляем запись в базу
            update_balance = models.Withdraw(
                uan=form.cleaned_data.get("uan"),
                category=form.cleaned_data.get("categories")[0],
                title=form.cleaned_data.get("title"),
                user=request.user,
            )
            update_balance.save()
            messages.success(request, "Transaction completed")
            return redirect("money:index")
        messages.error(request, "Error")
    # Если это GET, создать форму по умолчанию.
    form = WithdrawForm()
    return render(request, "money/withdraw.html", {"form": form})


@login_required(login_url="login/")
def index(request):
    # year = int(t[0:4])
    t = str(date.today())
    month = int(t[5:7])
    positive_balance = models.Deposit.objects.filter(date__month=month).aggregate(
        Sum("uan")
    )["uan__sum"]
    negative_balance = models.Withdraw.objects.filter(date__month=month).aggregate(
        Sum("uan")
    )["uan__sum"]
    context = {
        "all_deposits": models.Deposit.objects.filter(date__month=month).order_by(
            "-date"
        ),
        "all_withdraws": models.Withdraw.objects.filter(date__month=month).order_by(
            "-date"
        ),
        "positive_balance": positive_balance,
        "negative_balance": negative_balance,
    }
    if positive_balance and negative_balance:
        context["total_balance"] = positive_balance - negative_balance
    else:
        context["total_balance"] = "0"
    return render(request, "money/index.html", context)


def register(request):
    # форма связана c моделью
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # работает без 'data'
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration completed")
            return redirect("money:index")
        messages.error(request, "Error")
    form = UserCreationForm()

    return render(request, "money/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # !data
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("money:index")
        messages.error(request, "Error")
    form = AuthenticationForm()
    return render(request, "money/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("money:index")
