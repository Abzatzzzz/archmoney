from django.shortcuts import render
from . import models
from django.db.models import Sum

from datetime import date


def index(request):
    # year = int(t[0:4])
    t = str(date.today())
    month = int(t[5:7])
    positive_balance = models.Deposit.objects.aggregate(Sum("uan"))["uan__sum"]
    negative_balance = models.Withdraw.objects.aggregate(Sum("uan"))[
        "uan__sum"
    ]
    total_balance = positive_balance - negative_balance
    balances = {
        "positive_balance": positive_balance,
        "negative_balance": negative_balance,
        "total_balance": total_balance,
    }
    context = {
        "all_deposits": models.Deposit.objects.filter(date__month=month),
        "all_withdraws": models.Withdraw.objects.filter(date__month=month),
        "balances": balances,
    }
    return render(request, "money/index.html", context)


def deposit(request):
    return render(request, "money/deposit.html")


def withdraw(request):
    return render(request, "money/withdraw.html")
