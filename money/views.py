from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages

from . import models
from .forms import DepositForm, WithdrawForm

from datetime import date


def index(request):
    # year = int(t[0:4])
    t = str(date.today())
    month = int(t[5:7])
    positive_balance = models.Deposit.objects.aggregate(Sum("uan"))["uan__sum"]
    negative_balance = models.Withdraw.objects.aggregate(Sum("uan"))["uan__sum"]
    total_balance = positive_balance - negative_balance
    balances = {
        "positive_balance": positive_balance,
        "negative_balance": negative_balance,
        "total_balance": total_balance,
    }
    context = {
        "all_deposits": models.Deposit.objects.filter(date__month=month).order_by('-date'),
        "all_withdraws": models.Withdraw.objects.filter(date__month=month).order_by('-date'),
        "balances": balances,
    }
    return render(request, "money/index.html", context)


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
            messages.success(request, 'Transaction completed')
            return HttpResponseRedirect(reverse("index"))
    # Если это GET, создать форму по умолчанию.
    else:
        form = DepositForm()
    return render(request, "money/deposit.html", {"form": form})


def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            update_balance = models.Withdraw(
                uan=form.cleaned_data.get("uan"),
                category=form.cleaned_data.get("categories")[0],
                title=form.cleaned_data.get("title"),
            )
            update_balance.save()
            messages.success(request, 'Transaction completed')
            return HttpResponseRedirect(reverse("index"))
    else:
        form = WithdrawForm()
    return render(request, "money/withdraw.html", {'form': form})

